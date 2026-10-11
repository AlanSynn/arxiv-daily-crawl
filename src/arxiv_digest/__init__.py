"""Personal curated arXiv digest: daily score-ranked paper recommendations by email."""

__version__ = "0.1.0"
__author__ = "Alan Synn"
__email__ = "alan@alansynn.com"

from .cli.main import main

__all__ = ["main"]