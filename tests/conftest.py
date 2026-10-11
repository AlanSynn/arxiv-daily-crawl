"""Test configuration and fixtures for arxiv-digest"""

import pytest
import tempfile
from pathlib import Path


@pytest.fixture
def sample_config():
    """Sample configuration data for testing"""
    return {
        'base_url': 'https://arxiv.paperswithcode.com/api/v0/papers/',
        'max_results': 5,
        'user_name': 'TestUser',
        'repo_name': 'test-repo',
        'email_settings': {
            'enabled': True,
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'smtp_user': 'test@example.com',
            'smtp_password': 'testpass'
        },
        'keywords': {
            'Test Category': {
                'filters': ['Test Filter']
            }
        }
    }


@pytest.fixture
def sample_arxiv_response():
    """Sample ArXiv API response for testing"""
    return {
        'papers': [
            {
                'id': '2024.01234',
                'title': 'Test Paper Title',
                'authors': [
                    {'name': 'John Doe'},
                    {'name': 'Jane Smith'}
                ],
                'abstract': 'This is a test abstract for a sample paper.',
                'published': '2024-01-15',
                'pdf_url': 'https://arxiv.org/pdf/2024.01234.pdf',
                'url': 'https://arxiv.org/abs/2024.01234'
            }
        ]
    }


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing file operations"""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def sample_paper_data():
    """Sample processed paper data for testing"""
    return {
        'Test Category': [
            {
                'id': '2024.01234',
                'title': 'Test Paper Title',
                'authors': 'John Doe, Jane Smith',
                'abstract': 'This is a test abstract.',
                'published': '2024-01-15',
                'pdf_url': 'https://arxiv.org/pdf/2024.01234.pdf',
                'url': 'https://arxiv.org/abs/2024.01234',
                'code_link': None
            }
        ]
    }