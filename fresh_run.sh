#!/bin/bash

# Create backups directory
mkdir -p backups

# Get current timestamp for backup files
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Back up existing files before fresh run
if [ -f "README.md" ]; then
  cp README.md "backups/README_${TIMESTAMP}.md"
  echo "Backed up README.md to backups/README_${TIMESTAMP}.md"
fi

if [ -f "docs/index.md" ]; then
  cp docs/index.md "backups/index_${TIMESTAMP}.md"
  echo "Backed up docs/index.md to backups/index_${TIMESTAMP}.md"
fi

if [ -f "docs/daily-arxiv.json" ]; then
  cp docs/daily-arxiv.json "backups/daily-arxiv_${TIMESTAMP}.json"
  echo "Backed up docs/daily-arxiv.json to backups/daily-arxiv_${TIMESTAMP}.json"
fi

if [ -f "docs/daily-arxiv-web.json" ]; then
  cp docs/daily-arxiv-web.json "backups/daily-arxiv-web_${TIMESTAMP}.json"
  echo "Backed up docs/daily-arxiv-web.json to backups/daily-arxiv-web_${TIMESTAMP}.json"
fi

# Check if we need to prompt for email settings
if [ -z "$SMTP_USER" ] || [ -z "$SMTP_PASSWORD" ] || [ -z "$EMAIL_RECIPIENT" ]; then
  echo "Email settings not found in environment. Would you like to configure email notifications? (y/n)"
  read configure_email

  if [ "$configure_email" = "y" ] || [ "$configure_email" = "Y" ]; then
    if [ -z "$SMTP_USER" ]; then
      echo "Enter SMTP username (email address):"
      read SMTP_USER
      export SMTP_USER
    fi

    if [ -z "$SMTP_PASSWORD" ]; then
      echo "Enter SMTP password or app password:"
      read -s SMTP_PASSWORD
      export SMTP_PASSWORD
      echo
    fi

    if [ -z "$EMAIL_RECIPIENT" ]; then
      echo "Enter email recipient address:"
      read EMAIL_RECIPIENT
      export EMAIL_RECIPIENT
    fi

    SEND_EMAIL="--send-email"
  else
    SEND_EMAIL=""
  fi
else
  # Email settings found in environment
  SEND_EMAIL="--send-email"
fi

# Run the script with fresh-run flag
echo "Starting fresh run of Daily Arxiv..."
python3 daily_arxiv.py --fresh-run $SEND_EMAIL

echo "Fresh run completed!"