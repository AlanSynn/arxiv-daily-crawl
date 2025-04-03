# CV Arxiv Paper Archive System

This document explains the paper archiving system implemented for the CV Arxiv Daily project.

## Overview

The CV Arxiv Daily project automatically collects and organizes Computer Vision papers from arXiv. To keep the main collection current and relevant, papers older than 1 year are automatically archived.

## How the Archive Works

1. Papers are fetched daily from arXiv using the `daily_arxiv.py` script
2. Once a month, the `archive_old_papers.py` script runs to:
   - Identify papers older than 365 days
   - Move these papers from the main collection to monthly archive files
   - Generate markdown files for easier browsing of archived papers
   - Update the main collection by removing the archived papers

## Browsing Archived Papers

Archived papers are available in the [archive directory](./archive/index.md). They are organized by the month they were archived, with each archive file containing papers moved during that specific month.

## Archive Configuration

You can configure archive settings in the `config.yaml` file:

```yaml
archive_settings:
  enabled: True
  max_age_days: 365  # Papers older than this will be archived (1 year)
  archive_dir: './docs/archive'
```

- `enabled`: Enable or disable the archiving feature
- `max_age_days`: Papers older than this number of days will be archived
- `archive_dir`: Directory where archived papers will be stored

## Manual Archive Management

If you need to manually run the archiving process, you can:

1. Run it locally:
   ```bash
   python archive_old_papers.py
   ```

2. Trigger the GitHub Action workflow manually from the Actions tab

## Implementation Details

The archive system consists of:

1. `archive_old_papers.py`: The main archiving script
2. `archive-old-papers.yml`: GitHub workflow that runs monthly
3. Archive configuration in `config.yaml`
4. Archive directory structure in `docs/archive/`

The script parses paper dates, identifies old papers, moves them to archive files, and generates markdown for browsing.