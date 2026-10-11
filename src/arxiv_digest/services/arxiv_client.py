"""ArXiv API client for fetching research papers.

Architecture notes
------------------
* A single :class:`arxiv.Client` (built once via :func:`make_client`) enforces
  the >=3s rate limit, pagination and retries for the whole run.  Wave 2 owns
  instantiation; this module exposes the factory.
* Queries are *fielded* (``cat:cs.GR AND (abs:"..." OR ti:"...")``) via
  :func:`arxiv_digest.core.config.build_category_query` — never bare ``all:``
  keyword searches, which were the root cause of off-topic noise.
* "New today" is keyed on ``published.date()`` (the v1 submission date), not
  ``updated.date()`` — a v2 revision of an old paper no longer hijacks the
  email slice.  See :func:`filter_recent_day`.
* Code-link lookup is intentionally NOT done here; it lives in
  :mod:`arxiv_digest.services.code_link_client` and is called after scoring so
  we only spend API calls on papers that survive the relevance filter.
"""

from __future__ import annotations

import re
import logging
import warnings
from datetime import date, timedelta
from typing import Dict, List, Optional, Tuple

import arxiv

from ..core.config import Category, RateLimitConfig, build_category_query
from ..models.paper import Paper
from ..utils.date_utils import format_authors


_VERSION_RE = re.compile(r"v\d+$")
ARXIV_ABS_URL = "http://arxiv.org/abs/"


def _strip_version(paper_id: str) -> str:
    """Strip a trailing arXiv version suffix, e.g. ``2506.14513v2`` -> ``2506.14513``."""
    return _VERSION_RE.sub("", paper_id)


def make_client(rate_limit: RateLimitConfig) -> arxiv.Client:
    """Build a single shared :class:`arxiv.Client` honoring the configured rate limit."""
    return arxiv.Client(
        page_size=100,
        delay_seconds=rate_limit.arxiv_delay_seconds,
        num_retries=3,
    )


def filter_recent_day(papers: List[Paper], window_days: int = 1) -> List[Paper]:
    """Return papers published within ``window_days`` of the newest paper.

    "Newest" is keyed on ``published.date()`` (v1 submission), not
    ``updated.date()``.  ``window_days=1`` keeps only papers from the single
    most recent published day; larger windows are inclusive of the trailing days.
    """
    if not papers:
        return []
    newest = max(p.published for p in papers)
    cutoff = newest - timedelta(days=window_days - 1)
    return [p for p in papers if p.published >= cutoff]


class ArXivClient:
    """Client for interacting with the ArXiv API."""

    def __init__(self):
        pass

    # ------------------------------------------------------------------
    # New API
    # ------------------------------------------------------------------
    def fetch_category(
        self,
        category: Category,
        max_results: int,
        max_age_days: int,
        client: arxiv.Client,
    ) -> List[Paper]:
        """Fetch and post-filter papers for one :class:`Category`.

        Args:
            category: Category with cat codes + keyword filters.
            max_results: Cap on arXiv results to request.
            max_age_days: Drop papers whose ``published`` date is older than
                this many days (keeps the working set fresh).  ``<= 0`` disables.
            client: A shared :class:`arxiv.Client` (see :func:`make_client`).

        Returns:
            List of :class:`Paper` objects (may be partial on network errors).
        """
        query = build_category_query(category)
        if not query:
            logging.warning(
                "Category %r produced an empty query (no cat_codes and no "
                "include_keywords); skipping", category.name
            )
            return []

        logging.info("Fetching %r: %s", category.name, query)
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )

        cutoff = date.today() - timedelta(days=max_age_days) if max_age_days and max_age_days > 0 else None

        papers: List[Paper] = []
        try:
            for result in client.results(search):
                paper = self._build_paper(result)
                if paper is None:
                    continue
                if cutoff and paper.published < cutoff:
                    continue
                papers.append(paper)
        except arxiv.UnexpectedEmptyPageError as e:
            logging.warning(
                "ArXiv API returned empty page for %r: %s (returning %d partial)",
                category.name, e, len(papers),
            )
        except Exception as e:  # network / HTTP / parse -> return partial
            logging.error(
                "Error fetching papers for %r: %s (returning %d partial)",
                category.name, e, len(papers),
            )

        logging.info("Fetched %d papers for %r", len(papers), category.name)
        return papers

    def _build_paper(self, result) -> Optional[Paper]:
        """Convert one :class:`arxiv.Result` into a :class:`Paper`."""
        try:
            short_id = result.get_short_id()
            paper_key = _strip_version(short_id)
            title = result.title
            abstract = result.summary.replace("\n", " ")
            first_author = format_authors(result.authors, first_author=True)

            primary = getattr(result, "primary_category", "") or ""
            all_cats_raw = getattr(result, "categories", None)
            if all_cats_raw:
                all_categories = list(all_cats_raw)
            elif primary:
                all_categories = [primary]
            else:
                all_categories = []

            return Paper(
                paper_key=paper_key,
                title=title,
                authors_str=first_author,
                abstract=abstract,
                published=result.published.date(),
                updated=result.updated.date(),
                primary_category=primary,
                all_categories=all_categories,
                entry_id=result.entry_id,
                abs_url=f"{ARXIV_ABS_URL}{paper_key}",
            )
        except Exception as e:
            logging.error("Error processing arXiv result: %s", e)
            return None

    # ------------------------------------------------------------------
    # Deprecated compat wrapper
    # ------------------------------------------------------------------
    def get_daily_papers(
        self,
        topic: str,
        query: str = "computational design",
        max_results: int = 5,
    ) -> Tuple[Dict, Dict, Dict, Dict, Optional[date]]:
        """Deprecated.  Fetch papers and return the legacy 4-dict shape.

        Kept so the not-yet-rewritten ``cli/main.py`` keeps importing cleanly.
        New code should call :meth:`fetch_category` + :func:`filter_recent_day`
        and render via :meth:`Paper.to_md_row` / :meth:`Paper.to_web_row`.

        Returns:
            ``(email_content, email_content_web, main_content,
            main_content_web, most_recent_date)`` where each ``*_content`` is
            ``{topic: {paper_key: row_str}}``.
        """
        warnings.warn(
            "ArXivClient.get_daily_papers is deprecated; use fetch_category() "
            "+ filter_recent_day() with Paper.to_md_row()/to_web_row().",
            DeprecationWarning,
            stacklevel=2,
        )
        logging.warning("get_daily_papers(%r) called via deprecated path", topic)

        # Build a transient Category from the raw query so fetch_category can
        # run.  ``query`` is treated as a single abstract phrase.
        cat = Category(
            name=topic,
            cat_codes=[],
            include_keywords=[query] if query else [],
        )
        # If the caller passed an already-built query string (legacy kv shim),
        # fall back to using it verbatim by injecting it as the raw search query.
        client = make_client(RateLimitConfig())
        if query and (" OR " in query or ":" in query):
            papers = self._fetch_raw_query(query, max_results, client)
        else:
            papers = self.fetch_category(cat, max_results, max_age_days=0, client=client)

        main_content: Dict[str, str] = {}
        main_content_web: Dict[str, str] = {}
        for p in papers:
            main_content[p.paper_key] = p.to_md_row()
            main_content_web[p.paper_key] = p.to_web_row()

        recent = filter_recent_day(papers, window_days=1)
        email_content = {p.paper_key: p.to_md_row() for p in recent}
        email_content_web = {p.paper_key: p.to_web_row() for p in recent}

        most_recent = max((p.published for p in papers), default=None)
        return (
            {topic: email_content},
            {topic: email_content_web},
            {topic: main_content},
            {topic: main_content_web},
            most_recent,
        )

    def _fetch_raw_query(
        self, query: str, max_results: int, client: arxiv.Client
    ) -> List[Paper]:
        """Run a caller-supplied query string verbatim (legacy compat path)."""
        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )
        papers: List[Paper] = []
        try:
            for result in client.results(search):
                paper = self._build_paper(result)
                if paper is not None:
                    papers.append(paper)
        except arxiv.UnexpectedEmptyPageError as e:
            logging.warning("ArXiv empty page for raw query %r: %s", query, e)
        except Exception as e:
            logging.error("Error fetching raw query %r: %s", query, e)
        return papers
