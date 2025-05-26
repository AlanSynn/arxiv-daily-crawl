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
                    margin: 15px 0;
                    padding: 15px;
                    border-left: 4px solid #007bff;
                    background-color: #f8f9fa;
                    border-radius: 0 4px 4px 0;
                }}
                .paper-title {{
                    font-weight: bold;
                    color: #2c3e50;
                    margin-bottom: 5px;
                }}
                .paper-authors {{
                    color: #6c757d;
                    font-size: 0.9em;
                    margin-bottom: 8px;
                }}
                .paper-links a {{
                    color: #007bff;
                    text-decoration: none;
                    margin-right: 15px;
                    font-weight: 500;
                }}
                .paper-links a:hover {{
                    text-decoration: underline;
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
                        html_content += self._format_paper_for_email(paper_content)
                    
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
    
    def _format_paper_for_email(self, paper_content: str) -> str:
        """Format paper content for HTML email display."""
        # Parse the paper content (assuming it's in a specific format)
        # This is a simplified version - you might need to adjust based on actual format
        return f"""
        <div class="paper">
            {paper_content.replace('\\n', '<br>')}
        </div>
        """