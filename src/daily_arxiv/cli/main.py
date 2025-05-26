"""Main CLI entry point for daily-arxiv."""

import argparse
import logging
import datetime
from typing import Dict, Any

from ..core.config import load_config, validate_config
from ..services.arxiv_client import ArXivClient
from ..services.github_client import GitHubClient
from ..services.email_service import EmailService
from ..processors.file_manager import FileManager
from ..processors.content_generator import ContentGenerator
from ..utils.date_utils import get_dated_file_paths


class DailyArxivApp:
    """Main application class for daily-arxiv."""
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the application with configuration.
        
        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.arxiv_client = ArXivClient(config.get('base_url'))
        self.github_client = GitHubClient()
        self.email_service = EmailService(config)
        self.file_manager = FileManager()
        self.content_generator = ContentGenerator()
    
    def run(self):
        """Run the main application logic."""
        logging.info("Starting daily arXiv paper collection")
        
        # Handle fresh run
        if self.config.get('fresh_run', False):
            logging.info("Fresh run requested. Resetting all JSON files.")
            self.file_manager.reset_json_files(self.config)
        
        # Fetch papers for each category
        all_data = {}
        all_data_web = {}
        
        for topic, query_info in self.config['kv'].items():
            logging.info(f"Fetching papers for: {topic}")
            
            data, data_web = self.arxiv_client.get_daily_papers(
                topic, query_info, self.config.get('max_results', 30)
            )
            
            if data and data.get(topic):
                all_data.update(data)
                all_data_web.update(data_web)
                logging.info(f"Found {len(data[topic])} papers for {topic}")
            else:
                logging.info(f"No papers found for {topic}")
        
        # Update JSON files
        if all_data:
            self._update_output_files(all_data, all_data_web)
        
        # Send email if requested
        if self.config.get('send_email', False) and all_data_web:
            self._send_email_notification(all_data_web)
        
        logging.info("Daily arXiv collection completed")
    
    def _update_output_files(self, data: Dict, data_web: Dict):
        """Update all output files with new paper data."""
        # Update main JSON files
        json_files = [
            self.config.get('json_readme_path'),
            self.config.get('json_gitpage_path')
        ]
        
        for json_file in json_files:
            if json_file:
                self.file_manager.update_json_file(json_file, [data])
        
        # Generate markdown files
        markdown_files = [
            (self.config.get('json_readme_path'), self.config.get('md_readme_path'), False),
            (self.config.get('json_gitpage_path'), self.config.get('md_gitpage_path'), True)
        ]
        
        for json_file, md_file, to_web in markdown_files:
            if json_file and md_file:
                self.content_generator.json_to_md(
                    json_file, md_file, 
                    task=f"Generate {'web' if to_web else 'readme'} markdown",
                    to_web=to_web,
                    show_badge=self.config.get('show_badge', True)
                )
        
        # Update dated log files
        dated_paths = get_dated_file_paths(self.config)
        self.file_manager.update_json_file(dated_paths['json_path'], [data], create_new=True)
        self.content_generator.json_to_md(
            dated_paths['json_path'], dated_paths['md_path'],
            task="Generate daily log", create_new=True
        )
    
    def _send_email_notification(self, data_web: Dict):
        """Send email notification with daily papers."""
        recipient = self.config.get('email_recipient')
        if not recipient:
            logging.warning("No email recipient configured")
            return
        
        date_str = datetime.date.today().strftime("%Y-%m-%d")
        subject = f"Daily arXiv Papers - {date_str}"
        
        html_content = self.email_service.generate_daily_email_content(data_web, date_str)
        
        success = self.email_service.send_email(recipient, subject, html_content)
        if success:
            logging.info("Email notification sent successfully")
        else:
            logging.error("Failed to send email notification")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="Daily arXiv paper aggregator")
    parser.add_argument(
        '--config_path', type=str, default='config.yaml',
        help='configuration file path'
    )
    parser.add_argument(
        '--update_paper_links', default=False, action="store_true",
        help='whether to update paper links etc.'
    )
    parser.add_argument(
        '--fresh-run', default=False, action="store_true",
        help='reset all JSON files (clear existing data) before running'
    )
    parser.add_argument(
        '--send-email', default=False, action="store_true",
        help='send email with today\'s papers'
    )
    parser.add_argument(
        '--email-recipient', type=str, default=None,
        help='email recipient for daily updates (overrides config)'
    )
    parser.add_argument(
        '--smtp-user', type=str, default=None,
        help='SMTP username (overrides config and env variables)'
    )
    parser.add_argument(
        '--smtp-password', type=str, default=None,
        help='SMTP password (overrides config and env variables)'
    )

    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config_path)
    
    if not validate_config(config):
        logging.error("Invalid configuration. Exiting.")
        return 1
    
    # Apply command line overrides
    config.update({
        'update_paper_links': args.update_paper_links,
        'fresh_run': args.fresh_run,
        'send_email': args.send_email or config.get('send_email', False),
    })

    # Override email recipient if provided
    if args.email_recipient:
        config['email_recipient'] = args.email_recipient

    # Override SMTP settings if provided via command line
    if args.smtp_user or args.smtp_password:
        if 'email_settings' not in config:
            config['email_settings'] = {}

        if args.smtp_user:
            config['email_settings']['smtp_user'] = args.smtp_user

        if args.smtp_password:
            config['email_settings']['smtp_password'] = args.smtp_password

    # Run the application
    app = DailyArxivApp(config)
    app.run()
    
    return 0


if __name__ == "__main__":
    exit(main())