"""Email-rendering integration tests for the HuggingFace section.

The HF section is email-only and community-signal papers must NOT leak into
the relevance ranking. These pin: (1) Top-5 excludes them, (2) they render an
upvote badge instead of a score badge, (3) the section appears in the index.
"""

from datetime import date

from src.daily_arxiv.models.paper import Paper
from src.daily_arxiv.services.email_service import EmailService


def _scored(key, score=0.5, cat="Character Motion"):
    return Paper(
        paper_key=key, title=f"Scored {key}", authors_str="A",
        abstract="Short abstract.", published=date(2026, 7, 20),
        updated=date(2026, 7, 20), primary_category="cs.GR",
        all_categories=["cs.GR"], entry_id=f"http://arxiv.org/abs/{key}",
        abs_url=f"http://arxiv.org/abs/{key}", code_url=None,
        category=cat, score=score, matched_keywords=[],
        is_community_signal=False,
    )


def _hf(key, upvotes, section="Trending on HuggingFace"):
    return Paper(
        paper_key=key, title=f"HF {key}", authors_str="B",
        abstract="HF abstract.", published=date(2026, 7, 20),
        updated=date(2026, 7, 20), primary_category="HF",
        all_categories=["HF"], entry_id=f"http://arxiv.org/abs/{key}",
        abs_url=f"http://arxiv.org/abs/{key}", code_url=None,
        category=section, score=0.0, matched_keywords=[],
        upvotes=upvotes, is_community_signal=True,
    )


def test_compute_top5_excludes_community_signal():
    """Top-5 must keep only scored arXiv papers even when HF papers are present."""
    scored = [_scored(f"2607.{i:03d}", score=0.1 * i) for i in range(1, 7)]  # 6 papers
    hf = [_hf("2607.900", 999), _hf("2607.901", 200)]                        # 2 HF

    top5 = EmailService._compute_top5({"Character Motion": scored, "HF": hf})

    # No community-signal paper in the top-5.
    assert all(not p.is_community_signal for p in top5)
    # Exactly 5, highest-scored first.
    assert len(top5) == 5
    assert [p.paper_key for p in top5] == [
        "2607.006", "2607.005", "2607.004", "2607.003", "2607.002",
    ]


def test_render_email_hf_section_uses_upvote_badge():
    """HF paper shows an upvote badge (▲ N); scored paper shows the score."""
    config = {'email_settings': {'enabled': True}}
    service = EmailService(config)
    scored = _scored("2607.100", score=0.77)
    hf = _hf("2607.900", 113)

    html = service.render_email(
        {"Character Motion": [scored], "Trending on HuggingFace": [hf]},
        "2026-07-20", {"total": 2, "categories": 2, "threshold": 0.15},
    )

    # Upvote badge present for the HF paper; score badge for the scored paper.
    assert "▲ 113" in html
    assert "0.77" in html
    # Both titles render.
    assert "Scored 2607.100" in html
    assert "HF 2607.900" in html
    # The HF section heading appears (section index is local to the render).
    assert "Trending on HuggingFace" in html


def test_render_email_hf_section_in_index():
    """The HF section gets an index chip + a § section like any other."""
    config = {'email_settings': {'enabled': True}}
    service = EmailService(config)
    hf = _hf("2607.900", 40)

    html = service.render_email(
        {"Trending on HuggingFace": [hf]},
        "2026-07-20", {"total": 1, "categories": 1, "threshold": None},
    )

    # INDEX eyebrow + the HF section name as an anchor target.
    assert "INDEX" in html
    assert 'href="#trending-on-huggingface"' in html
    assert 'id="trending-on-huggingface"' in html
    # Single paper -> Top-5 block skipped (total <= 5).
    assert "TOP 5 BY RELEVANCE" not in html


def test_render_email_top5_skips_hf_when_slice_short():
    """With <5 scored papers + HF papers present, HF never pads the Top-5.

    Regression guard: HF papers have score 0.0, so without the
    community-signal skip they would sneak into a short Top-5 and display a
    meaningless 0.00 score badge.
    """
    config = {'email_settings': {'enabled': True}}
    service = EmailService(config)
    # 6 scored + 4 HF -> total 10 (>5) so the Top-5 block renders.
    scored = [_scored(f"2607.{i:03d}", score=0.1 * i) for i in range(1, 7)]
    hf = [_hf(f"2607.9{i:02d}", 500 - i) for i in range(4)]

    html = service.render_email(
        {"Character Motion": scored, "Trending on HuggingFace": hf},
        "2026-07-20",
    )

    assert "TOP 5 BY RELEVANCE" in html
    # No HF title leaked into the Top-5 mini-cards.
    for p in hf:
        assert p.title not in html.split("TOP 5 BY RELEVANCE")[1].split("INDEX")[0]


# --- Link row + inline abstract (post-toggle removal) -------------------
def test_render_email_hf_paper_full_link_row():
    """HF paper link row carries arXiv + code + project + hf paper page."""
    config = {'email_settings': {'enabled': True}}
    service = EmailService(config)
    hf = _hf("2607.900", 113)
    hf.code_url = "https://github.com/o/r"
    hf.project_url = "https://aka.ms/demo"
    html = service.render_email(
        {"Trending on HuggingFace": [hf]}, "2026-07-20",
        {"total": 1, "categories": 1, "threshold": None},
    )
    assert "huggingface.co/papers/2607.900" in html
    assert "github.com/o/r" in html and ">code<" in html
    assert "aka.ms/demo" in html and ">project<" in html
    assert ">hf<" in html


def test_render_email_no_hf_link_for_scored_papers():
    """Scored arXiv papers do NOT get the hf paper-page link."""
    config = {'email_settings': {'enabled': True}}
    service = EmailService(config)
    scored = _scored("2607.100", score=0.5)
    scored.code_url = "https://github.com/o/r"
    html = service.render_email({"Character Motion": [scored]}, "2026-07-20")
    assert "huggingface.co/papers/2607.100" not in html
    assert ">code<" in html


def test_render_email_abstract_is_inline_not_toggle():
    """No <details>/<summary>; ABSTRACT shown inline (email-client robust)."""
    config = {'email_settings': {'enabled': True}}
    service = EmailService(config)
    p = _scored("2607.100", score=0.5)
    html = service.render_email({"Character Motion": [p]}, "2026-07-20")
    assert "<details" not in html
    assert "<summary" not in html
    assert "▾" not in html
    assert "ABSTRACT" in html
    assert "Short abstract." in html      # body visible inline (not hidden)
