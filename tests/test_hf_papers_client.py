"""Unit tests for the HuggingFace Daily Papers client (community-signal source).

The client is the defensive template: every failure path returns ``[]`` so an
HF outage never crashes a run. These tests pin that contract plus the
filter / sort / mapping behavior.
"""

from unittest.mock import patch, MagicMock

from src.arxiv_digest.services.hf_papers_client import HfPapersClient, _extract_links
from src.arxiv_digest.models.paper import Paper


def _hf_item(paper_id, title, upvotes, summary="An abstract.",
             github=None, project=None, author="Jane Doe"):
    """Build a realistic HF daily-papers API item."""
    inner = {
        "id": paper_id,
        "title": title,
        "summary": summary,
        "upvotes": upvotes,
        "authors": [{"name": author}, {"name": "Co Author"}],
    }
    if github is not None:
        inner["githubRepo"] = github
    if project is not None:
        inner["projectPage"] = project
    return {
        "paper": inner,
        "numComments": 3,
        "publishedAt": "2026-07-20T13:00:00.000Z",
        "submittedOnDailyAt": "2026-07-20T13:00:00.000Z",
    }


def _mock_response(items, status=200):
    mock = MagicMock()
    mock.status_code = status
    mock.json.return_value = items
    return mock


@patch("src.arxiv_digest.services.hf_papers_client.requests.get")
def test_hf_fetch_maps_filters_sorts_caps(mock_get):
    """Survivors are: above min_upvotes, sorted desc, capped at top_n."""
    mock_get.return_value = _mock_response([
        _hf_item("2607.001", "Low", upvotes=10),     # below floor -> dropped
        _hf_item("2607.002", "Mid", upvotes=50),
        _hf_item("2607.003", "High", upvotes=113),
        _hf_item("2607.004", "Also", upvotes=80),
    ])

    client = HfPapersClient()
    papers = client.fetch_daily_papers(
        date_str="2026-07-20", section_name="Trending on HuggingFace",
        min_upvotes=15, top_n=2,
    )

    assert len(papers) == 2
    # Sorted desc by upvotes, capped at 2.
    assert [p.upvotes for p in papers] == [113, 80]
    # All below-floor papers dropped.
    assert all(p.upvotes >= 15 for p in papers)


@patch("src.arxiv_digest.services.hf_papers_client.requests.get")
def test_hf_paper_marked_community_signal_with_fields(mock_get):
    """Mapped Paper carries community-signal fields + built abs_url + code."""
    mock_get.return_value = _mock_response([
        _hf_item("2607.003", "Big Paper", upvotes=113,
                 github="https://github.com/org/repo",
                 summary="We propose a novel method."),
    ])

    papers = HfPapersClient().fetch_daily_papers(
        date_str="2026-07-20", section_name="Trending on HuggingFace",
        min_upvotes=15, top_n=10,
    )
    assert len(papers) == 1
    p = papers[0]
    assert isinstance(p, Paper)
    assert p.is_community_signal is True
    assert p.upvotes == 113
    assert p.score == 0.0                       # neutral; popularity in upvotes
    assert p.paper_key == "2607.003"
    assert p.abs_url == "http://arxiv.org/abs/2607.003"
    assert p.code_url == "https://github.com/org/repo"
    assert p.authors_str == "Jane Doe"
    assert p.category == "Trending on HuggingFace"
    assert p.published.isoformat() == "2026-07-20"   # feature date, not arxiv v1


@patch("src.arxiv_digest.services.hf_papers_client.requests.get")
def test_hf_code_url_falls_back_to_project_page(mock_get):
    """No githubRepo -> a github projectPage is used; non-github page -> None."""
    mock_get.return_value = _mock_response([
        _hf_item("2607.010", "Project Only", upvotes=40,
                 project="https://github.com/org/other"),
        _hf_item("2607.011", "No Code", upvotes=40,
                 project="https://example.com/non-github"),
    ])
    papers = HfPapersClient().fetch_daily_papers(
        date_str="2026-07-20", section_name="HF",
        min_upvotes=15, top_n=10,
    )
    by_key = {p.paper_key: p for p in papers}
    assert by_key["2607.010"].code_url == "https://github.com/org/other"
    assert by_key["2607.011"].code_url is None


@patch("src.arxiv_digest.services.hf_papers_client.requests.get")
def test_hf_malformed_items_skipped_not_fatal(mock_get):
    """Items missing required id/title or with a bad inner shape are skipped."""
    mock_get.return_value = _mock_response([
        {"paper": {"title": "No Id", "upvotes": 99}},     # missing id
        {"paper": {"id": "2607.020", "upvotes": 99}},     # missing title
        {"paper": "not-a-dict"},                          # bad inner
        "not-a-dict-item",                                # bad top-level
        _hf_item("2607.021", "Good", upvotes=99),         # the one survivor
    ])
    papers = HfPapersClient().fetch_daily_papers(
        date_str="2026-07-20", section_name="HF",
        min_upvotes=15, top_n=10,
    )
    assert [p.paper_key for p in papers] == ["2607.021"]


@patch("src.arxiv_digest.services.hf_papers_client.requests.get")
def test_hf_http_error_returns_empty(mock_get):
    """Non-200 -> [] (never raises)."""
    mock_get.return_value = _mock_response([], status=503)
    papers = HfPapersClient().fetch_daily_papers(
        date_str="2026-07-20", section_name="HF", min_upvotes=15, top_n=10,
    )
    assert papers == []


@patch("src.arxiv_digest.services.hf_papers_client.requests.get")
def test_hf_request_exception_returns_empty(mock_get):
    """Network failure -> [] (never raises)."""
    import requests
    mock_get.side_effect = requests.RequestException("boom")
    papers = HfPapersClient().fetch_daily_papers(
        date_str="2026-07-20", section_name="HF", min_upvotes=15, top_n=10,
    )
    assert papers == []


@patch("src.arxiv_digest.services.hf_papers_client.requests.get")
def test_hf_non_list_payload_returns_empty(mock_get):
    """A non-list JSON body (e.g. an error dict) -> []."""
    mock = MagicMock()
    mock.status_code = 200
    mock.json.return_value = {"error": "bad date"}
    mock_get.return_value = mock
    papers = HfPapersClient().fetch_daily_papers(
        date_str="2026-07-20", section_name="HF", min_upvotes=15, top_n=10,
    )
    assert papers == []


@patch("src.arxiv_digest.services.hf_papers_client.requests.get")
def test_hf_empty_day_returns_empty(mock_get):
    """A quiet HF day (empty list) -> [] (no top_n padding)."""
    mock_get.return_value = _mock_response([])
    papers = HfPapersClient().fetch_daily_papers(
        date_str="2026-07-20", section_name="HF", min_upvotes=15, top_n=10,
    )
    assert papers == []


# --- _extract_links: code vs project split ------------------------------
def test_extract_links_splits_github_repo_and_demo_page():
    """GitHub repo -> code; non-github projectPage -> project (both kept)."""
    code, project = _extract_links({
        "githubRepo": "https://github.com/org/repo",
        "projectPage": "https://robotics.xiaomi.com/demo.html",
    })
    assert code == "https://github.com/org/repo"
    assert project == "https://robotics.xiaomi.com/demo.html"


def test_extract_links_github_projectpage_only_becomes_code():
    """A lone GitHub projectPage (no repo) is code, not project."""
    code, project = _extract_links({"projectPage": "https://github.com/org/repo"})
    assert code == "https://github.com/org/repo"
    assert project is None


def test_extract_links_neither_present():
    assert _extract_links({}) == (None, None)


def test_extract_links_repo_wins_over_github_projectpage():
    """Repo + a GitHub projectPage -> repo is code; no project_url."""
    code, project = _extract_links({
        "githubRepo": "https://github.com/a/b",
        "projectPage": "https://github.com/a/b-site",
    })
    assert code == "https://github.com/a/b"
    assert project is None


@patch("src.arxiv_digest.services.hf_papers_client.requests.get")
def test_hf_project_url_preserved_on_paper(mock_get):
    """A non-github demo page flows through to Paper.project_url."""
    mock_get.return_value = _mock_response([
        _hf_item("2607.030", "Demo Paper", upvotes=50,
                 github="https://github.com/o/r",
                 project="https://aka.ms/demo"),
    ])
    papers = HfPapersClient().fetch_daily_papers(
        date_str="2026-07-20", section_name="HF", min_upvotes=15, top_n=10,
    )
    p = papers[0]
    assert p.code_url == "https://github.com/o/r"
    assert p.project_url == "https://aka.ms/demo"
