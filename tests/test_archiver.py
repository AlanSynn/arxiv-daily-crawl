"""Tests for the archiver's dual-format (pipe + web row) handling (Fix C)."""

import json
import os
import tempfile
from datetime import date, timedelta

from src.daily_arxiv.archive.archiver import archive_old_papers, parse_paper_entry


PIPE_ROW = (
    "|**2025-06-17**|**Title**|Author et.al.|"
    "[@2506.001](http://arxiv.org/abs/2506.001)|null|\n"
)
WEB_ROW = (
    "- 2025-06-17, **Title**, Author et.al., "
    "Paper: [@2506.001](http://arxiv.org/abs/2506.001)\n"
    "> **Abstract:** the abstract text\n"
)
WEB_ROW_WITH_CODE = (
    "- 2025-06-17, **Title**, Author et.al., "
    "Paper: [@2506.002](http://arxiv.org/abs/2506.002), "
    "Code: **[link](https://github.com/x/y)**\n"
    "> **Abstract:** another abstract\n"
)


# ---------------------------------------------------------------------------
# parse_paper_entry
# ---------------------------------------------------------------------------
def test_parse_pipe_row_still_works():
    parsed = parse_paper_entry(PIPE_ROW)
    assert parsed is not None
    assert parsed["date"] == date(2025, 6, 17)
    assert parsed["id"] == "@2506.001"  # existing behavior: keeps the '@'
    assert parsed["entry"] == PIPE_ROW


def test_parse_web_row_returns_date_and_key():
    parsed = parse_paper_entry(WEB_ROW)
    assert parsed is not None
    assert parsed["date"] == date(2025, 6, 17)
    assert parsed["id"] == "2506.001"  # prefix-stripped arxiv id, no '@'
    # The full original row is preserved verbatim for JSON rewrite.
    assert parsed["entry"] == WEB_ROW


def test_parse_web_row_with_code_link():
    parsed = parse_paper_entry(WEB_ROW_WITH_CODE)
    assert parsed is not None
    assert parsed["date"] == date(2025, 6, 17)
    assert parsed["id"] == "2506.002"
    assert parsed["entry"] == WEB_ROW_WITH_CODE


def test_parse_garbage_returns_none():
    assert parse_paper_entry("not a paper entry at all") is None
    assert parse_paper_entry("") is None


# ---------------------------------------------------------------------------
# archive_old_papers round-trip (web rows participate in pruning)
# ---------------------------------------------------------------------------
def _web_row(key, title, day):
    return (
        f"- {day.isoformat()}, **{title}**, Author et.al., "
        f"Paper: [@{key}](http://arxiv.org/abs/{key})\n"
        f"> **Abstract:** abstract for {title}\n"
    )


def test_archive_prunes_old_web_rows_and_keeps_recent():
    today = date.today()
    old_date = today - timedelta(days=400)   # older than the 365-day cutoff
    recent_date = today - timedelta(days=10)  # within the cutoff

    data = {
        "Motion": {
            "2400.001": _web_row("2400.001", "Old Paper", old_date),
            "2506.001": _web_row("2506.001", "Recent Paper", recent_date),
        }
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        json_file = os.path.join(tmpdir, "web.json")
        with open(json_file, "w") as f:
            json.dump(data, f)

        archive_dir = os.path.join(tmpdir, "archive")
        archive_old_papers(json_file, archive_dir, max_age_days=365)

        # Pruned main JSON keeps only the recent row.
        with open(json_file) as f:
            remaining = json.load(f)
        assert "2400.001" not in remaining["Motion"]   # old -> pruned
        assert "2506.001" in remaining["Motion"]        # recent -> kept
        # The kept row is preserved verbatim (not rebuilt from fields).
        assert remaining["Motion"]["2506.001"] == data["Motion"]["2506.001"]

        # The archive markdown was generated without crashing and contains the
        # archived (old) row verbatim, including its abstract.
        archive_md = os.path.join(
            archive_dir, f"archive_{today.strftime('%Y%m')}.md"
        )
        assert os.path.exists(archive_md)
        with open(archive_md) as f:
            md_text = f.read()
        assert "Old Paper" in md_text
        assert "> **Abstract:** abstract for Old Paper" in md_text
        assert "Recent Paper" not in md_text
