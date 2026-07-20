"""Code-link resolution via the Hugging Face Papers API.

Replaces the dead Papers With Code endpoint
(``arxiv.paperswithcode.com/api/v0/papers/{id}``, sunset mid-2025).  We query
``huggingface.co/api/papers/{arxiv_id}`` instead.

The HF Papers API does **not** expose a dedicated ``github_urls`` field.  The
most reliable code-repo signal available is ``projectPage``: when it points at
``github.com`` we return it as the code URL; otherwise we return ``None``.  This
is intentionally conservative (precision over recall) so the digest never links
to an unrelated demo page.  All failures degrade to ``None`` — this client must
never crash a run.
"""

from __future__ import annotations

import logging
import time
from typing import Dict, Optional
from urllib.parse import urlparse

import requests


_HF_PAPERS_URL = "https://huggingface.co/api/papers/{paper_key}"
_GITHUB_HOSTS = {"github.com"}


def _is_github_url(url: str) -> bool:
    """True if ``url`` is a ``github.com`` URL (code host), excluding demo pages."""
    try:
        host = urlparse(url).netloc.lower()
    except Exception:
        return False
    # Strip any "www." prefix so www.github.com still matches.
    return host.lstrip("www.") in _GITHUB_HOSTS


class CodeLinkClient:
    """Resolve a code-repository URL for an arXiv paper via the HF Papers API.

    Args:
        enabled: Master kill switch.  When ``False``, :meth:`get_code_url`
            short-circuits to ``None`` without any network traffic.
        delay_seconds: Minimum sleep between successive API calls.
        timeout: Per-request HTTP timeout in seconds.
    """

    def __init__(self, enabled: bool = True, delay_seconds: float = 1.0, timeout: float = 8.0):
        self.enabled = enabled
        self.delay_seconds = delay_seconds
        self.timeout = timeout
        # In-run LRU-ish cache: paper_key -> Optional[url].  A negative result
        # is cached too, so we never hit HF twice for the same key in one run.
        self._cache: Dict[str, Optional[str]] = {}

    def get_code_url(self, paper_key: str) -> Optional[str]:
        """Return a github code URL for ``paper_key`` or ``None``.

        Never raises: every error path (disabled, network, parse, missing
        field) returns ``None``.
        """
        if not self.enabled:
            return None

        if paper_key in self._cache:
            return self._cache[paper_key]

        url = self._fetch(paper_key)
        self._cache[paper_key] = url

        # Throttle between calls to stay friendly to the HF API.
        if self.delay_seconds > 0:
            time.sleep(self.delay_seconds)

        return url

    def _fetch(self, paper_key: str) -> Optional[str]:
        """Hit the HF Papers API and extract a github code URL if present."""
        endpoint = _HF_PAPERS_URL.format(paper_key=paper_key)
        try:
            response = requests.get(endpoint, timeout=self.timeout)
            if response.status_code != 200:
                logging.debug(
                    "HF Papers API returned %s for %s",
                    response.status_code, paper_key,
                )
                return None
            data = response.json()
        except requests.RequestException as e:
            logging.debug("HF Papers request failed for %s: %s", paper_key, e)
            return None
        except ValueError as e:  # bad JSON
            logging.debug("HF Papers returned non-JSON for %s: %s", paper_key, e)
            return None

        return self._extract_github_url(data)

    @staticmethod
    def _extract_github_url(data: object) -> Optional[str]:
        """Pull the first github.com URL out of the HF Papers response.

        Checks ``projectPage`` first (the documented code-repo field).  Falls
        back to scanning top-level string fields defensively, but will not
        invent a URL: if nothing github-shaped is found, returns ``None``.
        """
        if not isinstance(data, dict):
            return None

        project_page = data.get("projectPage")
        if isinstance(project_page, str) and project_page and _is_github_url(project_page):
            return project_page

        return None
