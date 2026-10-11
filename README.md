# arxiv-digest

[![License][license-shield]][license-url]
[![Python 3.11+][python-shield]][python-url]

> **A personal, curated arXiv digest — delivered as a daily email.**

arxiv-digest watches your research areas on arXiv (plus Hugging Face's
community-curated Daily Papers), scores every match against your own
keywords, and emails you a ranked shortlist each day — not a raw dump.
Papers are deduplicated across runs, so you see each one at most once, and
everything is archived to browsable markdown.

## ✨ What you get

- 📧 **Daily arXiv Digest email** — sections per research area, sorted by
  relevance score, with a "TOP 5 BY RELEVANCE" block and per-paper score
  badges
- 🔍 **Your keywords, your weights** — categories map arXiv category codes to
  include/exclude keywords (`ti:` prefix for title-only matching); the
  relevance scorer ranks every match
- 🔥 **Trending on HuggingFace** — the day's community-upvoted papers
  (upvote floor + top-N) as their own section
- 🔁 **At-most-once delivery** — a persistent notified-store means weekend
  stalls never re-send Thursday's papers
- 🔗 **Code discovery** — GitHub repos auto-resolved for each paper via the
  HF Papers API
- 📚 **Full archive** — dated snapshots, a flat `PAPER_LIST.md`, and a
  monthly 1-year archive, all committed to the `results` branch
- 🤖 **Fully automated** — GitHub Actions runs the whole pipeline daily at
  15:00 UTC (after both arXiv's overnight postings and HF's ~13:00 UTC
  publish)

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)

### Installation

```bash
git clone https://github.com/AlanSynn/arxiv-digest.git
cd arxiv-digest
uv sync
```

### Configuration

Everything you track lives in [`config.yaml`](config.yaml):

```yaml
categories:
  - name: "Character Motion Synthesis & Animation"
    cat_codes: ["cs.GR", "cs.CV"]        # arXiv categories to search
    priority: 9                          # section ordering (higher = earlier)
    include_keywords:                    # abstract matches
      - "motion synthesis"
      - "ti:character motion"            # ti: = title-only (higher precision)
    exclude_keywords:                    # whole-word penalty, e.g. "sport"
      - "motion planning"                # (never fires on "transport")

scoring:
  threshold: 0.15
  title_weight: 2.0
  include_boost: 1.0
  exclude_penalty: 1.0
```

Email settings use environment variables — no secrets in the repo:

```bash
export SMTP_USER="your-email@gmail.com"      # Gmail: use an app password
export SMTP_PASSWORD="your-app-password"
export EMAIL_RECIPIENT="you@example.com"
```

### Usage

```bash
# Fetch + score + update the local archive (no email)
uv run python -m src.arxiv_digest

# Full run: fetch, score, and send the digest email
uv run python -m src.arxiv_digest --send-email

# Reset accumulated JSON state first
uv run python -m src.arxiv_digest --fresh-run

# Installed console scripts (after `uv sync`)
uv run arxiv-digest --help
uv run archive-papers --help

# Preview the email HTML with mock papers (no network, no send)
PYTHONPATH=. uv run python scripts/generate_email_preview.py
```

## 🤖 Running on GitHub Actions (forks)

The repo ships three workflows: a daily run (`daily-arxiv.yml`, 15:00 UTC), a
monthly archive (`archive-old-papers.yml`), and state persistence — every run
commits `logs/` (snapshots + dedup state) to the `results` branch.

To run your own copy:

1. **Add repository secrets** (Settings → Secrets and variables → Actions):
   - `SMTP_USER`, `SMTP_PASSWORD`, `EMAIL_RECIPIENT`
2. **Allow workflow pushes** — the workflows declare
   `permissions: contents: write`; if your fork restricts the default
   `GITHUB_TOKEN`, set Settings → Actions → General → Workflow permissions to
   "Read and write".
3. Push to `main` and trigger **Run Daily Arxiv** manually once to create the
   `results` branch.

If a required secret is missing the run **fails loudly** (non-zero exit) —
it never silently skips your digest.

## 📋 Command Line Options

```
-h, --help            Show help message
--config_path PATH    Configuration file path (default: config.yaml)
--fresh-run           Reset all JSON files before running
--send-email          Send the digest email
--email-recipient ADDR  Override recipient
--smtp-user / --smtp-password  Override SMTP credentials
```

## 📁 Outputs (`logs/`)

| Path | Content |
|---|---|
| `ARXIV_PAPERS.md` / `arxiv-web.md` | accumulated collection, grouped by category |
| `daily-arxiv*.json` / dated `logs/json`, `logs/md` | per-day snapshots |
| `PAPER_LIST.md` | flat, deduplicated, newest-first list |
| `notified_papers.json` | dedup state (emailed paper keys) |
| `archive/archive_YYYYMM.*` | monthly archive of >1-year-old papers |

All of the above live on the `results` branch via the daily workflow.

## 🧪 Development

```bash
uv run pytest              # full test suite
uv run ruff check src      # lint
```

## 📄 License

Distributed under the Apache License 2.0. See `LICENSE` and `NOTICE` for
more information.

## 🙏 Acknowledgments

- Started from [Vincentqyw/cv-arxiv-daily](https://github.com/Vincentqyw/cv-arxiv-daily) (Apache-2.0)
- [arXiv](https://arxiv.org/) for open access to research
- [Hugging Face Daily Papers](https://huggingface.co/papers) for community curation

<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: https://img.shields.io/github/license/AlanSynn/arxiv-digest.svg?style=for-the-badge
[license-url]: https://github.com/AlanSynn/arxiv-digest/blob/main/LICENSE
[python-shield]: https://img.shields.io/badge/python-3.11+-blue.svg?style=for-the-badge
[python-url]: https://www.python.org/downloads/
