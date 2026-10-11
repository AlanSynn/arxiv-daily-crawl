"""File system utilities for arxiv-digest."""

import os
import logging


def ensure_directory_exists(directory: str):
    """
    Ensure that the specified directory exists, creating it if necessary.
    
    Args:
        directory: Path to the directory
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f"Created directory: {directory}")