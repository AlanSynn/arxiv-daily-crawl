"""Tests for the pure RelevanceScorer."""

from datetime import date

from src.arxiv_digest.core.config import Category, ScoringConfig
from src.arxiv_digest.models.paper import Paper
from src.arxiv_digest.processors.relevance import RelevanceScorer


def _paper(title: str, abstract: str = "") -> Paper:
    return Paper(
        paper_key="0000.00000",
        title=title,
        authors_str="Author",
        abstract=abstract,
        published=date(2025, 1, 1),
        updated=date(2025, 1, 1),
        primary_category="cs.GR",
        all_categories=["cs.GR"],
        entry_id="http://arxiv.org/abs/0000.00000",
        abs_url="http://arxiv.org/abs/0000.00000",
    )


def _category(includes=None, excludes=None) -> Category:
    return Category(
        name="t",
        cat_codes=["cs.GR"],
        include_keywords=includes or [],
        exclude_keywords=excludes or [],
    )


def test_empty_keywords_scores_zero():
    scorer = RelevanceScorer(ScoringConfig())
    p = _paper("Anything", "anything")
    score, hits = scorer.score(p, _category())
    assert score == 0.0
    assert hits == []


def test_single_abstract_hit_normalizes_to_one_third():
    # raw = 1.0 (one abs hit); denom = title_weight(2.0) + boost(1.0) = 3.0 -> 1/3
    scorer = RelevanceScorer(ScoringConfig())
    p = _paper("Some Title", "This discusses motion synthesis in depth")
    score, hits = scorer.score(p, _category(includes=["motion synthesis"]))
    assert abs(score - (1.0 / 3.0)) < 1e-9
    assert hits == ["motion synthesis"]


def test_single_title_hit_weights_double():
    # raw = title_weight(2.0); denom = 3.0 -> 2/3
    scorer = RelevanceScorer(ScoringConfig())
    p = _paper("Character animation at scale", "no keywords here")
    score, hits = scorer.score(p, _category(includes=["character animation"]))
    assert abs(score - (2.0 / 3.0)) < 1e-9
    assert hits == ["character animation"]


def test_title_hit_not_double_counted_as_abstract():
    # A keyword matching the title should count once (title weight), not twice.
    scorer = RelevanceScorer(ScoringConfig())
    p = _paper("motion everywhere", "motion motion motion")
    score, hits = scorer.score(p, _category(includes=["motion"]))
    # title hit only -> 2/3, not (2+1)/3
    assert abs(score - (2.0 / 3.0)) < 1e-9
    assert hits == ["motion"]


def test_exclude_penalty_drops_score():
    scorer = RelevanceScorer(ScoringConfig(exclude_penalty=1.0))
    p = _paper("Character animation", "but it covers motion planning")
    score, _ = scorer.score(
        p,
        _category(includes=["character animation"], excludes=["motion planning"]),
    )
    # 2/3 - 1.0 -> floored at 0.0
    assert score == 0.0


def test_exclude_penalty_partially_reduces_score():
    # Per spec pseudocode: normalize -> subtract exclude_penalty -> clamp last.
    # 2 title hits -> raw=4 -> 4/3 -> minus 0.5 -> 0.833 (no clamp needed).
    scorer = RelevanceScorer(ScoringConfig(exclude_penalty=0.5))
    p = _paper("animation rigging", "irrelevant abstract with battery")
    score, hits = scorer.score(
        p,
        _category(includes=["animation", "rigging"], excludes=["battery"]),
    )
    assert abs(score - (4.0 / 3.0 - 0.5)) < 1e-9
    assert set(hits) == {"animation", "rigging"}


def test_exclude_word_boundary_does_not_fire_on_superstring():
    # "sport" must not match inside "transport" / "transportation".
    scorer = RelevanceScorer(ScoringConfig(exclude_penalty=1.0))
    p = _paper(
        "Character animation",
        "we use a transportation dataset for animation",
    )
    score, _ = scorer.score(
        p,
        _category(includes=["character animation"], excludes=["sport"]),
    )
    assert abs(score - (2.0 / 3.0)) < 1e-9  # no penalty applied


def test_exclude_word_boundary_still_fires_on_whole_word():
    # Exact-word hits are still penalized. Boundary matching is exact-word:
    # plural/variant forms need their own exclude keyword ("sport" != "sports").
    scorer = RelevanceScorer(ScoringConfig(exclude_penalty=1.0))
    p = _paper("Character animation", "we evaluate on sport analytics")
    score, _ = scorer.score(
        p,
        _category(includes=["character animation"], excludes=["sport"]),
    )
    assert score == 0.0  # whole-word hit still penalized


def test_exclude_word_boundary_matches_phrase_edges():
    # Plural / hyphenated forms around the boundary behave sanely: the exact
    # word matches, and a hyphen-joined variant (word char vs '-') matches too.
    scorer = RelevanceScorer(ScoringConfig(exclude_penalty=1.0))
    cat = _category(includes=["animation"], excludes=["motion planning"])
    hit = _paper("Animation", "we study motion planning for characters")
    miss = _paper("Animation", "we study motion planning-adjacent work")
    score_hit, _ = scorer.score(hit, cat)
    score_miss, _ = scorer.score(miss, cat)
    assert score_hit == 0.0
    assert score_miss == 0.0  # "planning-adjacent": \b sits at the hyphen


def test_score_clamped_to_one():
    scorer = RelevanceScorer(ScoringConfig())
    p = _paper("animation rigging skeletal", "lots of animation here")
    score, hits = scorer.score(
        p, _category(includes=["animation", "rigging", "skeletal"])
    )
    assert score == 1.0  # 3 title hits -> >1.0 -> clamped
    assert len(hits) == 3


def test_ti_prefix_stripped_before_matching():
    # The scorer strips the ti: prefix and matches the phrase normally: a title
    # occurrence scores at title weight. (Title-only *enforcement* happens at
    # arXiv-query-build time, not in the scorer.) matched_keywords carries the
    # prefix-stripped phrase.
    scorer = RelevanceScorer(ScoringConfig())
    p_title = _paper("A new world model for robots", "abstract")
    cat = _category(includes=["ti:world model"])
    s_title, h_title = scorer.score(p_title, cat)
    assert h_title == ["world model"]
    assert abs(s_title - (2.0 / 3.0)) < 1e-9  # title hit at title_weight


def test_abs_prefix_also_stripped():
    scorer = RelevanceScorer(ScoringConfig())
    p = _paper("Title", "we discuss motion synthesis")
    _, hits = scorer.score(p, _category(includes=["abs:motion synthesis"]))
    assert hits == ["motion synthesis"]


def test_threshold_helper():
    scorer = RelevanceScorer(ScoringConfig(threshold=0.15))
    assert scorer.passes(0.15) is True
    assert scorer.passes(0.14) is False
    assert scorer.passes(0.5) is True


def test_matched_keywords_returned_with_original_casing():
    scorer = RelevanceScorer(ScoringConfig())
    p = _paper("Character Animation", "with Motion Synthesis")
    _, hits = scorer.score(
        p, _category(includes=["Character Animation", "Motion Synthesis", "absent"])
    )
    assert "Character Animation" in hits
    assert "Motion Synthesis" in hits
    assert "absent" not in hits
