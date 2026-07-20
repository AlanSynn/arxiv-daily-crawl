"""Tests for config parsing and arXiv field-query construction."""

import os
import tempfile

import yaml

from src.daily_arxiv.core.config import (
    Category,
    RateLimitConfig,
    ScoringConfig,
    TocConfig,
    build_category_query,
    load_config,
    validate_config,
)


# ---------------------------------------------------------------------------
# build_category_query
# ---------------------------------------------------------------------------
def test_single_cat_clause():
    cat = Category(name="t", cat_codes=["cs.GR"], include_keywords=["rigging"])
    assert build_category_query(cat) == 'cat:cs.GR AND (abs:rigging)'


def test_multi_cat_clause_wrapped_in_parens():
    cat = Category(name="t", cat_codes=["cs.GR", "cs.CV"], include_keywords=["rigging"])
    assert build_category_query(cat) == '(cat:cs.GR OR cat:cs.CV) AND (abs:rigging)'


def test_multi_word_keyword_is_quoted_abs():
    cat = Category(name="t", cat_codes=["cs.GR"], include_keywords=["character animation"])
    assert build_category_query(cat) == 'cat:cs.GR AND (abs:"character animation")'


def test_ti_prefix_emits_title_field():
    cat = Category(name="t", cat_codes=["cs.LG"], include_keywords=["ti:world model"])
    assert build_category_query(cat) == 'cat:cs.LG AND (ti:"world model")'


def test_ti_prefix_single_word_not_quoted():
    cat = Category(name="t", cat_codes=["cs.GR"], include_keywords=["ti:motion"])
    assert build_category_query(cat) == 'cat:cs.GR AND (ti:motion)'


def test_multiple_keywords_joined_with_or_and_wrapped():
    cat = Category(
        name="t",
        cat_codes=["cs.GR", "cs.CV"],
        include_keywords=["character animation", "motion diffusion", "ti:motion"],
    )
    q = build_category_query(cat)
    assert q.startswith("(cat:cs.GR OR cat:cs.CV) AND (")
    assert 'abs:"character animation"' in q
    assert 'abs:"motion diffusion"' in q
    assert "ti:motion" in q
    # joined with OR
    assert " OR " in q


def test_exclude_keywords_not_in_query():
    cat = Category(
        name="t",
        cat_codes=["cs.GR"],
        include_keywords=["animation"],
        exclude_keywords=["motion planning", "optical flow"],
    )
    q = build_category_query(cat)
    assert "motion planning" not in q
    assert "optical flow" not in q
    assert "NOT" not in q


def test_no_cat_codes_only_keyword_clause():
    cat = Category(name="t", cat_codes=[], include_keywords=["animation", "rigging"])
    assert build_category_query(cat) == "(abs:animation OR abs:rigging)"


def test_no_keywords_only_cat_clause():
    cat = Category(name="t", cat_codes=["cs.GR"], include_keywords=[])
    assert build_category_query(cat) == "cat:cs.GR"


def test_empty_category_returns_empty_query():
    cat = Category(name="t", cat_codes=[], include_keywords=[])
    assert build_category_query(cat) == ""


def test_empty_phrase_keywords_are_skipped():
    """A misconfigured ``ti:``/``abs:``/``""`` keyword must not yield a bare,
    malformed arXiv term (``ti:`` / ``abs:``) in the query."""
    cat = Category(
        name="t",
        cat_codes=["cs.GR"],
        include_keywords=["animation", "ti:", "abs:", "", "   ", "rigging"],
    )
    q = build_category_query(cat)
    # Only the two valid keywords survive; no bare ``ti:``/``abs:`` term and no
    # doubled ``OR`` from the dropped entries.
    assert q == "cat:cs.GR AND (abs:animation OR abs:rigging)"


def test_only_empty_keywords_yields_cat_clause_only():
    """If every include keyword is an empty phrase, the keyword clause drops out."""
    cat = Category(name="t", cat_codes=["cs.GR"], include_keywords=["ti:", "abs:", ""])
    assert build_category_query(cat) == "cat:cs.GR"


def test_real_character_motion_category_query():
    """The exact category from config.yaml produces the expected shape."""
    cat = Category(
        name="Character Motion Synthesis & Animation",
        cat_codes=["cs.GR", "cs.CV"],
        include_keywords=[
            "character animation", "motion synthesis", "motion generation",
            "human motion", "motion diffusion", "physics-based motion",
            "motion capture", "skeletal animation", "ti:motion",
        ],
    )
    q = build_category_query(cat)
    assert q == (
        '(cat:cs.GR OR cat:cs.CV) AND ('
        'abs:"character animation" OR abs:"motion synthesis" OR '
        'abs:"motion generation" OR abs:"human motion" OR '
        'abs:"motion diffusion" OR abs:"physics-based motion" OR '
        'abs:"motion capture" OR abs:"skeletal animation" OR ti:motion)'
    )
    assert q.endswith(")")


def test_real_world_models_query_uses_title_field():
    cat = Category(
        name="World Models & Generative Video",
        cat_codes=["cs.LG", "cs.CV", "cs.RO"],
        include_keywords=[
            "ti:world model", "ti:world models", "world simulator",
            "interactive video generation", "video diffusion",
        ],
    )
    q = build_category_query(cat)
    # multi-word ti: keywords must be quoted title terms
    assert 'ti:"world model"' in q
    assert 'ti:"world models"' in q
    assert 'abs:"world simulator"' in q
    assert q.startswith("(cat:cs.LG OR cat:cs.CV OR cat:cs.RO) AND (")


# ---------------------------------------------------------------------------
# Config loading / parsing
# ---------------------------------------------------------------------------
def _write_config(payload: dict) -> str:
    fd, path = tempfile.mkstemp(suffix=".yaml")
    with os.fdopen(fd, "w") as f:
        yaml.dump(payload, f)
    return path


def test_load_config_parses_categories_and_blocks():
    path = _write_config({
        "base_url": "https://example.com/",
        "max_results": 7,
        "categories": [
            {"name": "A", "cat_codes": ["cs.GR"], "include_keywords": ["x"], "priority": 3},
        ],
        "scoring": {"threshold": 0.2, "title_weight": 3.0},
        "rate_limit": {"arxiv_delay_seconds": 4.0, "code_link_enabled": False},
        "toc": {"enabled": False, "paper_list_path": "./x.md"},
    })
    try:
        cfg = load_config(path)
    finally:
        os.unlink(path)

    assert len(cfg["categories"]) == 1
    assert isinstance(cfg["categories"][0], Category)
    assert cfg["categories"][0].priority == 3
    assert isinstance(cfg["scoring"], ScoringConfig)
    assert cfg["scoring"].threshold == 0.2
    assert cfg["scoring"].title_weight == 3.0
    assert isinstance(cfg["rate_limit"], RateLimitConfig)
    assert cfg["rate_limit"].arxiv_delay_seconds == 4.0
    assert cfg["rate_limit"].code_link_enabled is False
    assert isinstance(cfg["toc"], TocConfig)
    assert cfg["toc"].enabled is False
    # kv backward-compat shim still populated
    assert "A" in cfg["kv"]


def test_load_config_legacy_keywords_shim():
    path = _write_config({
        "base_url": "https://example.com/",
        "max_results": 5,
        "keywords": {"Legacy Topic": {"filters": ["foo", "bar baz"]}},
    })
    try:
        cfg = load_config(path)
    finally:
        os.unlink(path)

    # Legacy keywords auto-converted to a Category (pure keyword mode).
    assert len(cfg["categories"]) == 1
    cat = cfg["categories"][0]
    assert cat.name == "Legacy Topic"
    assert cat.cat_codes == []
    assert cat.include_keywords == ["foo", "bar baz"]
    # validate should pass via the shim
    assert validate_config(cfg) is True


def test_validate_config_requires_categories():
    cfg = {"base_url": "x", "max_results": 5}  # no categories / keywords
    assert validate_config(cfg) is False


def test_validate_config_missing_base_url():
    cfg = {"max_results": 5, "categories": [{"name": "A", "cat_codes": ["cs.GR"]}]}
    assert validate_config(cfg) is False


def test_load_real_config_yaml():
    """The shipped config.yaml must load with 10 categories and pass validation."""
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cfg = load_config(os.path.join(here, "config.yaml"))
    assert len(cfg["categories"]) == 10
    assert validate_config(cfg) is True
    assert cfg["max_results"] == 40
    names = [c.name for c in cfg["categories"]]
    assert "Character Motion Synthesis & Animation" in names
    assert "World Models & Generative Video" in names
