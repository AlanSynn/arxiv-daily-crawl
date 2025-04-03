#!/bin/bash

# Check if environment variables are set, otherwise prompt for them
if [ -z "$SMTP_USER" ]; then
  read -p "Enter SMTP username (email): " SMTP_USER
  export SMTP_USER
fi

if [ -z "$SMTP_PASSWORD" ]; then
  read -s -p "Enter SMTP password: " SMTP_PASSWORD
  echo
  export SMTP_PASSWORD
fi

if [ -z "$EMAIL_RECIPIENT" ]; then
  read -p "Enter email recipient: " EMAIL_RECIPIENT
  export EMAIL_RECIPIENT
fi

# Backup existing files
echo "Backing up existing files..."
mkdir -p backup
cp docs/cv-arxiv-daily.json backup/ 2>/dev/null || true
cp docs/cv-arxiv-daily-web.json backup/ 2>/dev/null || true
cp docs/cv-arxiv-daily-wechat.json backup/ 2>/dev/null || true
cp README.md backup/ 2>/dev/null || true
cp docs/index.md backup/ 2>/dev/null || true
cp docs/wechat.md backup/ 2>/dev/null || true

# Run with fresh-run flag and email notification
echo "Running fresh start..."
python daily_arxiv.py --fresh-run --send-email

# Run archive to clean up old papers
echo "Running archive to clean old papers..."
python archive_old_papers.py

echo "Done! Fresh run completed."
echo "Email notification has been sent if properly configured in config.yaml."