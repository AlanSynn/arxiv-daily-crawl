"""Paper data model for arxiv-digest.

A :class:`Paper` is the canonical representation of a single arXiv paper as it
flows through the pipeline (fetch -> score -> render).  Row serializers keep the
exact pipe-delimited schema the archiver depends on (5 columns: date, title,
authors, arxiv link, code link).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Optional


@dataclass
class Paper:
    """A single arXiv paper.

    Attributes:
        paper_key: Version-stripped arXiv id, e.g. ``2506.14513``.
        title: Paper title.
        authors_str: First author display name (e.g. ``"Jane Smith"``); the
            ``et.al.`` suffix is appended by the row serializers so it is never
            duplicated.
        abstract: Cleaned abstract text (newlines collapsed to spaces).
        published: v1 submission date (used to key "new today").
        updated: Last revision date.
        primary_category: Primary arXiv category, e.g. ``"cs.GR"``.
        all_categories: Every arXiv category the paper is filed under.
        entry_id: Raw arXiv entry id / canonical URL.
        abs_url: Human abstract URL, ``http://arxiv.org/abs/{paper_key}``.
        code_url: Optional code-repository URL (filled by CodeLinkClient, or
            from HuggingFace ``githubRepo`` for community-signal papers).
        project_url: Optional non-code project/demo page — typically the
            paper's website (e.g. a HuggingFace ``projectPage`` that isn't a
            GitHub repo). Kept separate from ``code_url`` so both a repo and
            a demo site can link out at once.
        category: Display category name (assigned at orchestration).
        score: Relevance score in ``[0.0, 1.0]`` (assigned by RelevanceScorer).
        matched_keywords: Include keywords that matched (for transparency).
        upvotes: HuggingFace upvote count (community-signal papers only); the
            relevance ``score`` field stays in ``[0.0, 1.0]`` for keyword
            papers, so popularity is kept in its own field.
        is_community_signal: True for HuggingFace-sourced papers. Marks the
            paper as belonging to the parallel HF pipeline — it bypasses the
            arXiv publish-day slice, never enters ``seen_best``/``all_scored``,
            and renders an upvote badge instead of a score badge.
    """

    paper_key: str
    title: str
    authors_str: str
    abstract: str
    published: date
    updated: date
    primary_category: str
    all_categories: list[str]
    entry_id: str
    abs_url: str
    code_url: Optional[str] = None
    project_url: Optional[str] = None  # non-code demo/project page (HF papers)
    # Assigned at orchestration time:
    category: Optional[str] = None
    score: float = 0.0
    matched_keywords: list[str] = field(default_factory=list)
    # HuggingFace community-signal fields (default off — zero impact on the
    # keyword pipeline / existing callers).
    upvotes: Optional[int] = None
    is_community_signal: bool = False

    # ------------------------------------------------------------------
    # Row serializers
    # ------------------------------------------------------------------
    def to_md_row(self) -> str:
        """Markdown-table row for the readme/report output.

        Schema (5 pipe-delimited columns, must stay stable for the archiver):
        ``|date|title|authors|arxiv|code|`` with a trailing real newline.
        """
        code_field = f"**[link]({self.code_url})**" if self.code_url else "null"
        return (
            f"|**{self.published}**|**{self.title}**|{self.authors_str} et.al.|"
            f"[@{self.paper_key}]({self.abs_url})|{code_field}|\n"
        )

    def to_web_row(self) -> str:
        """Web/email-friendly list-item rendering (includes the abstract)."""
        if self.code_url:
            head = (
                f"- {self.published}, **{self.title}**, {self.authors_str} et.al., "
                f"Paper: [@{self.paper_key}]({self.abs_url}), "
                f"Code: **[link]({self.code_url})**\n"
            )
        else:
            head = (
                f"- {self.published}, **{self.title}**, {self.authors_str} et.al., "
                f"Paper: [@{self.paper_key}]({self.abs_url})\n"
            )
        return f"{head}> **Abstract:** {self.abstract}\n"
