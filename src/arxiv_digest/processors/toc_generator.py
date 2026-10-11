"""Table-of-contents and flat paper-list generation (pure, no I/O).

Two renderers fed by the orchestration layer:

* :func:`generate_toc` — a GitHub-markdown TOC block prepended to
  ``ARXIV_PAPERS.md``.  Category anchors are produced by
  :func:`arxiv_digest.utils.date_utils.github_slug` so the links line up with
  the rendered ``## {category}`` headings.
* :func:`generate_paper_list` — a flat, deduplicated ``PAPER_LIST.md`` table.
  A paper that matched several categories appears once (highest-score wins),
  sorted newest-first.

Both functions emit real newlines (``\\n``), never literal ``\\\\n``.
"""

from __future__ import annotations

from datetime import date
from typing import List, Tuple

from ..models.paper import Paper
from ..utils.date_utils import github_slug


def generate_toc(
    categories_with_papers: List[Tuple[str, List[Paper]]], target_date: date
) -> str:
    """Build the GitHub-markdown TOC block prepended to ``ARXIV_PAPERS.md``.

    Args:
        categories_with_papers: ``(category_name, papers)`` pairs; categories
            with empty paper lists are skipped.
        target_date: Date stamped into the "Updated on" header and the
            ``<summary>`` (report-generation date).

    Returns:
        A markdown block whose anchors match GitHub's rendered heading ids.
    """
    date_pretty = target_date.strftime("%Y.%m.%d")
    date_iso = target_date.strftime("%Y-%m-%d")

    lines = [
        f"## 📚 Updated on {date_pretty}",
        "",
        "<details open>",
        f"<summary>📑 Table of Contents — {date_iso}</summary>",
        "",
        "**By category**",
    ]

    for category_name, papers in categories_with_papers:
        if not papers:
            continue
        anchor = github_slug(category_name)
        lines.append(f"- [{category_name}](#{anchor}) ({len(papers)})")

    lines.append("")
    lines.append("</details>")

    return "\n".join(lines)


def generate_paper_list(scored_papers: List[Paper]) -> str:
    """Render the flat, deduplicated ``PAPER_LIST.md`` table.

    A paper is listed once even if it survived scoring for several categories
    — the highest-``score`` occurrence is kept.  Rows are sorted by
    ``published`` descending, then ``score`` descending.

    Args:
        scored_papers: All scored papers across categories (may contain
            duplicates by ``paper_key``).

    Returns:
        Markdown table string with a header row, separator, and one row per
        deduplicated paper.
    """
    # Dedup by paper_key, keeping the highest-score occurrence.
    best: dict[str, Paper] = {}
    for paper in scored_papers:
        prev = best.get(paper.paper_key)
        if prev is None or paper.score > prev.score:
            best[paper.paper_key] = paper

    ordered = sorted(
        best.values(), key=lambda p: (p.published, p.score), reverse=True
    )

    lines = [
        "# 📄 Paper List",
        "",
        "> Flat list of all tracked papers, newest first. Auto-generated.",
        "",
        "| Date | Title | Category | Score | Matched | arXiv | Code |",
        "|---|---|---|---|---|---|---|",
    ]

    for paper in ordered:
        code_field = f"[link]({paper.code_url})" if paper.code_url else "null"
        category_label = paper.category or ""
        # Matched include keywords ("why this paper"). Escape pipes so a
        # keyword containing one can't break the table row.
        matched_field = ", ".join(paper.matched_keywords or []).replace("|", "\\|")
        lines.append(
            f"| {paper.published.isoformat()} | **{paper.title}** | "
            f"{category_label} | {paper.score:.2f} | {matched_field} | "
            f"[@{paper.paper_key}]({paper.abs_url}) | {code_field} |"
        )

    return "\n".join(lines)
