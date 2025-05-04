# Daily arXiv

[![MIT License][license-shield]][license-url]
[![Python 3.11+][python-shield]][python-url]

> **Automated daily arXiv paper aggregator**

A Python tool that automatically fetches, filters, and formats the latest research papers from arXiv. Features email notifications and comprehensive paper management.

## ✨ Features

- 🔄 **Automated Daily Updates**: Runs daily via GitHub Actions
- 📧 **Email Notifications**: Get daily summaries delivered to your inbox
- 🔍 **Smart Filtering**: Advanced keyword filtering across multiple research domains
- 📊 **Multiple Output Formats**: Markdown, JSON, and web-ready formats
- 📚 **Paper Archiving**: Automatic management of historical papers
- 🔗 **Code Discovery**: Automatic GitHub repository detection for papers

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

```bash
# Clone the repository
git clone https://github.com/AlanSynn/daily-arxiv.git
cd daily-arxiv

# Install dependencies
uv sync

# Or with pip
pip install -e .
```

### Configuration

1. Edit the configuration file:

```bash
# Basic settings are already configured in config.yaml
# You can customize research categories and filters there
```

2. Set up email credentials (optional):

```bash
export SMTP_USER="your-email@gmail.com"
export SMTP_PASSWORD="your-app-password"
export EMAIL_RECIPIENT="recipient@email.com"
```

### Usage

```bash
# Fetch daily papers
uv run python -m src.daily_arxiv.daily_arxiv

# Send email notifications
uv run python -m src.daily_arxiv.daily_arxiv --send-email

# Fresh run (clear existing data)
uv run python -m src.daily_arxiv.daily_arxiv --fresh-run

# Custom configuration
uv run python -m src.daily_arxiv.daily_arxiv --config_path your_config.yaml
```

## 📋 Command Line Options

```bash
Options:
  -h, --help            Show help message
  --config_path PATH    Configuration file path
  --update_paper_links  Update paper links and GitHub repositories
  --fresh-run          Reset all JSON files before running
  --send-email         Send email with today's papers
  --email-recipient    Email recipient (overrides config)
  --smtp-user          SMTP username (overrides config)
  --smtp-password      SMTP password (overrides config)
```

## 📁 Output Structure

All outputs are stored in the `logs/` directory:

```
logs/
├── ARXIV_PAPERS.md          # Main paper listing (latest results)
├── daily-arxiv.json         # JSON data
├── daily-arxiv-web.json     # Web-ready JSON data
├── arxiv-web.md             # Web-ready markdown
├── json/                    # Daily JSON logs
│   └── daily-arxiv_YYYY-MM-DD.json
├── md/                      # Daily markdown logs
│   └── daily-arxiv_YYYY-MM-DD.md
└── archive/                 # Archived papers
    └── archive_YYYYMM.json
```

## ⚙️ Configuration

The `config.yaml` file allows you to customize:

- **Search Keywords**: Define research categories and filter terms
- **Email Settings**: SMTP configuration for notifications
- **Output Settings**: File paths and formatting options
- **API Settings**: arXiv API parameters and rate limiting

Example configuration:

```yaml
# Basic settings
max_results: 30
base_url: "https://arxiv.paperswithcode.com/api/v0/papers/"

# Email configuration
email_settings:
  enabled: true
  smtp_server: "smtp.gmail.com"
  smtp_port: 587
  smtp_user: "${SMTP_USER}"
  smtp_password: "${SMTP_PASSWORD}"

# Research categories
keywords:
  "Computational Design":
    filters:
      - "Computational Design"
      - "Generative Design"
```

## 🔄 Automation

### GitHub Actions

The project includes automated workflows:

- **Daily Updates**: Runs every day at 12:00 UTC
- **Paper Archiving**: Weekly cleanup of old papers
- **Email Notifications**: Optional daily email summaries

### Local Automation

Set up a cron job for local automation:

```bash
# Edit crontab
crontab -e

# Add daily execution at 9 AM
0 9 * * * cd /path/to/daily-arxiv && uv run python -m src.daily_arxiv.daily_arxiv --send-email
```

## 🧪 Testing

```bash
# Run all tests
uv run pytest

# Run specific test categories
uv run pytest tests/test_basic_functionality.py -v

# Run test script
./scripts/run_tests.sh
```

## 📚 Research Categories

The tool currently covers these research domains:

- **Computational Design & Fabrication**: Generative design, computational fabrication
- **Mechanics, Kinematics & Motion Synthesis**: Mechanism design, physics-based simulation
- **Robotics**: Robot design, control, learning, and simulation
- **Human-Computer Interaction**: Interactive design systems, VR/AR for design
- **Generative AI**: Foundation models, LLMs, and diffusion models in design

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 👤 Author

**Alan Synn**

- Email: alan@alansynn.com
- GitHub: [@AlanSynn](https://github.com/AlanSynn)

## 🙏 Acknowledgments

- [arXiv](https://arxiv.org/) for providing access to research papers
- [Papers With Code](https://paperswithcode.com/) for enhanced paper metadata
- The research community for continuously pushing the boundaries of knowledge

<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: https://img.shields.io/github/license/AlanSynn/daily-arxiv.svg?style=for-the-badge
[license-url]: https://github.com/AlanSynn/daily-arxiv/blob/main/LICENSE
[python-shield]: https://img.shields.io/badge/python-3.11+-blue.svg?style=for-the-badge
[python-url]: https://www.python.org/downloads/