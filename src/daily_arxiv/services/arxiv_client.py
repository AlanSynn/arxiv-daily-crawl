"""ArXiv API client for fetching research papers."""

import arxiv
import requests
import logging
from typing import Dict, Tuple, Optional
from datetime import date, timedelta

from ..utils.date_utils import format_authors


class ArXivClient:
    """Client for interacting with ArXiv API."""

    def __init__(self, base_url: str = "https://arxiv.paperswithcode.com/api/v0/papers/"):
        self.base_url = base_url
        self.arxiv_url = "http://arxiv.org/"

    def get_daily_papers(self, topic: str, query: str = "computational design",
                        max_results: int = 5) -> Tuple[Dict, Dict, Dict, Dict]:
        """
        Fetch papers from ArXiv for a given topic and query.

        Args:
            topic: Research topic/category name
            query: Search query string
            max_results: Maximum number of results to fetch

        Returns:
            Tuple of (email_content, email_content_web, main_content, main_content_web)
            - email_content: Papers for email (most recent day only)
            - email_content_web: Web version of email papers
            - main_content: All papers for main report
            - main_content_web: Web version of all papers for main report
        """
        email_content = {}
        email_content_web = {}
        main_content = {}
        main_content_web = {}

        search_engine = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )

        # Collect all papers first
        all_papers = []
        try:
            for result in search_engine.results():
                paper_data = self._process_paper_result(result)
                if paper_data:
                    all_papers.append(paper_data)
        except arxiv.UnexpectedEmptyPageError as e:
            # This can happen when the API returns fewer results than expected
            # Just log it and continue with whatever papers we collected
            logging.warning(f"ArXiv API returned empty page for {topic}: {e}")
            logging.info(f"Collected {len(all_papers)} papers before encountering empty page")
        except Exception as e:
            # Log other errors but don't fail completely
            logging.error(f"Error fetching papers for {topic}: {e}")
            logging.info(f"Collected {len(all_papers)} papers before error")

        if not all_papers:
            logging.info(f"No papers found for {topic}")
            return ({topic: email_content}, {topic: email_content_web},
                    {topic: main_content}, {topic: main_content_web})

        # Find the most recent date
        most_recent_date = max(paper['update_time'] for paper in all_papers)
        logging.info(f"Most recent paper date: {most_recent_date}")

        # Process papers
        for paper_data in all_papers:
            paper_key = paper_data['paper_key']
            update_time = paper_data['update_time']

            # Add to main (all papers)
            main_content[paper_key] = paper_data['content']
            main_content_web[paper_key] = paper_data['content_web']

            # Add to email only if paper is from the most recent day
            if update_time == most_recent_date:
                email_content[paper_key] = paper_data['content']
                email_content_web[paper_key] = paper_data['content_web']
            else:
                logging.info(f"Excluding from email (not most recent day): {paper_data['paper_title']} ({update_time})")

        logging.info(f"Found {len(main_content)} total papers, {len(email_content)} papers from most recent day ({most_recent_date}) for email")
        return ({topic: email_content}, {topic: email_content_web},
                {topic: main_content}, {topic: main_content_web})

    def _process_paper_result(self, result) -> Optional[Dict]:
        """Process a single ArXiv result into structured data."""
        try:
            paper_id = result.get_short_id()
            paper_title = result.title
            paper_url = result.entry_id
            code_url = self.base_url + paper_id
            paper_abstract = result.summary.replace("\n", " ")
            paper_authors = format_authors(result.authors)
            paper_first_author = format_authors(result.authors, first_author=True)
            publish_time = result.published.date()
            update_time = result.updated.date()
            comments = result.comment

            logging.info(f"Processing: {update_time} - {paper_title} by {paper_first_author}")

            # Clean paper ID (remove version info)
            ver_pos = paper_id.find('v')
            paper_key = paper_id[0:ver_pos] if ver_pos != -1 else paper_id
            paper_url = f"{self.arxiv_url}abs/{paper_key}"

            # Get code repository URL
            repo_url = self._get_paper_code_url(code_url)

            # Generate content strings
            content_data = self._generate_content_strings(
                update_time, paper_title, paper_first_author,
                paper_key, paper_url, repo_url, paper_abstract
            )

            return {
                'paper_key': paper_key,
                'paper_title': paper_title,
                'update_time': update_time,
                'content': content_data['content'],
                'content_web': content_data['content_web']
            }

        except Exception as e:
            logging.error(f"Error processing paper {result.get_short_id()}: {e}")
            return None

    def _get_paper_code_url(self, code_url: str) -> Optional[str]:
        """Get code repository URL for a paper."""
        try:
            response = requests.get(code_url)
            data = response.json()

            if "official" in data and data["official"]:
                return data["official"]["url"]
        except Exception as e:
            logging.debug(f"Could not fetch code URL from {code_url}: {e}")

        return None

    def _generate_content_strings(self, update_time: date, paper_title: str,
                                 paper_first_author: str, paper_key: str,
                                 paper_url: str, repo_url: Optional[str],
                                 paper_abstract: str) -> Dict[str, str]:
        """Generate markdown content strings for paper."""
        if repo_url:
            content = (f"|**{update_time}**|**{paper_title}**|{paper_first_author} et.al.|"
                      f"[@{paper_key}]({paper_url})|**[link]({repo_url})**|\\n")
            content_web = (f"- {update_time}, **{paper_title}**, {paper_first_author} et.al., "
                          f"Paper: [@{paper_key}]({paper_url}), Code: **[link]({repo_url})** \\n"
                          f"> **Abstract:** {paper_abstract}\\n")
        else:
            content = (f"|**{update_time}**|**{paper_title}**|{paper_first_author} et.al.|"
                      f"[@{paper_key}]({paper_url})|null|\\n")
            content_web = (f"- {update_time}, **{paper_title}**, {paper_first_author} et.al., "
                          f"Paper: [@{paper_key}]({paper_url}) \\n"
                          f"> **Abstract:** {paper_abstract}\\n")

        return {'content': content, 'content_web': content_web}