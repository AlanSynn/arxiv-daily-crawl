# Paper Archive System

This document explains the paper archiving system of the arxiv-digest project.

## Overview

arxiv-digest automatically collects and organizes papers from arXiv. To keep the
main collection current and relevant, papers older than 1 year are automatically
archived.

## How the Archive Works

1. Papers are fetched daily from arXiv by the `src.arxiv_digest` pipeline
2. The archiver (`src.arxiv_digest.archive`) runs monthly via GitHub Actions and
   is also invoked by the daily workflow:
   - Identify papers older than 365 days
   - Move these papers from the main collection to monthly archive files
   - Generate markdown files for easier browsing of archived papers
   - Update the main collection by removing the archived papers

## Browsing Archived Papers

Archived papers live in [`logs/archive/`](../logs/archive/), organized by the
month they were archived. Each `archive_YYYYMM.{json,md}` pair contains the
papers moved during that specific month.

## Archive Configuration

Configure archive settings in `config.yaml`:

```yaml
archive_settings:
  enabled: True
  max_age_days: 365  # Papers older than this will be archived (1 year)
  archive_dir: './logs/archive'
```

- `enabled`: Enable or disable the archiving feature
- `max_age_days`: Papers older than this number of days will be archived
- `archive_dir`: Directory where archived papers will be stored

## Manual Archive Management

If you need to manually run the archiving process, you can:

1. Run it locally:
   ```bash
   uv run python -m src.arxiv_digest.archive
   ```

2. Trigger the "Archive Old Papers Monthly" workflow manually from the
   GitHub Actions tab

## Implementation Details

The archive system consists of:

1. `src/arxiv_digest/archive/archiver.py`: the archiver module
2. `.github/workflows/archive-old-papers.yml`: the monthly GitHub Actions workflow
3. Archive configuration in `config.yaml`
4. Archive directory structure in `logs/archive/`

The archiver parses paper dates, identifies old papers, moves them to archive
files, and generates markdown for browsing.
