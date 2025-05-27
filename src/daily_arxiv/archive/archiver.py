import os
import json
import logging
import datetime
import yaml
import re
import argparse
import arxiv

logging.basicConfig(format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)

def load_config(config_file:str) -> dict:
    '''
    config_file: input config file path
    return: a dict of configuration
    '''
    with open(config_file,'r') as f:
        config = yaml.load(f,Loader=yaml.FullLoader)
        logging.info(f'config = {config}')
    return config

def parse_date(date_str):
    """Parse date from string format in papers"""
    date_str = date_str.strip('*')  # Remove asterisks used for bold formatting
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            logging.error(f"Failed to parse date: {date_str}")
            return None

def parse_paper_entry(paper_entry):
    """Parse a paper entry from the JSON data"""
    # Format is typically |**date**|**title**|authors|[id](url)|code|
    parts = paper_entry.split('|')
    if len(parts) >= 6:
        date_str = parts[1].strip('*')
        paper_date = parse_date(date_str)
        paper_id = re.search(r'\[(.*?)\]', parts[4]).group(1) if re.search(r'\[(.*?)\]', parts[4]) else None
        return {
            'date': paper_date,
            'entry': paper_entry,
            'id': paper_id
        }
    return None

def archive_old_papers(json_file, archive_dir, max_age_days=365):
    """
    Archive papers older than max_age_days (default 1 year)

    Args:
        json_file: Path to the JSON file containing papers
        archive_dir: Directory to store archived papers
        max_age_days: Maximum age in days before a paper is archived
    """
    today = datetime.date.today()
    cutoff_date = today - datetime.timedelta(days=max_age_days)

    # Create archive directory if it doesn't exist
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    # Load the existing JSON data
    try:
        with open(json_file, 'r') as f:
            content = f.read()
            if not content:
                logging.warning(f"Empty file: {json_file}")
                return
            data = json.loads(content)
    except Exception as e:
        logging.error(f"Error loading JSON file {json_file}: {e}")
        return

    # Create archive JSON if it doesn't exist
    archive_file = os.path.join(archive_dir, f"archive_{today.strftime('%Y%m')}.json")
    archive_data = {}
    if os.path.exists(archive_file):
        try:
            with open(archive_file, 'r') as f:
                content = f.read()
                if content:
                    archive_data = json.loads(content)
        except Exception as e:
            logging.error(f"Error loading archive file {archive_file}: {e}")

    papers_to_remove = {}
    # Process each category of papers
    for category, papers in data.items():
        papers_to_remove[category] = []
        if category not in archive_data:
            archive_data[category] = {}

        # Check each paper's date
        for paper_id, paper_entry in papers.items():
            parsed_paper = parse_paper_entry(paper_entry)
            if not parsed_paper or not parsed_paper['date']:
                continue

            if parsed_paper['date'] < cutoff_date:
                # Paper is older than max_age_days, move to archive
                archive_data[category][paper_id] = paper_entry
                papers_to_remove[category].append(paper_id)
                logging.info(f"Archiving paper {paper_id} from {parsed_paper['date']}")

    # Remove archived papers from original data
    for category, paper_ids in papers_to_remove.items():
        for paper_id in paper_ids:
            if paper_id in data[category]:
                del data[category][paper_id]
        # Remove empty categories
        if not data[category]:
            del data[category]

    # Save the updated main JSON
    with open(json_file, 'w') as f:
        json.dump(data, f)

    # Save the archive JSON
    with open(archive_file, 'w') as f:
        json.dump(archive_data, f)

    # Create archive markdown file
    archive_md_file = os.path.join(archive_dir, f"archive_{today.strftime('%Y%m')}.md")
    generate_archive_markdown(archive_data, archive_md_file)

    logging.info(f"Archived {sum(len(ids) for ids in papers_to_remove.values())} papers to {archive_file}")
    return archive_file

def generate_archive_markdown(archive_data, output_file):
    """Generate a markdown file from the archived JSON data"""
    with open(output_file, 'w') as f:
        f.write("# 📚 Archived Papers\n\n")
        f.write(f"*Last updated: {datetime.date.today().strftime('%Y-%m-%d')}*\n\n")

        # Table of contents
        f.write("## 📋 Table of Contents\n\n")
        for category in archive_data.keys():
            if archive_data[category]:  # Only add categories with papers
                category_link = category.replace(' ', '-').lower()
                f.write(f"- [{category}](#{category_link})\n")
        f.write("\n")

        # Write each category
        for category, papers in archive_data.items():
            if not papers:
                continue

            f.write(f"## 📑 {category}\n\n")

            # Sort papers by date (newest first)
            sorted_papers = sorted(
                papers.items(),
                key=lambda x: parse_date(x[1].split('|')[1]) if parse_date(x[1].split('|')[1]) else datetime.date.min,
                reverse=True
            )

            for paper_id, paper_entry in sorted_papers:
                # Process paper_entry - it might have simplified formatting for table in README
                # But we want to include abstracts in the archived version if they exist
                parts = paper_entry.split('|')
                if len(parts) >= 6:
                    date = parts[1].strip('*')
                    title = parts[2].strip('*')
                    authors = parts[3].strip()
                    paper_link = parts[4].strip()
                    code_link = parts[5].strip()

                    f.write(f"### {title}\n\n")
                    f.write(f"**📅 Date:** {date}  \n")
                    f.write(f"**👨‍🔬 Authors:** {authors}  \n")
                    f.write(f"**📄 Paper:** {paper_link}  \n")
                    if code_link != "null" and code_link.strip():
                        f.write(f"**💻 Code:** {code_link}  \n")

                    # Try to fetch abstract if not in the entry
                    try:
                        paper_id_clean = re.search(r'\[(.*?)\]', paper_link).group(1) if re.search(r'\[(.*?)\]', paper_link) else None
                        if paper_id_clean:
                            search = arxiv.Search(id_list=[paper_id_clean])
                            paper = next(search.results())
                            abstract = paper.summary.replace("\n", " ")
                            f.write(f"\n**📝 Abstract:** {abstract}\n\n")
                    except Exception as e:
                        logging.warning(f"Could not fetch abstract for {paper_id}: {e}")

                f.write("\n---\n\n")

            f.write("\n")

def update_config_for_archiving(config_file):
    """Update the config file to include archive settings"""
    config = load_config(config_file)

    # Add archive settings if they don't exist
    if 'archive_settings' not in config:
        config['archive_settings'] = {
            'enabled': True,
            'max_age_days': 365,  # 1 year
            'archive_dir': './docs/archive'
        }

        # Write the updated config back to the file
        with open(config_file, 'w') as f:
            yaml.dump(config, f, default_flow_style=False)

        logging.info(f"Updated config file with archive settings")

    return config

def main():
    parser = argparse.ArgumentParser(description='Archive old papers from daily-arxiv')
    parser.add_argument('--config', type=str, default='config.yaml', help='Path to config file')
    args = parser.parse_args()

    # Update config if needed and load it
    config = update_config_for_archiving(args.config)

    if config['archive_settings']['enabled']:
        # Archive papers from all JSON files mentioned in config
        json_files = [
            config['json_readme_path'],
            config['json_gitpage_path']
        ]

        for json_file in json_files:
            if os.path.exists(json_file):
                archive_old_papers(
                    json_file,
                    config['archive_settings']['archive_dir'],
                    config['archive_settings']['max_age_days']
                )

    logging.info("Archiving completed")

if __name__ == "__main__":
    main()