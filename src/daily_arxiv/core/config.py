"""Configuration loading, schema, and arXiv query building for daily-arxiv.

The config schema is dataclass-based (no pydantic dependency):

* ``categories``   — list of :class:`Category`, each mapping a display name to
  arXiv ``cat:`` codes plus include/exclude keyword lists.
* ``scoring``      — :class:`ScoringConfig` thresholds/weights for the
  :class:`~daily_arxiv.processors.relevance.RelevanceScorer`.
* ``rate_limit``   — :class:`RateLimitConfig` for the arXiv + code-link clients.

A legacy ``keywords:`` block (no ``categories:``) is auto-converted into a
single default :class:`Category` with empty ``cat_codes`` (pure keyword mode)
and a deprecation warning is logged, so old configs never hard-fail.
"""

from __future__ import annotations

import os
import logging
from dataclasses import dataclass, field
from typing import Any, Dict, List

import yaml


# ---------------------------------------------------------------------------
# Schema dataclasses
# ---------------------------------------------------------------------------
@dataclass
class Category:
    """A fetchable topic: arXiv category codes + keyword filters.

    ``include_keywords`` may target the abstract (default) or the title.  A
    keyword prefixed with ``ti:`` is matched against the title only — both in
    the generated arXiv query (emitted as ``ti:"..."``) and by the scorer.
    """

    name: str
    cat_codes: List[str] = field(default_factory=list)
    include_keywords: List[str] = field(default_factory=list)
    exclude_keywords: List[str] = field(default_factory=list)
    priority: int = 0


@dataclass
class ScoringConfig:
    """Weights/thresholds for :class:`RelevanceScorer`."""

    threshold: float = 0.15
    title_weight: float = 2.0
    include_boost: float = 1.0
    exclude_penalty: float = 1.0


@dataclass
class RateLimitConfig:
    """Rate-limit + feature-flag settings for the I/O clients."""

    arxiv_delay_seconds: float = 3.0
    code_link_delay_seconds: float = 1.0
    code_link_enabled: bool = True


@dataclass
class TocConfig:
    """Table-of-contents generation settings (consumed by Wave 2)."""

    enabled: bool = True
    paper_list_path: str = "./logs/PAPER_LIST.md"
    group_by_date: bool = True


# ---------------------------------------------------------------------------
# Query building
# ---------------------------------------------------------------------------
def _keyword_field(keyword: str) -> tuple[str, str]:
    """Split a configured keyword into ``(field, phrase)``.

    ``field`` is ``"ti"`` for title-only keywords (``ti:`` prefix) and
    ``"abs"`` otherwise.  The prefix is stripped from the returned phrase.
    """
    if keyword.startswith("ti:"):
        return "ti", keyword[3:].strip()
    if keyword.startswith("abs:"):
        return "abs", keyword[4:].strip()
    return "abs", keyword


def _format_term(field: str, phrase: str) -> str:
    """Format a single keyword as an arXiv fielded term.

    Multi-word phrases are quoted; single tokens are bare.
    """
    if len(phrase.split()) > 1:
        return f'{field}:"{phrase}"'
    return f"{field}:{phrase}"


def build_category_query(category: Category) -> str:
    """Construct an arXiv field-query string for a category.

    * Cat clause: one code -> ``cat:cs.GR``; several -> ``(cat:cs.GR OR cat:cs.CV)``.
    * Keyword clause: each include keyword becomes ``abs:"..."`` (or ``ti:"..."``
      when prefixed with ``ti:``), joined by ``OR`` and wrapped in parens.
    * Final: ``<cat_clause> AND (<keyword_clause>)``.  With no include
      keywords only the cat clause is emitted; with no cat codes only the
      keyword clause is emitted.

    Exclude keywords are deliberately NOT part of the query — they are applied
    client-side by the :class:`RelevanceScorer` as a penalty, because arXiv's
    query language has no robust NOT-over-substring operator.
    """
    cat_parts = [f"cat:{code}" for code in category.cat_codes if code]
    if len(cat_parts) == 1:
        cat_clause = cat_parts[0]
    elif len(cat_parts) > 1:
        cat_clause = "(" + " OR ".join(cat_parts) + ")"
    else:
        cat_clause = ""

    kw_terms = [
        _format_term(field, phrase)
        for kw in category.include_keywords
        if kw and kw.strip()
        for field, phrase in [_keyword_field(kw)]
        if phrase  # skip empty phrases (e.g. "ti:" / "abs:" / "")
    ]
    kw_clause = "(" + " OR ".join(kw_terms) + ")" if kw_terms else ""

    if cat_clause and kw_clause:
        return f"{cat_clause} AND {kw_clause}"
    return cat_clause or kw_clause


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------
def _parse_categories(raw: List[Dict[str, Any]]) -> List[Category]:
    """Parse a raw ``categories:`` YAML list into :class:`Category` objects."""
    categories: List[Category] = []
    if not raw:
        return categories
    for item in raw:
        if not isinstance(item, dict):
            continue
        name = item.get("name") or ""
        categories.append(
            Category(
                name=name,
                cat_codes=list(item.get("cat_codes") or []),
                include_keywords=[str(k) for k in (item.get("include_keywords") or [])],
                exclude_keywords=[str(k) for k in (item.get("exclude_keywords") or [])],
                priority=int(item.get("priority") or 0),
            )
        )
    return categories


def _migrate_legacy_keywords(raw_keywords: Dict[str, Any]) -> List[Category]:
    """Convert a legacy ``keywords:`` block into Category objects.

    Each legacy topic becomes its own :class:`Category` with empty ``cat_codes``
    (pure keyword mode) so old configs keep working.  The original ``filters``
    list becomes ``include_keywords``.
    """
    categories: List[Category] = []
    for name, settings in raw_keywords.items():
        settings = settings or {}
        filters = settings.get("filters") if isinstance(settings, dict) else None
        categories.append(
            Category(
                name=name,
                cat_codes=[],
                include_keywords=[str(f) for f in (filters or [])],
                exclude_keywords=[],
                priority=0,
            )
        )
    return categories


def _parse_scoring(raw: Dict[str, Any]) -> ScoringConfig:
    raw = raw or {}
    return ScoringConfig(
        threshold=float(raw.get("threshold", 0.15)),
        title_weight=float(raw.get("title_weight", 2.0)),
        include_boost=float(raw.get("include_boost", 1.0)),
        exclude_penalty=float(raw.get("exclude_penalty", 1.0)),
    )


def _parse_rate_limit(raw: Dict[str, Any]) -> RateLimitConfig:
    raw = raw or {}
    return RateLimitConfig(
        arxiv_delay_seconds=float(raw.get("arxiv_delay_seconds", 3.0)),
        code_link_delay_seconds=float(raw.get("code_link_delay_seconds", 1.0)),
        code_link_enabled=bool(raw.get("code_link_enabled", True)),
    )


def _parse_toc(raw: Dict[str, Any]) -> TocConfig:
    raw = raw or {}
    return TocConfig(
        enabled=bool(raw.get("enabled", True)),
        paper_list_path=str(raw.get("paper_list_path", "./logs/PAPER_LIST.md")),
        group_by_date=bool(raw.get("group_by_date", True)),
    )


def _legacy_query_string(filters: List[str]) -> str:
    """Build the legacy bare ``"phrase" OR word`` query string for old code paths.

    Kept for the deprecated ``config['kv']`` shim so any consumer still reading
    ``config['kv']`` (e.g. the not-yet-rewritten ``cli/main.py``) keeps working.
    """
    escape = '"'
    or_operator = " OR "
    result = ""
    for idx, term in enumerate(filters):
        term = str(term)
        if len(term.split()) > 1:
            result += f"{escape}{term}{escape}"
        else:
            result += term
        if idx != len(filters) - 1:
            result += or_operator
    return result


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------
def load_config(config_file: str) -> Dict[str, Any]:
    """Load configuration from a YAML file into a rich dictionary.

    The returned dict keeps every original top-level key (for backward
    compatibility) and adds the parsed dataclass objects under ``categories``,
    ``scoring``, ``rate_limit``, and ``toc``.

    Args:
        config_file: Path to the configuration file.

    Returns:
        Dictionary containing processed configuration.
    """
    with open(config_file, "r", encoding="utf-8") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    # --- env var substitution for email settings -----------------------
    if "email_settings" in config:
        email_settings = config["email_settings"]
        if "${SMTP_USER}" in email_settings.get("smtp_user", ""):
            email_settings["smtp_user"] = os.environ.get("SMTP_USER", "")
        if "${SMTP_PASSWORD}" in email_settings.get("smtp_password", ""):
            email_settings["smtp_password"] = os.environ.get("SMTP_PASSWORD", "")

    if "${EMAIL_RECIPIENT}" in config.get("email_recipient", ""):
        config["email_recipient"] = os.environ.get("EMAIL_RECIPIENT", "alansynn@gatech.edu")

    if "log_dir" not in config:
        config["log_dir"] = "./logs"

    # --- categories (new) or legacy keywords (shim) --------------------
    has_categories = bool(config.get("categories"))
    has_legacy_keywords = bool(config.get("keywords"))

    if has_categories:
        categories = _parse_categories(config["categories"])
    elif has_legacy_keywords:
        logging.warning(
            "config.yaml uses the legacy 'keywords:' block; auto-converting to "
            "categories (pure keyword mode, no arXiv cat: scoping). Migrate to "
            "the 'categories:' schema with cat_codes for precision."
        )
        categories = _migrate_legacy_keywords(config["keywords"])
    else:
        categories = []

    config["categories"] = categories
    config["scoring"] = _parse_scoring(config.get("scoring"))
    config["rate_limit"] = _parse_rate_limit(config.get("rate_limit"))
    config["toc"] = _parse_toc(config.get("toc"))

    # Backward-compat ``kv`` shim: map topic name -> legacy bare query string.
    # New code should call build_category_query(category) instead.
    kv: Dict[str, str] = {}
    for cat in categories:
        kv[cat.name] = build_category_query(cat)
    config["kv"] = kv

    logging.info(f"Loaded configuration from {config_file} ({len(categories)} categories)")
    return config


def validate_config(config: Dict[str, Any]) -> bool:
    """Validate configuration completeness.

    Requires either a ``categories`` block or a legacy ``keywords`` block
    (the latter is shimmed into categories by :func:`load_config`).
    """
    required_keys = ["base_url", "max_results"]
    for key in required_keys:
        if key not in config:
            logging.error(f"Missing required configuration key: {key}")
            return False

    categories = config.get("categories")
    if not categories:
        logging.error("No categories defined in configuration (need 'categories:' block)")
        return False

    return True


# Re-exported so ``from core.config import Category`` works for type checks.
__all__ = [
    "Category",
    "ScoringConfig",
    "RateLimitConfig",
    "TocConfig",
    "build_category_query",
    "load_config",
    "validate_config",
]
