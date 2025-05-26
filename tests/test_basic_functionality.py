"""Basic functionality tests that verify core operations work"""

import pytest
import tempfile
import os
from pathlib import Path

from src.daily_arxiv.core.config import load_config
from src.daily_arxiv.utils.file_utils import ensure_directory_exists


def test_ensure_directory_creation():
    """Test that directories can be created successfully"""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_dir = os.path.join(tmpdir, 'test_subdir')
        
        ensure_directory_exists(test_dir)
        
        assert os.path.exists(test_dir)
        assert os.path.isdir(test_dir)


def test_config_loading_basic():
    """Test basic configuration loading works"""
    with tempfile.TemporaryDirectory() as tmpdir:
        config_file = os.path.join(tmpdir, 'test_config.yaml')
        
        config_content = """
base_url: "https://arxiv.paperswithcode.com/api/v0/papers/"
max_results: 10
keywords:
  Test:
    filters:
      - "test filter"
"""
        
        with open(config_file, 'w') as f:
            f.write(config_content)
        
        config = load_config(config_file)
        
        assert config is not None
        assert config['base_url'] == "https://arxiv.paperswithcode.com/api/v0/papers/"
        assert config['max_results'] == 10
        assert 'keywords' in config


def test_project_structure():
    """Test that the project structure is correct"""
    project_root = Path(__file__).parent.parent
    
    # Check that key files exist
    assert (project_root / 'pyproject.toml').exists()
    assert (project_root / 'config.yaml').exists()
    assert (project_root / 'src' / 'daily_arxiv' / 'cli' / 'main.py').exists()
    assert (project_root / 'src' / 'daily_arxiv' / 'core' / 'config.py').exists()
    assert (project_root / 'src' / 'daily_arxiv' / 'services').exists()
    
    # Check that scripts folder exists
    assert (project_root / 'scripts').exists()


def test_import_works():
    """Test that the main modules can be imported"""
    try:
        from src.daily_arxiv.core.config import load_config
        from src.daily_arxiv.services.arxiv_client import ArXivClient
        from src.daily_arxiv.services.email_service import EmailService
        from src.daily_arxiv.cli.main import main
        
        # Test that main functions are callable
        assert callable(load_config)
        assert callable(main)
        assert ArXivClient is not None
        assert EmailService is not None
    except ImportError as e:
        pytest.fail(f"Failed to import refactored modules: {e}")


def test_dependencies_installed():
    """Test that required dependencies are available"""
    try:
        import arxiv
        import yaml
        import requests
        import smtplib
    except ImportError as e:
        pytest.fail(f"Required dependency not available: {e}")