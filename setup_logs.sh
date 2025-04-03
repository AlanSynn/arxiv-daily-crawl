#!/bin/bash

# This script sets up the required directory structure for logs

echo "Setting up log directory structure..."

# Create main log directory
mkdir -p logs/json
mkdir -p logs/md

# Create .gitkeep files to ensure directories are committed to git
touch logs/json/.gitkeep
touch logs/md/.gitkeep

# Create logs README
cat > logs/README.md << 'EOL'
# Daily Arxiv Log Files

This directory contains daily logs of papers collected by the Daily Arxiv system.

## Directory Structure

- `json/`: Contains JSON data files for each day's collection
- `md/`: Contains Markdown files generated from the JSON data

Each file is named with the date format `YYYY-MM-DD`.

## Using Log Files

These logs provide a historical record of papers collected each day. You can:

1. Browse past collections by date
2. Track which papers were discovered on which dates
3. Recover data in case of issues with the main files

## Retention Policy

Log files are kept indefinitely unless manually purged.
EOL

echo "Log directory structure created successfully."
echo "To initialize, run: './setup_logs.sh'"

# This script sets up the required directory structure for logs

echo "Setting up log directory structure..."

# Create main log directory
mkdir -p logs/json
mkdir -p logs/md

# Create .gitkeep files to ensure directories are committed to git
touch logs/json/.gitkeep
touch logs/md/.gitkeep

# Create logs README
cat > logs/README.md << 'EOL'
# Daily Arxiv Log Files

This directory contains daily logs of papers collected by the Daily Arxiv system.

## Directory Structure

- `json/`: Contains JSON data files for each day's collection
- `md/`: Contains Markdown files generated from the JSON data

Each file is named with the date format `YYYY-MM-DD`.

## Using Log Files

These logs provide a historical record of papers collected each day. You can:

1. Browse past collections by date
2. Track which papers were discovered on which dates
3. Recover data in case of issues with the main files

## Retention Policy

Log files are kept indefinitely unless manually purged.
EOL

echo "Log directory structure created successfully."
echo "To initialize, run: './setup_logs.sh'"