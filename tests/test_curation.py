"""Batch 4 curation tests: per-keyword weights, email caps, priority ordering,
and matched-keywords rendering."""

import os
import tempfile
from datetime import date

import yaml

from src.arxiv_digest.cli.main import DailyArxivApp
from src.arxiv_digest.core.config import Category, ScoringConfig, load_config
from src.arxiv_digest.models.paper import Paper
from src.arxiv_digest.processors.relevance import RelevanceScorer
from src.arxiv_digest.processors.toc_generator import generate_paper_list
from src.arxiv_digest.services.email_service import EmailService


def _paper(key, cat, score, matched=None, community=False):
    return Paper(
        paper_key=key, title=f"T {key}", authors_str="A", abstract="abs",
        published=date(2025, 6, 17), updated=date(2025, 6, 17),
        primary_category="cs.GR", all_categories=["cs.GR"],
        entry_id=f"http://arxiv.org/abs/{key}",
        abs_url=f"http://arxiv.org/abs/{key}", code_url=None,
        category=cat, score=score, matched_keywords=matched or [],
        is_community_signal=community,
    )


# ---------------------------------------------------------------------------
# Per-keyword weights
# ---------------------------------------------------------------------------
def _scored_paper(title, abstract):
    return Paper(
        paper_key="2506.00001", title=title, authors_str="A", abstract=abstract,
        published=date(2025, 6, 17), updated=date(2025, 6, 17),
        primary_category="cs.GR", all_categories=["cs.GR"],
        entry_id="http://arxiv.org/abs/2506.00001",
        abs_url="http://arxiv.org/abs/2506.00001", code_url=None,
    )


def test_keyword_weight_amplifies_score():
    """A weighted title hit must outscore the same hit at default weight."""
    paper = _scored_paper("Linkage Synthesis via Diffusion", "We study mechanisms.")

    base_cat = Category(name="t", cat_codes=["cs.GR"], include_keywords=["linkage synthesis"])
    weighted_cat = Category(
        name="t", cat_codes=["cs.GR"], include_keywords=["linkage synthesis"],
        keyword_weights={"linkage synthesis": 3.0},
    )

    scorer = RelevanceScorer(ScoringConfig())
    base_score, _ = scorer.score(paper, base_cat)
    weighted_score, _ = scorer.score(paper, weighted_cat)

    # Title hit at title_weight=2.0 -> 2/3; with weight 3.0 -> 2*3/3 = 2 -> clamps to 1.0.
    assert abs(base_score - 2.0 / 3.0) < 1e-9
    assert weighted_score == 1.0


def test_no_weights_legacy_scores_unchanged():
    """Empty weights dict must reproduce the pre-weights scoring exactly."""
    paper = _scored_paper(
        "A Title", "motion synthesis in the wild and rigging too"
    )
    cat = Category(
        name="t", cat_codes=["cs.GR"],
        include_keywords=["motion synthesis", "rigging"],
        keyword_weights={},
    )
    scorer = RelevanceScorer(ScoringConfig())
    score, matched = scorer.score(paper, cat)
    # Two abstract hits at boost 1.0 -> 2/3.
    assert abs(score - 2.0 / 3.0) < 1e-9
    assert matched == ["motion synthesis", "rigging"]


def test_matched_keywords_dedupe_ti_and_bare_variants():
    """A bare keyword and its ``ti:`` variant both score, but the displayed
    matched list must show the phrase once."""
    from src.arxiv_digest.core.config import ScoringConfig

    paper = _scored_paper(
        "Motion Generation at Scale", "We study motion generation broadly."
    )
    cat = Category(
        name="t", cat_codes=["cs.GR"],
        include_keywords=["motion generation", "ti:motion generation"],
    )
    scorer = RelevanceScorer(ScoringConfig())
    score, matched = scorer.score(paper, cat)

    assert matched == ["motion generation"]
    # Both declared keywords still hit the title: 2 * (2.0 * 1.0) / 3 -> clamp 1.0.
    assert score == 1.0


def test_weights_lookup_by_prefixed_and_bare_form():
    """Weights keyed either as the raw keyword ('ti:x') or the bare phrase
    ('x') must both apply."""
    paper = _scored_paper("World Models for Robots", "plain abstract")
    cat = Category(
        name="t", cat_codes=["cs.LG"], include_keywords=["ti:world model"],
        keyword_weights={"ti:world model": 2.0},
    )
    cat_bare = Category(
        name="t", cat_codes=["cs.LG"], include_keywords=["ti:world model"],
        keyword_weights={"world model": 2.0},
    )
    scorer = RelevanceScorer(ScoringConfig())
    s_prefixed, _ = scorer.score(paper, cat)
    s_bare, _ = scorer.score(paper, cat_bare)
    # Title hit at title_weight 2.0 * 2.0 = 4 -> /3 -> clamps to 1.0 both ways.
    assert s_prefixed == 1.0
    assert s_bare == 1.0


# ---------------------------------------------------------------------------
# Email caps
# ---------------------------------------------------------------------------
def test_email_caps_per_category_then_global():
    """Per-cat top-N by score, then a global cap with section-order ties."""
    papers = {
        "A": [_paper("2506.00001", "A", 0.9), _paper("2506.00002", "A", 0.8),
              _paper("2506.00003", "A", 0.7)],
        "B": [_paper("2506.00004", "B", 0.85), _paper("2506.00005", "B", 0.6)],
        "C": [_paper("2506.00006", "C", 0.5)],
    }
    scoring = ScoringConfig(email_max_per_category=2, email_max_total=3)

    capped = DailyArxivApp._apply_email_caps(papers, scoring)

    # Per-cat: A keeps {0.9, 0.8}, B keeps {0.85, 0.6}, C keeps {0.5}.
    # Global top-3 by score: A/0.9, B/0.85, A/0.8 -> B/0.6 and the whole
    # C section drop out.
    assert set(capped.keys()) == {"A", "B"}
    assert [p.score for p in capped["A"]] == [0.9, 0.8]
    assert [p.score for p in capped["B"]] == [0.85]


def test_email_caps_preserve_fetch_order():
    """Kept papers stay in their original order within a section."""
    papers = {
        "A": [_paper("2506.00001", "A", 0.1), _paper("2506.00002", "A", 0.9),
              _paper("2506.00003", "A", 0.5)],
    }
    scoring = ScoringConfig(email_max_per_category=2, email_max_total=0)

    capped = DailyArxivApp._apply_email_caps(papers, scoring)

    # Top-2 by score are the 0.9 and 0.5 papers, but they must come back in
    # original fetch order (0.9 paper was second).
    assert [p.paper_key for p in capped["A"]] == ["2506.00002", "2506.00003"]


def test_email_caps_zero_disables():
    papers = {
        "A": [_paper(f"2506.{i:05d}", "A", 0.5) for i in range(20)],
    }
    scoring = ScoringConfig(email_max_per_category=0, email_max_total=0)

    capped = DailyArxivApp._apply_email_caps(papers, scoring)
    assert len(capped["A"]) == 20


def test_email_caps_ties_break_by_section_order():
    """Equal scores fill the global cap from earlier sections first."""
    papers = {
        "A": [_paper("2506.00001", "A", 0.5)],
        "B": [_paper("2506.00002", "B", 0.5)],
        "C": [_paper("2506.00003", "C", 0.5)],
    }
    scoring = ScoringConfig(email_max_per_category=0, email_max_total=2)

    capped = DailyArxivApp._apply_email_caps(papers, scoring)
    assert set(capped.keys()) == {"A", "B"}


# ---------------------------------------------------------------------------
# priority ordering
# ---------------------------------------------------------------------------
def test_load_config_sorts_categories_by_priority_desc():
    """``priority`` must reorder sections (email + markdown), higher first;
    equal priorities keep declaration order (stable sort)."""
    payload = {
        "max_results": 5,
        "categories": [
            {"name": "Low", "cat_codes": ["cs.GR"], "priority": 3},
            {"name": "High", "cat_codes": ["cs.GR"], "priority": 10},
            {"name": "Mid", "cat_codes": ["cs.GR"], "priority": 5},
            {"name": "TieHigh", "cat_codes": ["cs.GR"], "priority": 10},
        ],
    }
    fd, path = tempfile.mkstemp(suffix=".yaml")
    with os.fdopen(fd, "w") as f:
        yaml.dump(payload, f)
    try:
        cfg = load_config(path)
    finally:
        os.unlink(path)

    names = [c.name for c in cfg["categories"]]
    assert names == ["High", "TieHigh", "Mid", "Low"]


def test_load_config_parses_weights():
    payload = {
        "max_results": 5,
        "categories": [
            {"name": "A", "cat_codes": ["cs.GR"],
             "include_keywords": ["linkage synthesis", "ti:motion"],
             "weights": {"linkage synthesis": 3.0, "ti:motion": 1.5}},
        ],
    }
    fd, path = tempfile.mkstemp(suffix=".yaml")
    with os.fdopen(fd, "w") as f:
        yaml.dump(payload, f)
    try:
        cfg = load_config(path)
    finally:
        os.unlink(path)

    cat = cfg["categories"][0]
    assert cat.keyword_weights == {"linkage synthesis": 3.0, "ti:motion": 1.5}


# ---------------------------------------------------------------------------
# matched-keywords rendering
# ---------------------------------------------------------------------------
def test_email_card_shows_matched_keywords():
    config = {"email_settings": {"enabled": True}}
    service = EmailService(config)

    paper = _paper("2506.00001", "Comp Design", 0.9,
                   matched=["linkage synthesis", "four-bar linkage"])
    html = service.render_email({"Comp Design": [paper]}, "2025-06-17")

    assert "matched: linkage synthesis, four-bar linkage" in html


def test_email_card_hides_matched_for_community_signal():
    """HF papers have no keyword set — the matched line must not render."""
    config = {"email_settings": {"enabled": True}}
    service = EmailService(config)

    paper = _paper("2506.00002", "Trending on HuggingFace", 1.0,
                   matched=["should-not-appear"], community=True)
    html = service.render_email({"Trending on HuggingFace": [paper]}, "2025-06-17")

    assert "matched:" not in html
    assert "should-not-appear" not in html


def test_paper_list_renders_matched_column():
    paper = _paper("2506.00001", "Comp Design", 0.9,
                   matched=["linkage synthesis"])
    md = generate_paper_list([paper])

    assert "| Matched |" in md
    assert "linkage synthesis" in md


def test_paper_list_escapes_pipes_in_matched_keywords():
    """A keyword containing '|' must not break the markdown table row."""
    paper = _paper("2506.00001", "X", 0.9, matched=["bad|keyword"])
    md = generate_paper_list([paper])

    row = [line for line in md.splitlines() if "2506.00001" in line][0]
    # 7 columns = 8 unescaped boundary pipes (leading + 6 separators +
    # trailing); the escaped pipe inside the keyword must not count.
    assert row.count("|") - row.count("\\|") == 8
    assert "bad\\|keyword" in row
