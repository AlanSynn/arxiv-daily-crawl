"""File management and I/O operations for daily-arxiv."""

import os
import json
import logging
from typing import Dict, List, Any

from ..utils.file_utils import ensure_directory_exists


class FileManager:
    """Handles file operations for daily-arxiv."""
    
    def update_json_file(self, filename: str, data_dict: List[Dict], create_new: bool = False) -> Dict:
        """
        Update JSON file with new paper data.
        
        Args:
            filename: Path to the JSON file
            data_dict: List of dictionaries containing paper data
            create_new: If True, create a new file instead of updating existing one
            
        Returns:
            Updated JSON data dictionary
        """
        # Ensure the directory exists
        directory = os.path.dirname(filename)
        if directory:
            ensure_directory_exists(directory)

        if create_new or not os.path.exists(filename) or os.path.getsize(filename) == 0:
            json_data = self._create_new_json_file(filename, data_dict)
        else:
            json_data = self._update_existing_json_file(filename, data_dict)

        return json_data
    
    def _create_new_json_file(self, filename: str, data_dict: List[Dict]) -> Dict:
        """Create a new JSON file with the provided data."""
        json_data = {}
        
        for data in data_dict:
            for keyword, papers in data.items():
                if keyword in json_data:
                    json_data[keyword].update(papers)
                else:
                    json_data[keyword] = papers

        with open(filename, "w", encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
        logging.info(f"Created new JSON file: {filename}")
        
        return json_data
    
    def _update_existing_json_file(self, filename: str, data_dict: List[Dict]) -> Dict:
        """Update an existing JSON file with new data."""
        try:
            with open(filename, "r", encoding='utf-8') as f:
                content = f.read()
                json_data = json.loads(content) if content else {}
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.warning(f"Error reading {filename}: {e}. Creating a new file.")
            json_data = {}

        # Update papers in each category
        for data in data_dict:
            for keyword, papers in data.items():
                if keyword in json_data:
                    json_data[keyword].update(papers)
                else:
                    json_data[keyword] = papers

        with open(filename, "w", encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
        logging.info(f"Updated existing JSON file: {filename}")
        
        return json_data
    
    def reset_json_files(self, config: Dict):
        """
        Reset (delete) all JSON files for a fresh start.
        
        Args:
            config: Configuration dictionary containing file paths
        """
        json_files = [
            config.get('json_readme_path'),
            config.get('json_gitpage_path')
        ]
        
        for json_file in json_files:
            if json_file and os.path.exists(json_file):
                try:
                    os.remove(json_file)
                    logging.info(f"Removed JSON file: {json_file}")
                except OSError as e:
                    logging.error(f"Error removing {json_file}: {e}")
    
    def load_json_file(self, filename: str) -> Dict:
        """
        Load data from a JSON file.
        
        Args:
            filename: Path to the JSON file
            
        Returns:
            Dictionary containing the JSON data
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.warning(f"Error loading {filename}: {e}")
            return {}