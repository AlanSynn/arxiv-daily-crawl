"""Tests for the rewritten ArXiv client (fetch_category + filter_recent_day).

These exercise the new API: a single shared ``arxiv.Client`` whose
``results()`` generator is mocked, paper building, version stripping, age
filtering, and the published-date-keyed "recent day" filter (the fix for the
old ``updated``-based bug where a v2 revision of an old paper hijacked the
slice).
"""

from datetime import date, timedelta
from unittest.mock import MagicMock

import arxiv
import pytest

from src.arxiv_digest.core.config import Category, RateLimitConfig
from src.arxiv_digest.models.paper import Paper
from src.arxiv_digest.services.arxiv_client import (
    ArXivClient,
    filter_recent_day,
    make_client,
    _strip_version,
)


# ---------------------------------------------------------------------------
# Mock arxiv primitives
# ---------------------------------------------------------------------------
class MockAuthor:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class MockDate:
    def __init__(self, date_obj):
        self._date = date_obj

    def date(self):
        return self._date


class MockArxivResult:
    """Mimics the attributes of arxiv.Result used by _build_paper."""

    def __init__(
        self,
        paper_id,
        title,
        authors,
        published_date,
        updated_date,
        abstract="Test abstract",
        primary_category="cs.GR",
        categories=None,
    ):
        self.paper_id = paper_id
        self.title = title
        self.authors = [MockAuthor(a) for a in authors]
        self.published = MockDate(published_date)
        self.updated = MockDate(updated_date)
        self.summary = abstract
        self.entry_id = f"http://arxiv.org/abs/{paper_id}"
        self.comment = None
        self.primary_category = primary_category
        self.categories = categories if categories is not None else [primary_category]

    def get_short_id(self):
        return self.paper_id


def _client_with_results(results):
    """Build an ArXivClient whose fetch_category uses a mocked arxiv.Client.

    The returned mock ``arxiv.Client`` exposes ``results(search)`` returning an
    iterator over ``results`` and records the search it was called with.
    """
    mock_arxiv_client = MagicMock()
    mock_arxiv_client.results.return_value = iter(results)
    return mock_arxiv_client


# ---------------------------------------------------------------------------
# _strip_version
# ---------------------------------------------------------------------------
def test_strip_version_removes_suffix():
    assert _strip_version("2506.14513v2") == "2506.14513"
    assert _strip_version("2506.14513v12") == "2506.14513"
    assert _strip_version("2506.14513") == "2506.14513"  # no version
    assert _strip_version("2506.14513v1") == "2506.14513"


# ---------------------------------------------------------------------------
# make_client
# ---------------------------------------------------------------------------
def test_make_client_honors_rate_limit():
    rl = RateLimitConfig(arxiv_delay_seconds=5.0)
    client = make_client(rl)
    assert isinstance(client, arxiv.Client)
    assert client.delay_seconds == 5.0
    assert client.num_retries == 3


# ---------------------------------------------------------------------------
# fetch_category
# ---------------------------------------------------------------------------
@pytest.fixture
def motion_category():
    return Category(
        name="Character Motion",
        cat_codes=["cs.GR"],
        include_keywords=["character animation", "motion synthesis"],
    )


@pytest.fixture
def mixed_date_results():
    today = date.today()
    yesterday = today - timedelta(days=1)
    two_days_ago = today - timedelta(days=2)
    return [
        MockArxivResult("2506.00001v1", "Today Motion Synthesis", ["Jane"], today, today),
        MockArxivResult("2506.00002v1", "Another Today", ["John"], today, today),
        MockArxivResult("2506.00003v1", "Yesterday Paper", ["Bob"], yesterday, yesterday),
        MockArxivResult("2506.00004v1", "Old Paper", ["Alice"], two_days_ago, two_days_ago),
    ]


def test_fetch_category_builds_papers(motion_category, mixed_date_results):
    mock_client = _client_with_results(mixed_date_results)
    client = ArXivClient()
    papers = client.fetch_category(motion_category, max_results=10, max_age_days=0, client=mock_client)

    assert len(papers) == 4
    assert all(isinstance(p, Paper) for p in papers)
    # paper_key has version stripped
    assert papers[0].paper_key == "2506.00001"
    assert papers[0].abs_url == "http://arxiv.org/abs/2506.00001"
    # published keying (not updated)
    assert papers[0].published == date.today()


def test_fetch_category_uses_fielded_query(motion_category, mixed_date_results):
    mock_client = _client_with_results(mixed_date_results)
    client = ArXivClient()
    client.fetch_category(motion_category, max_results=10, max_age_days=0, client=mock_client)

    mock_client.results.assert_called_once()
    search = mock_client.results.call_args[0][0]
    assert isinstance(search, arxiv.Search)
    # Fielded query: must contain a cat: clause and abs:"..." phrases, NOT a
    # bare keyword.
    assert "cat:cs.GR" in search.query
    assert 'abs:"character animation"' in search.query
    assert search.sort_by == arxiv.SortCriterion.SubmittedDate
    assert search.sort_order == arxiv.SortOrder.Descending


def test_fetch_category_age_filter(motion_category):
    """max_age_days=N drops papers published more than N days ago (age cap)."""
    today = date.today()
    yesterday = today - timedelta(days=1)
    old = today - timedelta(days=10)
    results = [
        MockArxivResult("2506.00001v1", "Today", ["A"], today, today),
        MockArxivResult("2506.00002v1", "Yesterday", ["B"], yesterday, yesterday),
        MockArxivResult("2506.00003v1", "Old", ["C"], old, old),
    ]

    client = ArXivClient()

    # max_age_days=0 disables the age filter -> all 3 kept
    mc0 = _client_with_results(results)
    assert len(client.fetch_category(motion_category, 10, max_age_days=0, client=mc0)) == 3

    # max_age_days=5: cutoff = today - 5 days; the 10-day-old paper is dropped
    mc5 = _client_with_results(results)
    papers = client.fetch_category(motion_category, 10, max_age_days=5, client=mc5)
    assert len(papers) == 2
    assert {p.paper_key for p in papers} == {"2506.00001", "2506.00002"}

    # max_age_days=1 keeps today + yesterday (cutoff = today - 1 day = yesterday)
    mc1 = _client_with_results(results)
    papers = client.fetch_category(motion_category, 10, max_age_days=1, client=mc1)
    assert {p.paper_key for p in papers} == {"2506.00001", "2506.00002"}


def test_fetch_category_handles_empty_page(motion_category):
    mock_client = MagicMock()
    # UnexpectedEmptyPageError requires (url, retry, raw_feed) at construction.
    mock_client.results.side_effect = arxiv.UnexpectedEmptyPageError("http://x", 3, {})
    client = ArXivClient()
    papers = client.fetch_category(motion_category, max_results=10, max_age_days=0, client=mock_client)
    assert papers == []


def test_fetch_category_handles_network_error(motion_category):
    mock_client = MagicMock()
    mock_client.results.side_effect = ConnectionError("network down")
    client = ArXivClient()
    papers = client.fetch_category(motion_category, max_results=10, max_age_days=0, client=mock_client)
    assert papers == []


def test_fetch_category_empty_query_returns_empty():
    """Category with no cat_codes and no keywords -> empty query -> skip."""
    cat = Category(name="Empty", cat_codes=[], include_keywords=[])
    mock_client = _client_with_results([])
    client = ArXivClient()
    papers = client.fetch_category(cat, max_results=10, max_age_days=0, client=mock_client)
    assert papers == []
    mock_client.results.assert_not_called()


def test_fetch_category_partial_on_mid_stream_error(motion_category):
    """If the results generator errors partway, keep already-collected papers."""
    today = date.today()
    good = MockArxivResult("2506.00001v1", "Good", ["A"], today, today)

    def gen():
        yield good
        raise arxiv.UnexpectedEmptyPageError("http://x", 3, {})

    mock_client = MagicMock()
    mock_client.results.return_value = gen()
    client = ArXivClient()
    papers = client.fetch_category(motion_category, max_results=10, max_age_days=0, client=mock_client)
    assert len(papers) == 1
    assert papers[0].title == "Good"


def test_build_paper_captures_categories():
    result = MockArxivResult(
        "2506.99999v1", "T", ["A"], date.today(), date.today(),
        primary_category="cs.GR", categories=["cs.GR", "cs.CV"],
    )
    client = ArXivClient()
    paper = client._build_paper(result)
    assert paper.primary_category == "cs.GR"
    assert paper.all_categories == ["cs.GR", "cs.CV"]


# ---------------------------------------------------------------------------
# filter_recent_day
# ---------------------------------------------------------------------------
def _mk_paper(paper_id, published, title="t"):
    return Paper(
        paper_key=paper_id,
        title=title,
        authors_str="Author",
        abstract="abs",
        published=published,
        updated=published,
        primary_category="cs.GR",
        all_categories=["cs.GR"],
        entry_id=f"http://arxiv.org/abs/{paper_id}",
        abs_url=f"http://arxiv.org/abs/{paper_id}",
    )


def test_filter_recent_day_keeps_only_newest_day():
    today = date.today()
    yesterday = today - timedelta(days=1)
    papers = [
        _mk_paper("1", today),
        _mk_paper("2", today),
        _mk_paper("3", yesterday),
    ]
    recent = filter_recent_day(papers, window_days=1)
    assert len(recent) == 2
    assert all(p.published == today for p in recent)


def test_filter_recent_day_empty():
    assert filter_recent_day([], window_days=1) == []


def test_filter_recent_day_keys_on_published_not_updated():
    """The fix: a v2 revision (recent updated, old published) is NOT 'new today'."""
    today = date.today()
    long_ago = today - timedelta(days=400)
    papers = [
        _mk_paper("recent-v1", today),                      # genuinely new
        _mk_paper("old-paper-v2", long_ago),                # old paper, revised today
    ]
    recent = filter_recent_day(papers, window_days=1)
    assert len(recent) == 1
    assert recent[0].paper_key == "recent-v1"


def test_filter_recent_day_window_inclusive():
    today = date.today()
    yesterday = today - timedelta(days=1)
    two_days_ago = today - timedelta(days=2)
    papers = [
        _mk_paper("1", today),
        _mk_paper("2", yesterday),
        _mk_paper("3", two_days_ago),
    ]
    recent = filter_recent_day(papers, window_days=2)
    assert {p.paper_key for p in recent} == {"1", "2"}


# ---------------------------------------------------------------------------
# Paper row serializers
# ---------------------------------------------------------------------------
def test_to_md_row_null_code():
    p = _mk_paper("2506.00001", date(2025, 6, 23), "Paper One")
    row = p.to_md_row()
    assert row == "|**2025-06-23**|**Paper One**|Author et.al.|[@2506.00001](http://arxiv.org/abs/2506.00001)|null|\n"
    assert row.endswith("null|\n")  # real trailing newline


def test_to_md_row_with_code():
    p = _mk_paper("2506.00001", date(2025, 6, 23), "Paper One")
    p.code_url = "https://github.com/x/y"
    row = p.to_md_row()
    assert "**[link](https://github.com/x/y)**" in row


def test_to_web_row_includes_abstract():
    p = _mk_paper("2506.00001", date(2025, 6, 23), "Paper One")
    p.abstract = "A great abstract"
    web = p.to_web_row()
    assert web.startswith("- 2025-06-23, **Paper One**")
    assert "Author et.al." in web
    assert "**Abstract:** A great abstract" in web


def test_to_md_row_is_five_columns():
    """Archiver depends on exactly 5 pipe-delimited columns."""
    p = _mk_paper("2506.00001", date(2025, 6, 23), "T")
    parts = p.to_md_row().rstrip("\n").split("|")
    # leading '' + 5 columns + trailing '' = 7 parts
    assert len(parts) == 7
