"""Test daily paper filtering functionality for cv-arxiv-daily."""

import pytest
from datetime import date, timedelta
from unittest.mock import patch, MagicMock
from src.daily_arxiv.services.arxiv_client import ArXivClient


class MockArxivResult:
    """Mock ArXiv result object for testing."""

    def __init__(self, paper_id, title, authors, published_date, updated_date, abstract="Test abstract"):
        self.paper_id = paper_id
        self.title = title
        self.authors = [MockAuthor(author) for author in authors]
        self.published = MockDate(published_date)
        self.updated = MockDate(updated_date)
        self.summary = abstract
        self.entry_id = f"http://arxiv.org/abs/{paper_id}"
        self.comment = None

    def get_short_id(self):
        return self.paper_id


class MockAuthor:
    """Mock author object for testing."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class MockDate:
    """Mock date object for testing."""

    def __init__(self, date_obj):
        self._date = date_obj

    def date(self):
        return self._date


class MockSearchResults:
    """Mock ArXiv search results."""

    def __init__(self, results):
        self._results = results

    def results(self):
        return iter(self._results)


@pytest.fixture
def client():
    """Create ArXivClient instance for testing."""
    return ArXivClient()


@pytest.fixture
def mixed_date_papers():
    """Sample papers with different dates for testing filtering."""
    today = date.today()
    yesterday = today - timedelta(days=1)
    two_days_ago = today - timedelta(days=2)

    return [
        MockArxivResult("2024.01001", "Today's Paper", ["John Doe"], today, today),
        MockArxivResult("2024.01002", "Another Today's Paper", ["Jane Smith"], today, today),
        MockArxivResult("2024.01003", "Yesterday's Paper", ["Bob Wilson"], yesterday, yesterday),
        MockArxivResult("2024.01004", "Two Days Ago Paper", ["Alice Brown"], two_days_ago, two_days_ago),
    ]


@pytest.fixture
def same_date_papers():
    """Sample papers all from the same date."""
    test_date = date(2025, 6, 23)

    return [
        MockArxivResult("2024.02001", "Paper One", ["Author One"], test_date, test_date),
        MockArxivResult("2024.02002", "Paper Two", ["Author Two"], test_date, test_date),
        MockArxivResult("2024.02003", "Paper Three", ["Author Three"], test_date, test_date),
    ]


def test_daily_filtering_with_mixed_dates(client, mixed_date_papers):
    """Test that only most recent day papers are included in email data."""

    # Mock the arxiv search
    mock_search = MockSearchResults(mixed_date_papers)

    with patch('arxiv.Search') as mock_arxiv_search:
        mock_arxiv_search.return_value = mock_search

        # Mock requests for code URL (return None for simplicity)
        with patch('requests.get') as mock_requests:
            mock_requests.return_value.json.return_value = {}

            email_data, email_web, main_data, main_web = client.get_daily_papers(
                "Test Topic", "test query", 10
            )

            # Check that main data contains all papers
            assert len(main_data["Test Topic"]) == 4

            # Check that email data contains only today's papers (most recent date)
            assert len(email_data["Test Topic"]) == 2

            # Verify the content contains today's papers
            email_content = list(email_data["Test Topic"].values())
            assert any("Today's Paper" in content for content in email_content)
            assert any("Another Today's Paper" in content for content in email_content)

            # Verify yesterday's and older papers are not in email
            assert not any("Yesterday's Paper" in content for content in email_content)
            assert not any("Two Days Ago Paper" in content for content in email_content)


def test_daily_filtering_with_same_dates(client, same_date_papers):
    """Test behavior when all papers are from the same date."""

    mock_search = MockSearchResults(same_date_papers)

    with patch('arxiv.Search') as mock_arxiv_search:
        mock_arxiv_search.return_value = mock_search

        with patch('requests.get') as mock_requests:
            mock_requests.return_value.json.return_value = {}

            email_data, email_web, main_data, main_web = client.get_daily_papers(
                "Test Topic", "test query", 10
            )

            # When all papers are from same date, email and main should be identical
            assert len(main_data["Test Topic"]) == 3
            assert len(email_data["Test Topic"]) == 3

            # Check that all papers are included in both
            main_titles = [content for content in main_data["Test Topic"].values()]
            email_titles = [content for content in email_data["Test Topic"].values()]

            assert len(main_titles) == len(email_titles)


def test_daily_filtering_with_no_papers(client):
    """Test behavior when no papers are found."""

    mock_search = MockSearchResults([])

    with patch('arxiv.Search') as mock_arxiv_search:
        mock_arxiv_search.return_value = mock_search

        email_data, email_web, main_data, main_web = client.get_daily_papers(
            "Test Topic", "test query", 10
        )

        # Both should be empty
        assert len(main_data["Test Topic"]) == 0
        assert len(email_data["Test Topic"]) == 0


def test_most_recent_date_identification(client, mixed_date_papers):
    """Test that the most recent date is correctly identified."""

    mock_search = MockSearchResults(mixed_date_papers)

    with patch('arxiv.Search') as mock_arxiv_search:
        mock_arxiv_search.return_value = mock_search

        with patch('requests.get') as mock_requests:
            mock_requests.return_value.json.return_value = {}

            # Capture the log output to verify most recent date detection
            with patch('logging.info') as mock_log:
                email_data, email_web, main_data, main_web = client.get_daily_papers(
                    "Test Topic", "test query", 10
                )

                # Check that logging was called with most recent date info
                log_calls = [call[0][0] for call in mock_log.call_args_list]
                most_recent_log = [log for log in log_calls if "Most recent paper date" in log]
                assert len(most_recent_log) > 0

                # Verify today's date is in the log
                today_str = str(date.today())
                assert any(today_str in log for log in most_recent_log)


def test_paper_content_format(client, same_date_papers):
    """Test that paper content is properly formatted."""

    mock_search = MockSearchResults(same_date_papers)

    with patch('arxiv.Search') as mock_arxiv_search:
        mock_arxiv_search.return_value = mock_search

        with patch('requests.get') as mock_requests:
            mock_requests.return_value.json.return_value = {}

            email_data, email_web, main_data, main_web = client.get_daily_papers(
                "Test Topic", "test query", 10
            )

            # Check format of first paper content
            first_paper = list(main_data["Test Topic"].values())[0]

            # Should be in markdown table format: |date|title|authors|link|code|
            assert first_paper.startswith("|**2025-06-23**|")
            assert "Paper One" in first_paper
            assert "Author One" in first_paper
            assert "2024.02001" in first_paper
            assert first_paper.endswith("|null|\\n")


def test_web_content_format(client, same_date_papers):
    """Test that web content is properly formatted."""

    mock_search = MockSearchResults(same_date_papers)

    with patch('arxiv.Search') as mock_arxiv_search:
        mock_arxiv_search.return_value = mock_search

        with patch('requests.get') as mock_requests:
            mock_requests.return_value.json.return_value = {}

            email_data, email_web, main_data, main_web = client.get_daily_papers(
                "Test Topic", "test query", 10
            )

            # Check format of first paper web content
            first_paper_web = list(main_web["Test Topic"].values())[0]

            # Should be in list format with abstract
            assert first_paper_web.startswith("- 2025-06-23, **Paper One**")
            assert "Author One" in first_paper_web
            assert "Abstract:" in first_paper_web
            assert "Test abstract" in first_paper_web


def test_code_url_integration(client, same_date_papers):
    """Test integration with code URL fetching."""

    mock_search = MockSearchResults(same_date_papers)

    with patch('arxiv.Search') as mock_arxiv_search:
        mock_arxiv_search.return_value = mock_search

        # Mock successful code URL response
        with patch('requests.get') as mock_requests:
            mock_response = MagicMock()
            mock_response.json.return_value = {
                "official": {"url": "https://github.com/test/repo"}
            }
            mock_requests.return_value = mock_response

            email_data, email_web, main_data, main_web = client.get_daily_papers(
                "Test Topic", "test query", 10
            )

            # Check that code link is included
            first_paper = list(main_data["Test Topic"].values())[0]
            assert "**[link](https://github.com/test/repo)**" in first_paper


@pytest.mark.integration
def test_cli_integration_with_filtering():
    """Integration test for CLI with new filtering functionality."""
    from src.daily_arxiv.cli.main import DailyArxivApp

    # Mock config
    config = {
        'base_url': 'https://test.com',
        'kv': {'Test Category': 'test query'},
        'max_results': 5,
        'email_settings': {'enabled': False},
        'send_email': False,
        'json_readme_path': '/tmp/test.json',
        'json_gitpage_path': '/tmp/test_web.json',
        'md_readme_path': '/tmp/test.md',
        'md_gitpage_path': '/tmp/test_web.md',
        'log_dir': '/tmp/logs'
    }

    # Test that app can be created and has the right components
    app = DailyArxivApp(config)
    assert hasattr(app, 'arxiv_client')
    assert hasattr(app, 'file_manager')
    assert hasattr(app, 'content_generator')

    # Test that arxiv_client has the new method signature
    import inspect
    sig = inspect.signature(app.arxiv_client.get_daily_papers)
    # Should return 4 values now (email_data, email_web, main_data, main_web)
    assert 'topic' in sig.parameters
    assert 'query' in sig.parameters
    assert 'max_results' in sig.parameters