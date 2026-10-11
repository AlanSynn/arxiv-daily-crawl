"""Entry point for running arxiv-digest as a module."""

from .cli.main import main

if __name__ == "__main__":
    exit(main())