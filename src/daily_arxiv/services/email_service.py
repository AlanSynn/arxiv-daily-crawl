"""Email service for sending daily paper updates."""

import smtplib
import logging
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Dict, Any


class EmailService:
    """Service for sending email notifications."""

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize email service with configuration.

        Args:
            config: Configuration dictionary containing email settings
        """
        self.config = config
        self.email_settings = config.get('email_settings', {})

    def send_email(self, email_to: str, email_subject: str, email_body: str) -> bool:
        """
        Send email with daily paper updates.

        Args:
            email_to: Recipient email address
            email_subject: Email subject
            email_body: Email body content (HTML format)

        Returns:
            True if email sent successfully, False otherwise
        """
        if not self._is_email_enabled():
            logging.warning("Email settings not configured or disabled")
            return False

        if not self._validate_smtp_settings():
            logging.error("SMTP settings incomplete. Check your config file.")
            return False

        msg = self._create_email_message(email_to, email_subject, email_body)

        return self._send_via_smtp(msg, email_to)

    def generate_daily_email_content(self, data_collector_web: Dict, date_now: str) -> str:
        """
        Generate HTML email content from paper data.

        Args:
            data_collector_web: Dictionary containing paper data for web display
            date_now: Current date string

        Returns:
            HTML email content string
        """
        return self._get_email_body(data_collector_web, date_now)

    def _is_email_enabled(self) -> bool:
        """Check if email functionality is enabled."""
        return self.email_settings.get('enabled', False)

    def _validate_smtp_settings(self) -> bool:
        """Validate that all required SMTP settings are present."""
        required_settings = ['smtp_server', 'smtp_user', 'smtp_password']
        return all(self.email_settings.get(setting) for setting in required_settings)

    def _create_email_message(self, email_to: str, email_subject: str, email_body: str) -> MIMEMultipart:
        """Create email message with HTML and text parts."""
        msg = MIMEMultipart('alternative')
        msg['Subject'] = email_subject
        msg['From'] = self.email_settings['smtp_user']
        msg['To'] = email_to

        # Create both plain text and HTML versions
        text_part = MIMEText("This email requires HTML support to view properly.", 'plain')
        html_part = MIMEText(email_body, 'html')

        msg.attach(text_part)
        msg.attach(html_part)

        return msg

    def _send_via_smtp(self, msg: MIMEMultipart, email_to: str) -> bool:
        """Send email via SMTP server."""
        try:
            with smtplib.SMTP(self.email_settings['smtp_server'],
                            self.email_settings.get('smtp_port', 587)) as server:
                server.ehlo()
                server.starttls()
                server.login(self.email_settings['smtp_user'],
                           self.email_settings['smtp_password'])
                server.send_message(msg)

            logging.info(f"Email sent successfully to {email_to}")
            return True

        except Exception as e:
            logging.error(f"Failed to send email: {e}")
            return False

    @staticmethod
    def _format_paper_content(paper_content: str) -> str:
        """
        Formats the paper content into HTML with improved structure.

        Args:
            paper_content: The content of the paper.

        Returns:
            The formatted paper content.
        """
        # Parse the paper content to extract structured information
        lines = paper_content.strip().split('\n')
        if len(lines) < 3:
            # Fallback for malformed content
            formatted_content = paper_content.replace('\n', '<br>')
            return f'<div class="paper">{formatted_content}</div>'

        # Extract paper information
        date_line = lines[0] if lines[0].startswith('**') else ""
        title_line = lines[1] if len(lines) > 1 else ""
        authors_line = lines[2] if len(lines) > 2 else ""
        links_line = lines[3] if len(lines) > 3 else ""

        # Clean up the extracted information
        date = date_line.replace('**', '').strip()
        title = title_line.replace('**', '').strip()
        authors = authors_line.strip()

        # Parse links
        arxiv_link = ""
        code_link = ""
        if '[@' in links_line and '](' in links_line:
            # Extract arXiv link
            import re
            arxiv_match = re.search(r'\[@([^\]]+)\]\(([^)]+)\)', links_line)
            if arxiv_match:
                arxiv_id = arxiv_match.group(1)
                arxiv_url = arxiv_match.group(2)
                arxiv_link = f'<a href="{arxiv_url}" class="arxiv-link">📄 arXiv:{arxiv_id}</a>'

            # Extract code link
            if '**[link](' in links_line:
                code_match = re.search(r'\*\*\[link\]\(([^)]+)\)', links_line)
                if code_match:
                    code_url = code_match.group(1)
                    code_link = f'<a href="{code_url}" class="code-link">💻 Code</a>'
            elif 'null' in links_line:
                code_link = '<span class="no-code">💻 No Code</span>'

        return f"""
        <div class="paper">
            <div class="paper-header">
                <div class="paper-date">{date}</div>
                <h3 class="paper-title">{title}</h3>
                <div class="paper-authors">{authors}</div>
            </div>
            <div class="paper-links">
                {arxiv_link}
                {code_link}
            </div>
        </div>
        """

    def _get_email_body(
        self,
        data_collector_web: Dict,
        date_now: str
    ) -> str:
        """
        Get the email body content.

        Args:
            data_collector_web: The collected data for the web.
            date_now: The current date.

        Returns:
            The formatted email body.
        """
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Daily arXiv Papers - {date_now}</title>
            <style>
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                    line-height: 1.6;
                    color: #333;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f8f9fa;
                }}
                .header {{
                    text-align: center;
                    padding: 20px 0;
                    border-bottom: 2px solid #e9ecef;
                    margin-bottom: 30px;
                }}
                .header h1 {{
                    color: #2c3e50;
                    margin: 0;
                    font-size: 2.5em;
                }}
                .date {{
                    color: #6c757d;
                    font-size: 1.1em;
                    margin-top: 10px;
                }}
                .category {{
                    margin: 30px 0;
                    background: white;
                    border-radius: 8px;
                    padding: 20px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
                .category h2 {{
                    color: #495057;
                    border-bottom: 2px solid #dee2e6;
                    padding-bottom: 10px;
                    margin-top: 0;
                }}
                .paper {{
                    margin: 20px 0;
                    padding: 20px;
                    background: white;
                    border-radius: 8px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
                    border-left: 4px solid #007bff;
                    transition: box-shadow 0.2s ease;
                }}
                .paper:hover {{
                    box-shadow: 0 4px 12px rgba(0,0,0,0.12);
                }}
                .paper-header {{
                    margin-bottom: 15px;
                }}
                .paper-date {{
                    font-size: 0.85em;
                    color: #28a745;
                    font-weight: 600;
                    margin-bottom: 8px;
                    text-transform: uppercase;
                    letter-spacing: 0.5px;
                }}
                .paper-title {{
                    font-size: 1.2em;
                    font-weight: 600;
                    color: #2c3e50;
                    line-height: 1.4;
                    margin: 8px 0;
                    text-decoration: none;
                }}
                .paper-authors {{
                    color: #6c757d;
                    font-size: 0.95em;
                    margin-bottom: 12px;
                    font-style: italic;
                }}
                .paper-links {{
                    padding-top: 12px;
                    border-top: 1px solid #e9ecef;
                }}
                .paper-links a {{
                    display: inline-block;
                    color: #007bff;
                    text-decoration: none;
                    margin-right: 20px;
                    font-weight: 500;
                    font-size: 0.9em;
                    padding: 6px 12px;
                    border-radius: 6px;
                    background-color: #f8f9fa;
                    border: 1px solid #dee2e6;
                    transition: all 0.2s ease;
                }}
                .paper-links a:hover {{
                    background-color: #007bff;
                    color: white;
                    text-decoration: none;
                    transform: translateY(-1px);
                }}
                .paper-links .no-code {{
                    display: inline-block;
                    color: #6c757d;
                    font-size: 0.9em;
                    padding: 6px 12px;
                    border-radius: 6px;
                    background-color: #f8f9fa;
                    border: 1px solid #dee2e6;
                }}
                .arxiv-link {{
                    background-color: #e8f4f8 !important;
                    border-color: #17a2b8 !important;
                    color: #17a2b8 !important;
                }}
                .arxiv-link:hover {{
                    background-color: #17a2b8 !important;
                    color: white !important;
                }}
                .code-link {{
                    background-color: #e8f5e8 !important;
                    border-color: #28a745 !important;
                    color: #28a745 !important;
                }}
                .code-link:hover {{
                    background-color: #28a745 !important;
                    color: white !important;
                }}
                .abstract {{
                    color: #495057;
                    font-style: italic;
                    margin-top: 10px;
                    padding: 10px;
                    background-color: white;
                    border-radius: 4px;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 40px;
                    padding-top: 20px;
                    border-top: 2px solid #e9ecef;
                    color: #6c757d;
                    font-size: 0.9em;
                }}
                .emoji {{
                    font-size: 1.2em;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1><span class="emoji">📚</span> Daily arXiv Papers</h1>
                <div class="date">{date_now}</div>
            </div>
        """

        # Add paper content
        if not data_collector_web:
            html_content += """
            <div class="category">
                <p style="text-align: center; color: #6c757d; font-style: italic;">
                    No new papers found today. Check back tomorrow!
                </p>
            </div>
            """
        else:
            for category, papers in data_collector_web.items():
                if papers:
                    html_content += f"""
                    <div class="category">
                        <h2><span class="emoji">🔬</span> {category}</h2>
                    """

                    for paper_content in papers.values():
                        html_content += self._format_paper_content(paper_content)

                    html_content += "</div>"

        # Add footer
        html_content += """
            <div class="footer">
                <p>
                    <span class="emoji">🤖</span> Generated automatically by
                    <a href="https://github.com/AlanSynn/daily-arxiv" style="color: #007bff;">daily-arxiv</a>
                </p>
                <p>
                    <span class="emoji">📧</span> You're receiving this because you subscribed to daily arXiv updates
                </p>
            </div>
        </body>
        </html>
        """

        return html_content