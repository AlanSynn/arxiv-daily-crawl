"""Test refactored functionality for daily-arxiv."""

import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

from src.daily_arxiv.core.config import load_config, validate_config
from src.daily_arxiv.services.arxiv_client import ArXivClient
from src.daily_arxiv.services.github_client import GitHubClient
from src.daily_arxiv.services.email_service import EmailService
from src.daily_arxiv.processors.file_manager import FileManager
from src.daily_arxiv.processors.content_generator import ContentGenerator
from src.daily_arxiv.utils.file_utils import ensure_directory_exists
from src.daily_arxiv.utils.date_utils import format_authors, get_dated_file_paths


def test_config_validation():
    """Test configuration validation."""
    # Valid config
    valid_config = {
        'base_url': 'https://test.com',
        'keywords': {'Test': {'filters': ['test']}},
        'max_results': 10
    }
    assert validate_config(valid_config) is True
    
    # Invalid config - missing required key
    invalid_config = {
        'base_url': 'https://test.com'
    }
    assert validate_config(invalid_config) is False


def test_arxiv_client_initialization():
    """Test ArXiv client can be initialized."""
    client = ArXivClient()
    assert client is not None
    assert hasattr(client, 'get_daily_papers')


def test_github_client_initialization():
    """Test GitHub client can be initialized."""
    client = GitHubClient()
    assert client is not None
    assert hasattr(client, 'get_code_link')


def test_email_service_initialization():
    """Test email service can be initialized."""
    config = {'email_settings': {'enabled': True}}
    service = EmailService(config)
    assert service is not None
    assert hasattr(service, 'send_email')


def test_file_manager_initialization():
    """Test file manager can be initialized."""
    manager = FileManager()
    assert manager is not None
    assert hasattr(manager, 'update_json_file')


def test_content_generator_initialization():
    """Test content generator can be initialized."""
    generator = ContentGenerator()
    assert generator is not None
    assert hasattr(generator, 'json_to_md')


def test_format_authors():
    """Test author formatting utility."""
    # Mock author objects with proper __str__ implementation
    class MockAuthor:
        def __init__(self, name):
            self.name = name
        def __str__(self):
            return self.name
    
    authors = [MockAuthor('John Doe'), MockAuthor('Jane Smith')]
    
    # Test full author list
    result = format_authors(authors)
    assert 'John Doe' in result
    assert 'Jane Smith' in result
    
    # Test first author only
    result = format_authors(authors, first_author=True)
    assert result == 'John Doe'
    
    # Test empty list
    result = format_authors([])
    assert result == ""


def test_file_utils():
    """Test file utility functions."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_dir = os.path.join(tmpdir, 'test_subdir')
        ensure_directory_exists(test_dir)
        assert os.path.exists(test_dir)


def test_dated_file_paths():
    """Test dated file path generation."""
    config = {'log_dir': './logs'}
    
    with patch('src.daily_arxiv.utils.date_utils.datetime') as mock_datetime:
        mock_datetime.date.today().strftime.return_value = '2024-01-15'
        
        paths = get_dated_file_paths(config, '2024-01-15')
        
        assert isinstance(paths, dict)
        assert '2024-01-15' in str(paths)


@patch('src.daily_arxiv.services.github_client.requests.get')
def test_github_client_get_code_link(mock_get):
    """Test GitHub client code link fetching."""
    # Mock successful response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        'total_count': 1,
        'items': [{'html_url': 'https://github.com/test/repo'}]
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    
    client = GitHubClient()
    result = client.get_code_link('test query')
    
    assert result == 'https://github.com/test/repo'


@patch('src.daily_arxiv.services.github_client.requests.get')
def test_github_client_no_results(mock_get):
    """Test GitHub client with no results."""
    # Mock empty response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        'total_count': 0,
        'items': []
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    
    client = GitHubClient()
    result = client.get_code_link('nonexistent query')
    
    assert result is None


def test_file_manager_json_operations():
    """Test file manager JSON operations."""
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = FileManager()
        json_file = os.path.join(tmpdir, 'test.json')
        
        test_data = [{'Test Category': {'paper1': 'content1'}}]
        
        # Test creating new file
        result = manager.update_json_file(json_file, test_data, create_new=True)
        
        assert os.path.exists(json_file)
        assert 'Test Category' in result
        assert result['Test Category']['paper1'] == 'content1'


def test_email_service_content_generation():
    """Test email service content generation."""
    config = {'email_settings': {'enabled': True}}
    service = EmailService(config)
    
    test_data = {
        'Test Category': {
            'paper1': 'Test paper content'
        }
    }
    
    html_content = service.generate_daily_email_content(test_data, '2024-01-15')
    
    assert html_content is not None
    assert 'Test Category' in html_content
    assert '2024-01-15' in html_content
    assert '<html lang="en">' in html_content


def test_cli_integration():
    """Test that CLI components can be imported and used together."""
    from src.daily_arxiv.cli.main import DailyArxivApp
    
    # Mock config
    config = {
        'base_url': 'https://test.com',
        'kv': {'Test': 'test query'},
        'max_results': 5,
        'email_settings': {'enabled': False}
    }
    
    # Test app initialization
    app = DailyArxivApp(config)
    assert app is not None
    assert hasattr(app, 'run')
    assert app.config == config