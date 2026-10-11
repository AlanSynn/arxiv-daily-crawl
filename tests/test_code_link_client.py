"""Tests for the Hugging Face Papers code-link client."""

from unittest.mock import patch, MagicMock

from src.arxiv_digest.services.code_link_client import CodeLinkClient, _is_github_url


def test_disabled_returns_none_without_network():
    client = CodeLinkClient(enabled=False)
    with patch("src.arxiv_digest.services.code_link_client.requests.get") as mock_get:
        assert client.get_code_url("2506.14513") is None
        mock_get.assert_not_called()


def test_github_project_page_returned():
    client = CodeLinkClient(enabled=True, delay_seconds=0)
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "id": "2106.09685",
        "projectPage": "https://github.com/microsoft/LoRA",
    }
    with patch(
        "src.arxiv_digest.services.code_link_client.requests.get",
        return_value=mock_resp,
    ):
        assert client.get_code_url("2106.09685") == "https://github.com/microsoft/LoRA"


def test_non_github_project_page_returns_none():
    client = CodeLinkClient(enabled=True, delay_seconds=0)
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {
        "projectPage": "https://openai.com/index/gpt-4-research/",
    }
    with patch(
        "src.arxiv_digest.services.code_link_client.requests.get",
        return_value=mock_resp,
    ):
        assert client.get_code_url("2303.08774") is None


def test_missing_project_page_returns_none():
    client = CodeLinkClient(enabled=True, delay_seconds=0)
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"id": "1706.03762"}  # no projectPage field
    with patch(
        "src.arxiv_digest.services.code_link_client.requests.get",
        return_value=mock_resp,
    ):
        assert client.get_code_url("1706.03762") is None


def test_404_returns_none():
    client = CodeLinkClient(enabled=True, delay_seconds=0)
    mock_resp = MagicMock()
    mock_resp.status_code = 404
    with patch(
        "src.arxiv_digest.services.code_link_client.requests.get",
        return_value=mock_resp,
    ):
        assert client.get_code_url("0000.00000") is None


def test_network_error_returns_none():
    client = CodeLinkClient(enabled=True, delay_seconds=0)
    import requests
    with patch(
        "src.arxiv_digest.services.code_link_client.requests.get",
        side_effect=requests.RequestException("boom"),
    ):
        assert client.get_code_url("2506.14513") is None


def test_cache_avoids_duplicate_calls():
    client = CodeLinkClient(enabled=True, delay_seconds=0)
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {"projectPage": "https://github.com/x/y"}
    with patch(
        "src.arxiv_digest.services.code_link_client.requests.get",
        return_value=mock_resp,
    ) as mock_get:
        first = client.get_code_url("2106.09685")
        second = client.get_code_url("2106.09685")
        assert first == "https://github.com/x/y"
        assert second == "https://github.com/x/y"
        # Only one network call despite two lookups.
        assert mock_get.call_count == 1


def test_cache_stores_negative_result():
    client = CodeLinkClient(enabled=True, delay_seconds=0)
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = {}  # no projectPage -> None
    with patch(
        "src.arxiv_digest.services.code_link_client.requests.get",
        return_value=mock_resp,
    ) as mock_get:
        assert client.get_code_url("1706.03762") is None
        assert client.get_code_url("1706.03762") is None  # cached None
        assert mock_get.call_count == 1


def test_is_github_url_helper():
    assert _is_github_url("https://github.com/org/repo")
    assert _is_github_url("https://www.github.com/org/repo")
    assert not _is_github_url("https://anthropics.github.io/demo/")
    assert not _is_github_url("https://huggingface.co/spaces/x/y")
    assert not _is_github_url("not a url")
