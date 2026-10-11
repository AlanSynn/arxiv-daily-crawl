"""HuggingFace Daily Papers client — community-signal source.

Fetches the papers HuggingFace featured on a given day
(``huggingface.co/api/daily_papers?date=YYYY-MM-DD``) and maps them into the
pipeline's :class:`~arxiv_digest.models.paper.Paper` model as **community-signal**
papers (``is_community_signal=True``).

HF papers are a parallel pipeline to the keyword crawl:

* They carry an arXiv id (``paper.id``), so they share the notified-store
  keyspace — a paper already emailed via the keyword crawl is dropped here too
  (and vice versa). One notified store, two feeders.
* HF curates by its own *feature date*, not the arxiv v1 date (a June arXiv
  paper can appear in a July HF daily). Callers must therefore route HF papers
  straight into the email dict, NOT through ``filter_recent_day`` or
  ``seen_best``.
* ``paper.upvotes`` (0..~120) is the popularity signal; it is kept in its own
  field so the relevance ``score`` (``[0.0, 1.0]``) contract is untouched.

The client is defensive like :class:`~arxiv_digest.services.code_link_client.CodeLinkClient`:
every failure path returns ``[]`` — an HF outage must never crash a run or
block the arXiv-only digest.
"""

from __future__ import annotations

import datetime
import logging
from typing import Any, Dict, List, Optional, Tuple

import requests

from ..models.paper import Paper
from .arxiv_client import _strip_version
from .code_link_client import _is_github_url


_HF_DAILY_URL = "https://huggingface.co/api/daily_papers"
# Defensive page size: empirically the daily set is ~25, but ``limit`` costs
# nothing and protects us if the cap rises.
_DEFAULT_LIMIT = 50


class HfPapersClient:
    """Fetch + map HuggingFace Daily Papers into community-signal ``Paper``s.

    Args:
        timeout: Per-request HTTP timeout in seconds.
        limit: Page size hint passed to the API.
    """

    def __init__(self, timeout: float = 12.0, limit: int = _DEFAULT_LIMIT):
        self.timeout = timeout
        self.limit = limit

    def fetch_daily_papers(
        self,
        date_str: str,
        section_name: str,
        min_upvotes: int = 15,
        top_n: int = 10,
    ) -> List[Paper]:
        """Return notable HF daily papers for ``date_str`` as ``Paper`` objects.

        Filters to ``upvotes >= min_upvotes``, sorts by upvotes desc, takes
        ``top_n``. Returns ``[]`` on any HTTP / JSON / parse error or when no
        paper clears the floor (a quiet HF day). Never raises.
        """
        items = self._fetch(date_str)
        if not items:
            return []

        feature_date = _parse_date(date_str)
        papers: List[Paper] = []
        for item in items:
            paper = self._map_item(item, section_name, feature_date)
            if paper is not None:
                papers.append(paper)

        # Notable filter: above the floor, then the top-N by community vote.
        notable = [p for p in papers if (p.upvotes or 0) >= min_upvotes]
        notable.sort(key=lambda p: p.upvotes or 0, reverse=True)
        return notable[:top_n]

    def _fetch(self, date_str: str) -> List[Dict[str, Any]]:
        """Hit the HF daily-papers API. Returns ``[]`` on any failure."""
        try:
            response = requests.get(
                _HF_DAILY_URL,
                params={"date": date_str, "limit": self.limit},
                timeout=self.timeout,
            )
            if response.status_code != 200:
                logging.warning(
                    "HF daily-papers API returned %s for date=%s",
                    response.status_code, date_str,
                )
                return []
            data = response.json()
        except requests.RequestException as e:
            logging.warning("HF daily-papers request failed for %s: %s", date_str, e)
            return []
        except ValueError as e:  # bad JSON
            logging.warning("HF daily-papers returned non-JSON for %s: %s", date_str, e)
            return []

        if not isinstance(data, list):
            logging.warning("HF daily-papers returned non-list for %s", date_str)
            return []
        return data

    @staticmethod
    def _map_item(
        item: Dict[str, Any], section_name: str, feature_date: Optional[datetime.date]
    ) -> Optional[Paper]:
        """Map one HF daily-papers item to a community-signal ``Paper``.

        Returns ``None`` for items missing the required id / title (defensive —
        a malformed item is skipped, not fatal).
        """
        if not isinstance(item, dict):
            return None
        inner = item.get("paper")
        if not isinstance(inner, dict):
            return None

        paper_id = inner.get("id")
        title = inner.get("title")
        if not paper_id or not title:
            return None

        paper_id = _strip_version(str(paper_id))
        # Strip the version suffix so HF papers share the arXiv-path keyspace
        # exactly (``2610.01234v1`` and ``2610.01234`` must dedup as one key).
        authors_str = _first_author(inner.get("authors"))
        code_url, project_url = _extract_links(inner)

        return Paper(
            paper_key=paper_id,
            title=str(title),
            authors_str=authors_str,
            abstract=str(inner.get("summary") or ""),
            published=feature_date,
            updated=feature_date,
            primary_category="HF",
            all_categories=["HF"],
            entry_id=f"http://arxiv.org/abs/{paper_id}",
            abs_url=f"http://arxiv.org/abs/{paper_id}",
            code_url=code_url,
            project_url=project_url,
            category=section_name,
            score=0.0,  # left at the neutral default; popularity lives in upvotes
            matched_keywords=[],
            upvotes=_to_int(inner.get("upvotes")),
            is_community_signal=True,
        )


def _first_author(authors: Any) -> str:
    """Display name of the first author (``""`` if unknown)."""
    if isinstance(authors, list) and authors:
        first = authors[0]
        if isinstance(first, dict):
            name = first.get("name")
            if isinstance(name, str) and name:
                return name
    return ""


def _extract_links(inner: Dict[str, Any]) -> Tuple[Optional[str], Optional[str]]:
    """Split HF links into ``(code_url, project_url)``.

    ``code_url`` is the GitHub repo (or a GitHub ``projectPage`` as fallback
    when no repo is listed). ``project_url`` is a NON-GitHub ``projectPage``
    — typically the paper's demo / website (e.g. ``robotics.xiaomi.com/...``,
    ``aka.ms/...``). HF items often carry BOTH a repo and a separate demo
    page; previously the demo page was dropped whenever a repo was present
    or whenever the projectPage wasn't a GitHub URL.
    """
    repo = inner.get("githubRepo")
    project = inner.get("projectPage")
    repo_ok = isinstance(repo, str) and bool(repo) and _is_github_url(repo)
    project_ok = isinstance(project, str) and bool(project)

    code_url: Optional[str] = None
    if repo_ok:
        code_url = repo
    elif project_ok and _is_github_url(project):
        code_url = project

    project_url: Optional[str] = None
    if project_ok and not _is_github_url(project):
        project_url = project

    return code_url, project_url


def _to_int(value: Any) -> Optional[int]:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _parse_date(date_str: str) -> Optional[datetime.date]:
    """Parse ``YYYY-MM-DD`` → ``date``; ``None`` if malformed (non-fatal)."""
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None
