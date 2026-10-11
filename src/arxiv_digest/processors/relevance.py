"""Relevance scoring for fetched papers.

Pure, dependency-light scoring with no network I/O.  A paper is scored against
a single :class:`~arxiv_digest.core.config.Category`: include keywords add
weight (title hits weighted higher than abstract hits), exclude keywords apply
a penalty.  The score is normalized to ``[0.0, 1.0]`` so a single abstract hit
is ~0.33 and a single title hit ~0.67 with the default config.
"""

from __future__ import annotations

import re
from typing import List, Tuple

from ..core.config import Category, ScoringConfig
from ..models.paper import Paper


def _strip_prefix(keyword: str) -> str:
    """Drop a ``ti:``/``abs:`` field prefix so substring matching uses the phrase only."""
    if keyword.startswith("ti:"):
        return keyword[3:]
    if keyword.startswith("abs:"):
        return keyword[4:]
    return keyword


def _phrase_in_text(phrase: str, text: str) -> bool:
    """Whole-word containment test (word-boundary anchored).

    Used for exclude matching: a bare substring test makes ``sport`` fire on
    ``transport``/``transportation`` (common in robotics abstracts) and zero
    out on-topic papers. ``\\b`` anchors the phrase at word edges.
    """
    if not phrase:
        return False
    return re.search(rf"\b{re.escape(phrase)}\b", text) is not None


class RelevanceScorer:
    """Score papers against a category's keyword filters."""

    def __init__(self, scoring: ScoringConfig):
        self.scoring = scoring

    def score(self, paper: Paper, category: Category) -> Tuple[float, List[str]]:
        """Score ``paper`` against ``category``.

        Returns ``(score, matched_keywords)`` where ``score`` is clamped to
        ``[0.0, 1.0]`` and ``matched_keywords`` lists every include keyword
        (prefix-stripped, original casing) that hit the title or abstract.
        """
        title_lower = paper.title.lower()
        text_lower = (paper.title + " " + paper.abstract).lower()

        title_hits: List[str] = []
        abs_hits: List[str] = []
        for keyword in category.include_keywords:
            phrase = _strip_prefix(keyword).strip()
            if not phrase:
                continue
            phrase_lower = phrase.lower()
            if phrase_lower in title_lower:
                title_hits.append(phrase)
            elif phrase_lower in text_lower:
                abs_hits.append(phrase)

        title_weight = self.scoring.title_weight
        # Raw weight: title hits count at title_weight, abstract hits at 1.0.
        raw = title_weight * len(title_hits) + self.scoring.include_boost * len(abs_hits)

        # Normalize so one abstract hit ~= include_boost/(title_weight+boost).
        denom = title_weight + self.scoring.include_boost
        score = raw / denom if denom > 0 else 0.0

        # Exclude penalty: any exclude hit subtracts exclude_penalty (floor 0).
        # Word-boundary matched so ``sport`` does not fire on ``transport``.
        exclude_hit = any(
            _phrase_in_text(_strip_prefix(k).strip().lower(), text_lower)
            for k in category.exclude_keywords
            if k and k.strip()
        )
        if exclude_hit:
            score = max(0.0, score - self.scoring.exclude_penalty)

        return min(1.0, score), title_hits + abs_hits

    def passes(self, score: float) -> bool:
        """Whether a score clears the configured relevance threshold."""
        return score >= self.scoring.threshold
