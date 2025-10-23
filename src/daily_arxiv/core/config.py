"""Configuration loading and processing for daily-arxiv."""

import os
import yaml
import logging
from typing import Dict, Any


def load_config(config_file: str) -> Dict[str, Any]:
    """
    Load and process configuration from YAML file.
    
    Args:
        config_file: Path to the configuration file
        
    Returns:
        Dictionary containing processed configuration
    """
    def _parse_filters(filters: list) -> str:
        """Parse filter list into query string format."""
        escape = '"'
        or_operator = ' OR '
        
        result = ''
        for idx, filter_term in enumerate(filters):
            if len(filter_term.split()) > 1:
                result += f'{escape}{filter_term}{escape}'
            else:
                result += filter_term
            
            if idx != len(filters) - 1:
                result += or_operator
                
        return result
    
    def _create_search_queries(config: Dict[str, Any]) -> Dict[str, str]:
        """Create search query strings from keyword filters."""
        keywords = {}
        for category, settings in config['keywords'].items():
            keywords[category] = _parse_filters(settings['filters'])
        return keywords

    with open(config_file, 'r', encoding='utf-8') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    # Process environment variables in email settings
    if 'email_settings' in config:
        email_settings = config['email_settings']
        
        # Replace environment variables
        if '${SMTP_USER}' in email_settings.get('smtp_user', ''):
            email_settings['smtp_user'] = os.environ.get('SMTP_USER', '')
            
        if '${SMTP_PASSWORD}' in email_settings.get('smtp_password', ''):
            email_settings['smtp_password'] = os.environ.get('SMTP_PASSWORD', '')

    # Handle email recipient
    if '${EMAIL_RECIPIENT}' in config.get('email_recipient', ''):
        config['email_recipient'] = os.environ.get('EMAIL_RECIPIENT', 'alansynn@gatech.edu')

    # Set default log directory if not specified
    if 'log_dir' not in config:
        config['log_dir'] = './logs'

    # Create search query strings from keywords
    config['kv'] = _create_search_queries(config)
    
    logging.info(f'Loaded configuration from {config_file}')
    return config


def validate_config(config: Dict[str, Any]) -> bool:
    """
    Validate configuration completeness.
    
    Args:
        config: Configuration dictionary
        
    Returns:
        True if configuration is valid
    """
    required_keys = ['base_url', 'keywords', 'max_results']
    
    for key in required_keys:
        if key not in config:
            logging.error(f"Missing required configuration key: {key}")
            return False
    
    if 'keywords' in config and not config['keywords']:
        logging.error("No keywords defined in configuration")
        return False
        
    return True