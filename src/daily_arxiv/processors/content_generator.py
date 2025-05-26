"""Content generation for markdown and other formats."""

import os
import re
import json
import logging
import datetime
from typing import Dict, Any

from ..utils.file_utils import ensure_directory_exists


class ContentGenerator:
    """Generates markdown and other content formats from paper data."""
    
    def json_to_md(self, json_filename: str, md_filename: str, 
                   task: str = '', to_web: bool = False, 
                   use_title: bool = True, use_tc: bool = True,
                   show_badge: bool = True, use_b2t: bool = True,
                   create_new: bool = False):
        """
        Convert JSON data to markdown format.
        
        Args:
            json_filename: Path to input JSON file
            md_filename: Path to output markdown file
            task: Task description for logging
            to_web: Whether generating for web output
            use_title: Whether to include title
            use_tc: Whether to include table of contents
            show_badge: Whether to show badges
            use_b2t: Whether to use back-to-top links
            create_new: Whether to create a new file
        """
        # Ensure output directory exists
        directory = os.path.dirname(md_filename)
        if directory:
            ensure_directory_exists(directory)

        date_now = datetime.date.today().strftime("%Y.%m.%d")
        
        # Load JSON data
        data = self._load_json_data(json_filename)
        
        if not data:
            logging.warning(f"No data found in {json_filename}")
            return

        # Generate markdown content
        md_content = self._generate_markdown_content(
            data, date_now, to_web, use_title, use_tc, show_badge, use_b2t
        )
        
        # Write to file
        with open(md_filename, "w", encoding='utf-8') as f:
            f.write(md_content)
        
        logging.info(f"{task} finished: {md_filename}")
    
    def _load_json_data(self, filename: str) -> Dict:
        """Load data from JSON file."""
        if not os.path.exists(filename):
            logging.warning(f"JSON file {filename} not found.")
            return {}
        
        try:
            with open(filename, "r", encoding='utf-8') as f:
                content = f.read()
                return json.loads(content) if content else {}
        except (json.JSONDecodeError, FileNotFoundError) as e:
            logging.error(f"Error loading JSON from {filename}: {e}")
            return {}
    
    def _generate_markdown_content(self, data: Dict, date_now: str, 
                                 to_web: bool, use_title: bool, 
                                 use_tc: bool, show_badge: bool, 
                                 use_b2t: bool) -> str:
        """Generate the complete markdown content."""
        content_parts = []
        
        # Add header
        if use_title:
            content_parts.append(self._generate_header(show_badge))
        
        # Add update date
        content_parts.append(f"## 📚 Updated on {date_now}")
        
        # Add usage instructions if not for web
        if not to_web:
            content_parts.append("> 📖 Usage instructions: [here](./docs/README.md#usage)")
        
        # Add table of contents
        if use_tc and data:
            content_parts.append(self._generate_table_of_contents(data))
        
        # Add paper sections
        for topic, papers in data.items():
            if papers:  # Only add sections with papers
                section_content = self._generate_paper_section(
                    topic, papers, use_b2t
                )
                content_parts.append(section_content)
        
        # Add footer
        content_parts.append(self._generate_footer())
        
        return "\\n\\n".join(content_parts)
    
    def _generate_header(self, show_badge: bool) -> str:
        """Generate markdown header with badges."""
        header = []
        
        if show_badge:
            badges = [
                "[![Contributors][contributors-shield]][contributors-url]",
                "[![Forks][forks-shield]][forks-url]", 
                "[![Stargazers][stars-shield]][stars-url]",
                "[![Issues][issues-shield]][issues-url]"
            ]
            header.extend(badges)
        
        return "\\n".join(header)
    
    def _generate_table_of_contents(self, data: Dict) -> str:
        """Generate table of contents from paper categories."""
        toc_lines = [
            "<details>",
            "  <summary>Table of Contents</summary>",
            "  <ol>"
        ]
        
        for topic in data.keys():
            # Convert topic to anchor link format
            anchor = topic.replace(" ", "-").replace("&", "").replace(",", "").replace(":", "")
            toc_lines.append(f"    <li><a href=#{anchor}>{topic}</a></li>")
        
        toc_lines.extend(["  </ol>", "</details>"])
        
        return "\\n".join(toc_lines)
    
    def _generate_paper_section(self, topic: str, papers: Dict, use_b2t: bool) -> str:
        """Generate a section for a specific paper topic."""
        section_lines = [
            f"## {topic}",
            "",
            "|Publish Date|Title|Authors|arXiv|Code|",
            "|---|---|---|---|---|"
        ]
        
        # Add papers (they should already be formatted strings)
        for paper_content in papers.values():
            section_lines.append(paper_content.rstrip('\\n'))
        
        if use_b2t:
            section_lines.append("")
            section_lines.append("<p align=right>(<a href=#updated-on-{date}>back to top</a>)</p>")
        
        return "\\n".join(section_lines)
    
    def _generate_footer(self) -> str:
        """Generate markdown footer with links."""
        return """
[contributors-shield]: https://img.shields.io/github/contributors/AlanSynn/daily-arxiv.svg?style=for-the-badge
[contributors-url]: https://github.com/AlanSynn/daily-arxiv/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AlanSynn/daily-arxiv.svg?style=for-the-badge
[forks-url]: https://github.com/AlanSynn/daily-arxiv/network/members
[stars-shield]: https://img.shields.io/github/stars/AlanSynn/daily-arxiv.svg?style=for-the-badge
[stars-url]: https://github.com/AlanSynn/daily-arxiv/stargazers
[issues-shield]: https://img.shields.io/github/issues/AlanSynn/daily-arxiv.svg?style=for-the-badge
[issues-url]: https://github.com/AlanSynn/daily-arxiv/issues
        """.strip()
    
    def _pretty_math(self, s: str) -> str:
        """Clean up math expressions in text."""
        match = re.search(r"\\$.*\\$", s)
        if not match:
            return s
            
        math_start, math_end = match.span()
        space_trail = space_leading = ''
        
        if s[:math_start] and s[:math_start][-1] not in [' ', '*']:
            space_trail = ' '
        if s[math_end:] and s[math_end:][0] not in [' ', '*']:
            space_leading = ' '
            
        result = s[:math_start]
        result += f'{space_trail}${match.group()[1:-1].strip()}${space_leading}'
        result += s[math_end:]
        
        return result