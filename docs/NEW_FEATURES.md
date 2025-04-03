# New Features for Daily Arxiv

## 1. Fresh Run Option (`--fresh-run`)

This feature allows you to completely reset all JSON files and start collecting papers from scratch. This is useful when:
- You want to change your keywords and start fresh
- There are issues with the existing data
- You want to rebuild the entire collection

### Usage

```bash
# Run from command line
python daily_arxiv.py --fresh-run

# Or use the convenient script
./fresh_run.sh
```

The `fresh_run.sh` script will:
1. Back up your existing files to a `backup/` directory
2. Run daily_arxiv.py with the `--fresh-run` flag
3. Run the archive_old_papers.py script to organize papers

## 2. Email Notifications

Daily Arxiv now supports email notifications! When configured, the system will send a beautiful HTML email containing the latest papers fetched from arXiv with:

- 📝 Clean, modern design with emojis
- 📚 Papers organized by topic category
- 📄 Direct links to papers and source code
- 📋 Abstracts included for quick review

To configure email notifications:

1. Edit `config.yaml` and set `send_email: True`
2. Configure `email_settings` with your SMTP server details:
   ```yaml
   email_settings:
     enabled: True
     smtp_server: "smtp.gmail.com"
     smtp_port: 587
     smtp_user: "${SMTP_USER}"  # Uses environment variable
     smtp_password: "${SMTP_PASSWORD}"  # Uses environment variable
   ```
3. Set `email_recipient: "${EMAIL_RECIPIENT}"` to specify who receives the notifications

For GitHub Actions, add these as repository secrets.

### Usage

```bash
# To send an email with today's papers
python daily_arxiv.py --send-email

# You can also specify a different recipient
python daily_arxiv.py --send-email --email-recipient someone@example.com
```

The default recipient is `alansynn@gatech.edu` but you can change it with the `--email-recipient` argument.

## 3. Paper Archiving

Old papers are now automatically archived to keep the main view focused on recent research:

- 🗄️ Papers older than 365 days are moved to archive files
- 📚 Archives are organized by month in `docs/archive`
- 📑 Each archive includes full paper details and abstracts

### Configuration

Edit the `config.yaml` file to configure archiving:

```yaml
# archive settings
archive_settings:
  enabled: True  # Enable/disable archiving
  max_age_days: 365  # Papers older than this will be archived (1 year)
  archive_dir: './docs/archive'  # Where to store archives
```

### Usage

The archiving process runs automatically with the daily update. You can also run it manually:

```bash
python archive_old_papers.py
```

Archives can be browsed in the `docs/archive/` directory.

## 4. Daily Logs

Daily Arxiv now generates daily log files to make tracking and recovery easier. The system will:

- 📂 Create a new log file each day (both JSON and MD formats)
- 🗃️ Store previous files in `logs/json` and `logs/md` directories
- 📊 Maintain a history of all papers collected

Example directory structure:
```
logs/
├── README.md
├── json/
│   ├── daily-arxiv_2023-07-01.json
│   ├── daily-arxiv_2023-07-02.json
│   ├── daily-arxiv-web_2023-07-01.json
│   └── daily-arxiv-web_2023-07-02.json
└── md/
    ├── README_2023-07-01.md
    ├── README_2023-07-02.md
    ├── index_2023-07-01.md
    └── index_2023-07-02.md
```

## 5. GitHub Secrets 사용하기 (민감한 정보 보호)

민감한 정보(SMTP 인증 정보, 이메일 주소 등)는 GitHub Secrets를 통해 안전하게 관리됩니다.

### GitHub Secrets 설정 방법

1. GitHub 저장소로 이동하여 **Settings** 탭을 클릭합니다.
2. 왼쪽 메뉴에서 **Secrets and variables** → **Actions**를 선택합니다.
3. **New repository secret** 버튼을 클릭하여 다음 비밀을 추가합니다:
   - `SMTP_USER`: 이메일 발송에 사용할 SMTP 사용자 이름(이메일 주소)
   - `SMTP_PASSWORD`: SMTP 비밀번호 또는 앱 비밀번호
   - `EMAIL_RECIPIENT`: 알림을 받을 이메일 주소

![GitHub Secrets 설정](https://docs.github.com/assets/cb-45016/mw-1440/images/help/actions/add-repository-secret.webp)

### 로컬에서 실행 시

로컬에서 실행할 때는 환경 변수를 설정하거나 명령줄 인수를 사용할 수 있습니다:

```bash
# 환경 변수 사용
export SMTP_USER="your-email@gmail.com"
export SMTP_PASSWORD="your-app-password"
export EMAIL_RECIPIENT="recipient@example.com"
python daily_arxiv.py --send-email

# 또는 명령줄 인수 사용
python daily_arxiv.py --send-email --smtp-user "your-email@gmail.com" --smtp-password "your-app-password" --email-recipient "recipient@example.com"
```

`fresh_run.sh` 스크립트는 환경 변수가 설정되어 있지 않으면 대화형으로 필요한 정보를 입력받습니다.