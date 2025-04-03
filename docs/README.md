# 📚 Daily Arxiv

A tool that automatically collects and organizes the latest research papers from arXiv, making it easy to stay updated with cutting-edge research.

## 🚀 Features

- **Automated Collection**: Fetches the latest papers from arXiv daily
- **Multiple Categories**: Covers various research domains like Computer Vision, Machine Learning, and more
- **Email Notifications**: Sends beautiful, emoji-enhanced email updates with the latest papers
- **Automatic Archiving**: Archives older papers to maintain a clean, focused view of recent research
- **Daily Logs**: Generates log files to track updates and troubleshoot issues
- **GitHub Integration**: Generates GitHub Pages to provide a beautiful web interface

## 📋 Configuration

The project is configured through `config.yaml`. Here are the key configuration options:

```yaml
repo_name: "daily-arxiv"
repo_url: "https://github.com/yourusername/daily-arxiv"
categories:
  - "cs.CV"    # Computer Vision
  - "cs.LG"    # Machine Learning
  - "cs.AI"    # Artificial Intelligence
  - "cs.CL"    # Computation and Language
email:
  enabled: true
  sender: "your-email@example.com"
  receiver: "recipient@example.com"
log_dir: "./logs"  # Directory for storing log files
```

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/daily-arxiv.git
cd daily-arxiv

# Install dependencies
pip install -r requirements.txt

# Set up the logs directory
./setup_logs.sh
```

## 📝 Usage

### Running manually

```bash
# Normal run
python daily_arxiv.py

# Fresh run (resets JSON files)
python daily_arxiv.py --fresh-run
# or
./fresh_run.sh
```

### Scheduled runs with GitHub Actions

The project is configured to run automatically once a day using GitHub Actions. The workflow configuration is in `.github/workflows/daily-arxiv.yml`.

## 📦 Directory Structure

```
daily-arxiv/
├── daily_arxiv.py           # Main script
├── archive_old_papers.py    # Script for archiving papers
├── config.yaml              # Configuration file
├── requirements.txt         # Python dependencies
├── setup_logs.sh            # Script to set up logging
├── fresh_run.sh             # Script to perform a fresh run
├── docs/                    # Documentation and output files
│   ├── README.md            # Generated README with papers
│   ├── daily-arxiv.json     # JSON data for README
│   ├── daily-arxiv-web.json # JSON data for web page
│   ├── archive/             # Archived older papers
│   └── index.md             # Generated web page
└── logs/                    # Log files directory
    └── README.md            # Log directory documentation
```

## 📧 Email Notifications

When enabled, the system sends attractive emails with emojis containing the latest papers. Configure your email settings in `config.yaml` and set up the required environment variables:

- `SMTP_SERVER`: Your SMTP server (e.g., smtp.gmail.com)
- `SMTP_PORT`: SMTP port (e.g., 587)
- `SMTP_USERNAME`: Your email username
- `SMTP_PASSWORD`: Your email password or app password

## 📊 Logging

Detailed logs are generated in the `logs` directory. Each run creates a new log file with a timestamp, making it easy to track updates and troubleshoot issues.

## 🗄️ Archiving

Papers older than one year are automatically archived to keep the main list focused on recent research. Archived papers are stored in the `docs/archive` directory in both JSON and Markdown formats.

## 🔄 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
