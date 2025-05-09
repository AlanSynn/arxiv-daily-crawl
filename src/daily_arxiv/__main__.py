"""Entry point for running daily-arxiv as a module."""

from .cli.main import main

if __name__ == "__main__":
    exit(main())