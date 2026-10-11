"""Date and time utilities for arxiv-digest."""

import datetime
import os
import re
from typing import Dict


def github_slug(text: str) -> str:
    """GitHub-flavored markdown heading anchor slug.

    Mirrors GitHub's server-side anchor generation so in-page links line up
    with rendered ``## {heading}`` sections.  Non-word characters (``&``,
    ``(``, ``:``, ``/``, ...) are *removed* rather than replaced; the spaces
    flanking them then each collapse into their own hyphen, which is what
    produces the double-hyphen in e.g.
    ``"World Models & Generative Video" -> "world-models--generative-video"``.

    Algorithm:
      1. strip + lowercase
      2. drop every char that is not a word char, hyphen, or space
      3. spaces -> hyphens
      4. strip leading/trailing hyphens
    """
    s = text.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    s = s.replace(" ", "-")
    return s.strip("-")


def format_authors(authors, first_author: bool = False) -> str:
    """
    Format author list into a string.
    
    Args:
        authors: List of author objects
        first_author: If True, return only the first author
        
    Returns:
        Formatted author string
    """
    if not authors:
        return ""
    
    if first_author:
        return str(authors[0])
    
    return ", ".join(str(author) for author in authors)


def get_dated_file_paths(config: Dict, date_str: str = None) -> Dict[str, str]:
    """
    Generate file paths with date included.
    
    Args:
        config: Configuration dictionary
        date_str: Date string in YYYY-MM-DD format, uses today if None
        
    Returns:
        Dictionary with dated file paths for JSON and MD files
    """
    if date_str is None:
        date_str = datetime.date.today().strftime("%Y-%m-%d")

    # Create log directories if they don't exist
    log_dir = config.get('log_dir', './logs')
    _ensure_directory_exists(log_dir)

    json_log_dir = os.path.join(log_dir, 'json')
    md_log_dir = os.path.join(log_dir, 'md')
    _ensure_directory_exists(json_log_dir)
    _ensure_directory_exists(md_log_dir)

    return {
        'json_path': os.path.join(json_log_dir, f"daily-arxiv_{date_str}.json"),
        'md_path': os.path.join(md_log_dir, f"daily-arxiv_{date_str}.md"),
        'json_web_path': os.path.join(json_log_dir, f"daily-arxiv-web_{date_str}.json"),
        'md_web_path': os.path.join(md_log_dir, f"daily-arxiv-web_{date_str}.md")
    }


def _ensure_directory_exists(directory: str):
    """Ensure that the specified directory exists, creating it if necessary."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        import logging
        logging.info(f"Created directory: {directory}")


def sort_papers(papers: Dict) -> Dict:
    """
    Sort papers dictionary by date keys in descending order.
    
    Args:
        papers: Dictionary with date keys
        
    Returns:
        Sorted dictionary with most recent papers first
    """
    sorted_keys = sorted(papers.keys(), reverse=True)
    return {key: papers[key] for key in sorted_keys}