"""GitHub API client for finding code repositories."""

import requests
import logging
from typing import Optional


class GitHubClient:
    """Client for searching GitHub repositories."""
    
    def __init__(self):
        self.github_url = "https://api.github.com/search/repositories"
    
    def get_code_link(self, query: str) -> Optional[str]:
        """
        Search for code repository related to a paper.
        
        Args:
            query: Search query (paper title, arxiv ID, etc.)
            
        Returns:
            URL of the most relevant repository, or None if not found
        """
        params = {
            "q": query,
            "sort": "stars",
            "order": "desc"
        }
        
        try:
            response = requests.get(self.github_url, params=params)
            response.raise_for_status()
            results = response.json()
            
            if results.get("total_count", 0) > 0:
                return results["items"][0]["html_url"]
                
        except requests.RequestException as e:
            logging.warning(f"GitHub API request failed for query '{query}': {e}")
        except (KeyError, IndexError) as e:
            logging.warning(f"Unexpected GitHub API response format: {e}")
            
        return None
    
    def search_multiple_queries(self, queries: list) -> Optional[str]:
        """
        Try multiple search queries and return the first successful result.
        
        Args:
            queries: List of search queries to try
            
        Returns:
            URL of the first found repository, or None if none found
        """
        for query in queries:
            result = self.get_code_link(query)
            if result:
                return result
        return None