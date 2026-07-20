"""Tests for TOC + flat paper-list generation (output layer, Wave 2)."""

from datetime import date

from src.daily_arxiv.models.paper import Paper
from src.daily_arxiv.processors.content_generator import ContentGenerator
from src.daily_arxiv.processors.toc_generator import (
    generate_paper_list,
    generate_toc,
)


def _paper(key, title, category, score, published, code_url=None):
    return Paper(
        paper_key=key,
        title=title,
        authors_str="Author",
        abstract="abstract",
        published=published,
        updated=published,
        primary_category="cs.GR",
        all_categories=["cs.GR"],
        entry_id=f"http://arxiv.org/abs/{key}",
        abs_url=f"http://arxiv.org/abs/{key}",
        category=category,
        score=score,
        code_url=code_url,
    )


# ---------------------------------------------------------------------------
# generate_toc
# ---------------------------------------------------------------------------
def test_toc_structure_and_anchors():
    cat_a = "World Models & Generative Video"
    cat_b = "Vision-Language & Action Models (VLA/VLM)"
    papers_a = [_paper("2506.001", "T1", cat_a, 0.5, date(2025, 6, 17))]
    papers_b = [
        _paper("2506.002", "T2", cat_b, 0.7, date(2025, 6, 17)),
        _paper("2506.003", "T3", cat_b, 0.4, date(2025, 6, 17)),
    ]

    out = generate_toc([(cat_a, papers_a), (cat_b, papers_b)], date(2025, 6, 17))

    # Pretty-date header.
    assert "## 📚 Updated on 2025.06.17" in out
    # ISO date in the summary.
    assert "📑 Table of Contents — 2025-06-17" in out
    # Anchors match GitHub slug + paper counts.
    assert "(#world-models--generative-video) (1)" in out
    assert "(#vision-language--action-models-vlavlm) (2)" in out
    # Real newlines, never literal backslash-n.
    assert b"\n" in out.encode()
    assert "\\n" not in out


def test_toc_skips_empty_categories():
    out = generate_toc(
        [("Empty", []), ("Full", [_paper("k", "t", "Full", 0.5, date(2025, 1, 1))])],
        date(2025, 1, 1),
    )
    assert "Empty" not in out
    assert "Full" in out
    assert "(#full) (1)" in out


def test_toc_has_details_open_block():
    out = generate_toc(
        [("Cat", [_paper("k", "t", "Cat", 0.5, date(2025, 1, 1))])],
        date(2025, 1, 1),
    )
    assert "<details open>" in out
    assert "</details>" in out
    assert "**By category**" in out


# ---------------------------------------------------------------------------
# generate_paper_list
# ---------------------------------------------------------------------------
def test_paper_list_dedup_keeps_highest_score():
    # Same paper_key appearing twice (matched two categories) -> highest score wins.
    dup_a = _paper("2506.001", "Title", "Cat A", 0.30, date(2025, 6, 17))
    dup_b = _paper("2506.001", "Title", "Cat B", 0.80, date(2025, 6, 17))

    out = generate_paper_list([dup_a, dup_b])

    # Only one data row (the paper_key appears twice within that single row:
    # once in [@key] and once in the abs_url, so count rows not substrings).
    data_rows = [line for line in out.splitlines() if "[@" in line]
    assert len(data_rows) == 1
    # The kept row shows the higher score + its best category.
    assert "0.80" in data_rows[0]
    assert "Cat B" in data_rows[0]
    assert "0.30" not in out


def test_paper_list_sort_newest_first():
    older = _paper("2506.001", "Older", "Cat", 0.5, date(2025, 6, 10))
    newer = _paper("2506.002", "Newer", "Cat", 0.5, date(2025, 6, 17))

    out = generate_paper_list([older, newer])

    newer_idx = out.index("2506.002")
    older_idx = out.index("2506.001")
    assert newer_idx < older_idx  # newer appears first


def test_paper_list_sort_score_tiebreak_on_same_date():
    same_day_a = _paper("2506.001", "Lower", "Cat", 0.40, date(2025, 6, 17))
    same_day_b = _paper("2506.002", "Higher", "Cat", 0.90, date(2025, 6, 17))

    out = generate_paper_list([same_day_a, same_day_b])

    # Higher score first when dates tie.
    assert out.index("2506.002") < out.index("2506.001")


def test_paper_list_score_two_decimals():
    p = _paper("2506.001", "T", "Cat", 0.83333, date(2025, 6, 17))
    out = generate_paper_list([p])
    assert "0.83" in out


def test_paper_list_date_is_isoformat():
    p = _paper("2506.001", "T", "Cat", 0.5, date(2025, 6, 17))
    out = generate_paper_list([p])
    assert "| 2025-06-17 |" in out


def test_paper_list_code_link_and_null():
    with_code = _paper(
        "2506.001", "WithCode", "Cat", 0.5, date(2025, 6, 17),
        code_url="https://github.com/x/y",
    )
    no_code = _paper("2506.002", "NoCode", "Cat", 0.5, date(2025, 6, 17))

    out = generate_paper_list([with_code, no_code])

    assert "[link](https://github.com/x/y)" in out
    # No-code -> "null" in the code column.
    assert "null" in out


def test_paper_list_real_newlines_byte_assertion():
    p = _paper("2506.001", "T", "Cat", 0.5, date(2025, 6, 17))
    out = generate_paper_list([p])
    assert b"\n" in out.encode()
    assert "\\n" not in out


def test_paper_list_has_header_and_separator():
    p = _paper("2506.001", "T", "Cat", 0.5, date(2025, 6, 17))
    out = generate_paper_list([p])
    assert "# 📄 Paper List" in out
    assert "| Date | Title | Category | Score | arXiv | Code |" in out
    assert "|---|---|---|---|---|---|" in out


# ---------------------------------------------------------------------------
# content_generator real-newline regression
# ---------------------------------------------------------------------------
def test_content_generator_emits_real_newlines():
    """The literal-``\\n`` join bug must stay fixed: output has real newlines."""
    cg = ContentGenerator()
    data = {
        "Some Category": {
            "2506.001": (
                "|**2025-06-17**|**Title**|Author et.al.|"
                "[@2506.001](http://arxiv.org/abs/2506.001)|null|\n"
            )
        }
    }
    md = cg._generate_markdown_content(
        data, "2025.06.17",
        to_web=False, use_title=False, use_tc=False,
        show_badge=False, use_b2t=False,
    )
    # Real newline bytes present...
    assert b"\n" in md.encode()
    # ...and never a literal backslash-n.
    assert "\\n" not in md


def test_content_generator_toc_block_replaces_default_header():
    """When toc_block is passed it is used verbatim (no duplicate header)."""
    cg = ContentGenerator()
    data = {"Cat": {"k": "|row|\n"}}
    toc_block = "## 📚 Updated on 2025.06.17\n\n<details open>\nstuff\n</details>"
    md = cg._generate_markdown_content(
        data, "2025.06.17",
        to_web=False, use_title=False, use_tc=True,
        show_badge=False, use_b2t=False, toc_block=toc_block,
    )
    assert toc_block in md
    # The fallback "Updated on" line is not also emitted.
    assert md.count("## 📚 Updated on") == 1


def test_content_generator_anchor_uses_github_slug():
    """The built-in TOC anchors must use github_slug (lowercased, correct hyphens)."""
    cg = ContentGenerator()
    data = {"World Models & Generative Video": {"k": "|row|\n"}}
    md = cg._generate_markdown_content(
        data, "2025.06.17",
        to_web=False, use_title=False, use_tc=True,
        show_badge=False, use_b2t=False,
    )
    assert "#world-models--generative-video" in md


def test_content_generator_web_section_no_pipe_header():
    """Web rows (to_web_row) render as bullets, NOT under a malformed pipe table."""
    cg = ContentGenerator()
    data = {
        "Some Category": {
            "2506.001": (
                "- 2025-06-17, **Title**, Author et.al., "
                "Paper: [@2506.001](http://arxiv.org/abs/2506.001)\n"
                "> **Abstract:** the abstract text\n"
            )
        }
    }
    md = cg._generate_markdown_content(
        data, "2025.06.17",
        to_web=True, use_title=False, use_tc=False,
        show_badge=False, use_b2t=False,
    )
    # No dangling pipe-table separator above the bullet rows.
    assert "|---|" not in md
    assert "|Publish Date|" not in md
    # The web row + abstract are present verbatim.
    assert "> **Abstract:** the abstract text" in md
    assert "- 2025-06-17, **Title**" in md
    # Real newlines, never literal backslash-n.
    assert b"\n" in md.encode()
    assert "\\n" not in md


def test_content_generator_readme_section_keeps_pipe_header():
    """Regression: readme rows (to_md_row) still get the pipe-table header."""
    cg = ContentGenerator()
    data = {
        "Some Category": {
            "2506.001": (
                "|**2025-06-17**|**Title**|Author et.al.|"
                "[@2506.001](http://arxiv.org/abs/2506.001)|null|\n"
            )
        }
    }
    md = cg._generate_markdown_content(
        data, "2025.06.17",
        to_web=False, use_title=False, use_tc=False,
        show_badge=False, use_b2t=False,
    )
    assert "|Publish Date|Title|Authors|arXiv|Code|" in md
    assert "|---|---|---|---|---|" in md


def test_content_generator_back_to_top_anchor_matches_heading():
    """Back-to-top anchor uses github_slug of the 'Updated on' heading (Fix G).

    GitHub drops the emoji and the dots in '2025.06.17', so the slug is
    'updated-on-20250617' -- a naive f'{date}' (dots kept) would be a dead link.
    """
    cg = ContentGenerator()
    data = {"Cat": {"k": "|**2025-06-17**|**T**|A et.al.|[@k](u)|null|\n"}}
    md = cg._generate_markdown_content(
        data, "2025.06.17",
        to_web=False, use_title=False, use_tc=False,
        show_badge=False, use_b2t=True,
    )
    assert "href=#updated-on-20250617" in md
    # The buggy literal '{date}' must be gone.
    assert "{date}" not in md
