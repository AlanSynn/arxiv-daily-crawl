"""Cross-run notification dedup state for the daily Dispatch email.

Problem this solves
-------------------
The email slice is "papers published on the single newest day"
(:func:`~daily_arxiv.services.arxiv_client.filter_recent_day`).  arXiv posts
new submissions on weekdays only, so over a weekend the "newest day" stalls
and the *same* papers sit in the slice for 3 consecutive daily runs — each
run re-emails them.  Without persistent state the runner cannot tell "already
sent" from "genuinely new".

This module is the state half of the fix: a small JSON set of paper keys that
have already been dispatched.  The runner loads it, drops already-notified
keys from the slice, sends the remainder, then records the freshly-sent keys.
Net effect: every paper is emailed **at most once**.

State file shape (round-trip stable, forward/backward compatible)::

    {"notified": ["2506.14513", "2506.14000", ...], "count": 27}

Both the legacy bare-list ``["2506.14513", ...]`` and a ``{key: ...}`` dict
are accepted on load so a hand-edited or older file never breaks the run.

Pruning
-------
Keys are arXiv ids ``YYMM.NNNNN`` (or legacy ``archive/YYMMnnnn``); the first
four digits encode year/month.  Papers older than the fetch window (14 days)
can never re-enter the slice, so we prune keys older than ``max_age_days`` to
bound the file's growth.  Pruning is conservative: unparseable keys are kept,
and the cutoff is rounded to whole months so a current-month paper is never
dropped early.
"""

from __future__ import annotations

import datetime
import json
import logging
import math
import os
from typing import Iterable, Optional, Set, Tuple


def _key_year_month(key: str) -> Optional[Tuple[int, int]]:
    """Extract ``(year, month)`` from an arXiv id, or ``None`` if unparseable.

    Handles modern ``YYMM.NNNNN`` (e.g. ``2506.14513`` -> ``(2025, 6)``) and
    legacy ``archive/YYMMnnnn`` ids.  Two-digit years ``< 70`` are 20xx.
    """
    # Take the segment after any '/' (legacy archive prefix) and before '.'.
    head = str(key).split("/")[-1].split(".")[0]
    if len(head) < 4 or not head[:4].isdigit():
        return None
    yy = int(head[:2])
    mm = int(head[2:4])
    if not (1 <= mm <= 12):
        return None
    year = 2000 + yy if yy < 70 else 1900 + yy
    return year, mm


def _month_ordinal(year: int, month: int) -> int:
    """Total-months integer (year*12 + month) for monotonic comparison."""
    return year * 12 + month


def prune_old(
    keys: Iterable[str],
    max_age_days: int = 30,
    today: Optional[datetime.date] = None,
) -> Set[str]:
    """Drop notified keys older than ``max_age_days``.

    Conservative by design: the cutoff is rounded *up* to whole months
    (``ceil(max_age_days / 30)``, minimum 1) so a paper published this month
    is never pruned while it could still be in the fetch window.  Keys whose
    year/month cannot be parsed are kept (never silently lost).
    """
    today = today or datetime.date.today()
    keep_months = max(1, math.ceil(max(max_age_days, 1) / 30))
    cutoff = _month_ordinal(today.year, today.month) - keep_months

    kept: Set[str] = set()
    for key in keys:
        ym = _key_year_month(key)
        # Unparseable -> keep (do not silently drop unknown key shapes).
        if ym is None or _month_ordinal(*ym) >= cutoff:
            kept.add(key)
    return kept


def load_notified(path: str) -> Set[str]:
    """Load the set of already-dispatched paper keys from ``path``.

    Returns an empty set if the file is missing, empty, or corrupt — a
    missing state file just means "nothing notified yet" (first run after
    deploy, or state evicted), which is always a safe default.
    """
    try:
        with open(path, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return set()

    if isinstance(data, dict):
        # Preferred shape: {"notified": [...]}. If the key is present but the
        # value is not a list (corrupt), start fresh rather than mis-reading
        # the wrapper keys ("notified"/"count") as paper ids.
        if "notified" in data:
            inner = data["notified"]
            return {str(k) for k in inner} if isinstance(inner, list) else set()
        # Legacy/alt shape: {key: anything}.
        return {str(k) for k in data.keys()}
    if isinstance(data, list):
        return {str(k) for k in data}
    return set()


def save_notified(
    path: str,
    keys: Iterable[str],
    max_age_days: int = 30,
    today: Optional[datetime.date] = None,
) -> Set[str]:
    """Prune + persist the notified-key set to ``path``.

    Returns the pruned set actually written.  ``today`` is injectable for
    deterministic tests; in production it defaults to the real current date.
    Writes are atomic-ish (single ``json.dump``); the file is small (bounded
    by pruning) so partial-write risk is negligible, and
    :func:`load_notified` tolerates a truncated file.
    """
    pruned = prune_old(set(keys), max_age_days=max_age_days, today=today)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    payload = sorted(pruned)
    # Atomic write: dump to a sibling temp file then os.replace into place
    # so a killed runner / full disk can't leave a truncated state file.
    tmp = f"{path}.tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump({"notified": payload, "count": len(payload)}, fh, indent=2)
    os.replace(tmp, path)
    logging.info(
        "Notified state saved: %d keys (pruned to last %d days) -> %s",
        len(pruned), max_age_days, path,
    )
    return pruned
