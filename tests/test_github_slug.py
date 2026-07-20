"""Tests for the GitHub-style heading anchor slug (``github_slug``)."""

from src.daily_arxiv.utils.date_utils import github_slug


def test_slug_required_examples():
    """The three spec-mandated examples must match exactly (double hyphens)."""
    assert github_slug("World Models & Generative Video") == "world-models--generative-video"
    assert (
        github_slug("Vision-Language & Action Models (VLA/VLM)")
        == "vision-language--action-models-vlavlm"
    )
    assert (
        github_slug("3D Understanding: Reconstruction & Generation")
        == "3d-understanding-reconstruction--generation"
    )


def test_slug_strips_leading_trailing_whitespace():
    assert github_slug("  Hello World  ") == "hello-world"


def test_slug_lowercases():
    assert github_slug("CamelCaseTitle") == "camelcasetitle"


def test_slug_ampersand_yields_double_hyphen():
    # The & is removed (not replaced), leaving two adjacent spaces -> two hyphens.
    assert github_slug("A & B") == "a--b"


def test_slug_keeps_existing_hyphens():
    assert github_slug("Already-Hyphenated") == "already-hyphenated"


def test_slug_keeps_alphanumeric_including_digits():
    assert github_slug("3D Vision") == "3d-vision"


def test_slug_empty_string():
    assert github_slug("") == ""


def test_slug_punctuation_only_collapses_to_empty():
    assert github_slug("!!!") == ""


def test_slug_strips_leading_trailing_hyphens():
    # Leading/trailing punctuation is removed then the leftover edge hyphens stripped.
    assert github_slug("& Foo &") == "foo"


def test_slug_never_emits_literal_backslash_n():
    result = github_slug("Some & Category")
    assert "\\n" not in result
    assert result == "some--category"
