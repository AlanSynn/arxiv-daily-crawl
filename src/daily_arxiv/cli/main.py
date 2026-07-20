"""Main CLI entry point for daily-arxiv.

Orchestrates the Wave 1 data API into the output layer:

1. ``load_config`` -> rich config (categories, scoring, rate_limit, toc).
2. ``make_client`` builds ONE shared ``arxiv.Client`` (enforces the >=3s
   rate limit for the whole run).
3. For each category: ``fetch_category`` -> ``RelevanceScorer.score`` ->
   threshold filter -> ``CodeLinkClient.get_code_url`` for survivors.
4. Build the legacy ``{category: {paper_key: row_str}}`` dicts consumed by
   ``FileManager`` / ``EmailService`` / the archiver.
5. Render outputs: dated JSON, ``ARXIV_PAPERS.md`` (with TOC), ``arxiv-web.md``,
   and the flat ``PAPER_LIST.md``.
6. Optional email of the most-recent-day slice.

Dedup policy: a paper MAY appear in several category sections of
``ARXIV_PAPERS.md`` (matches reader intent), but in ``PAPER_LIST.md`` it
appears once (highest-``score`` occurrence).
"""

import argparse
import datetime
import logging
from typing import Any, Callable, Dict, List, Set, Tuple

from ..core.config import load_config, validate_config
from ..models.paper import Paper
from ..processors.content_generator import ContentGenerator
from ..processors.file_manager import FileManager
from ..processors.notified_store import load_notified, save_notified
from ..processors.relevance import RelevanceScorer
from ..processors.toc_generator import generate_paper_list, generate_toc
from ..services.arxiv_client import ArXivClient, filter_recent_day, make_client
from ..services.code_link_client import CodeLinkClient
from ..services.email_service import EmailService
from ..utils.date_utils import get_dated_file_paths


class DailyArxivApp:
    """Main application class for daily-arxiv."""

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the application with configuration.

        Args:
            config: Configuration dictionary (output of :func:`load_config`).
        """
        self.config = config
        self.arxiv_client = ArXivClient()
        self.email_service = EmailService(config)
        self.file_manager = FileManager()
        self.content_generator = ContentGenerator()

    def run(self):
        """Run the main application logic."""
        logging.info("Starting daily arXiv paper collection")
        config = self.config

        # Fresh run: clear accumulated JSON state first.
        if config.get('fresh_run', False):
            logging.info("Fresh run requested. Resetting all JSON files.")
            self.file_manager.reset_json_files(config)

        rate_limit = config['rate_limit']
        scoring = config['scoring']
        toc_cfg = config['toc']

        # One shared arXiv client enforces rate-limiting for the whole run.
        client = make_client(rate_limit)
        scorer = RelevanceScorer(scoring)
        code_link = CodeLinkClient(
            rate_limit.code_link_enabled,
            rate_limit.code_link_delay_seconds,
        )

        max_results = int(config.get('max_results', 30))
        # Freshness window for fetches; not in config by default -> 14 days.
        max_age_days = int(config.get('fetch_max_age_days', 14))

        # Per-category survivors (a paper may legitimately appear in more than
        # one section) plus a global best-score view for the flat paper list.
        category_papers: Dict[str, List[Paper]] = {}
        seen_best: Dict[str, Paper] = {}

        for category in config['categories']:
            papers = self.arxiv_client.fetch_category(
                category, max_results, max_age_days, client
            )

            section_papers: List[Paper] = []
            for paper in papers:
                score, matched = scorer.score(paper, category)
                paper.score = score
                paper.matched_keywords = matched
                paper.category = category.name

                if score < scoring.threshold:
                    continue

                # Only spend a code-link API call on papers that survived.
                if rate_limit.code_link_enabled:
                    paper.code_url = code_link.get_code_url(paper.paper_key)

                section_papers.append(paper)

                # Track the highest-score occurrence per paper_key globally.
                prev = seen_best.get(paper.paper_key)
                if prev is None or paper.score > prev.score:
                    seen_best[paper.paper_key] = paper

            category_papers[category.name] = section_papers
            logging.info(
                "Category %r: %d papers survived scoring",
                category.name, len(section_papers),
            )

        # Deduplicated global view (one entry per paper_key, best score).
        all_scored: List[Paper] = list(seen_best.values())

        # Legacy {category: {paper_key: row_str}} dicts.
        main_data = self._rows_by_category(category_papers, Paper.to_md_row)
        main_data_web = self._rows_by_category(category_papers, Paper.to_web_row)

        most_recent_date = max(
            (p.published for p in all_scored), default=None
        )

        # Email slice: only papers from the most recent published day.
        # ``email_papers_by_cat`` feeds the Dispatch renderer directly.
        email_papers = filter_recent_day(all_scored, window_days=1)
        email_papers_by_cat: Dict[str, List[Paper]] = {}
        for paper in email_papers:
            email_papers_by_cat.setdefault(paper.category or "", []).append(paper)

        # Cross-run dedup: drop papers already dispatched in a prior run so
        # each paper is emailed at most once.  Guards against the newest-day
        # stall on weekends (no new arXiv posts -> same slice 3 days running)
        # re-sending the same batch every day.
        dedup_cfg = self.config.get("email_dedup") or {}
        dedup_enabled = bool(dedup_cfg.get("enabled", True))
        notified_path = dedup_cfg.get(
            "state_path", "./logs/notified_papers.json"
        )
        dedup_max_age = int(dedup_cfg.get("max_age_days", 30))
        delta_keys: Set[str] = set()
        if dedup_enabled:
            notified = load_notified(notified_path)
            email_papers_by_cat, delta_keys = self._dedupe_email_slice(
                email_papers_by_cat, notified
            )

        if not main_data:
            logging.warning(
                "No papers passed the relevance filter; nothing to write."
            )
            return

        # TOC block (readme markdown only, gated on toc.enabled).
        toc_block = ""
        if toc_cfg.enabled:
            cats_with_papers = [
                (name, papers)
                for name, papers in category_papers.items()
                if papers
            ]
            toc_block = generate_toc(cats_with_papers, datetime.date.today())

        # Main (non-dated) output files.
        self._update_main_files(main_data, main_data_web, toc_block)

        # Dated snapshot files (filename keyed on most-recent paper date).
        self._update_daily_logs(
            main_data, main_data_web, most_recent_date, toc_block
        )

        # Flat paper list (always written; independent of inline TOC).
        paper_list_md = generate_paper_list(all_scored)
        self.file_manager.write_paper_list(paper_list_md, toc_cfg.paper_list_path)

        # Email the most-recent-day slice if requested. After a successful
        # send, record the dispatched keys so they are never re-emailed.
        if config.get('send_email', False) and email_papers_by_cat:
            sent = self._send_email_notification(
                email_papers_by_cat, most_recent_date
            )
            if sent and dedup_enabled and delta_keys:
                combined = load_notified(notified_path) | delta_keys
                save_notified(
                    notified_path, combined, max_age_days=dedup_max_age
                )
        elif config.get('send_email', False):
            logging.info(
                "No new papers since last dispatch; email skipped."
            )

        logging.info("Daily arXiv collection completed")

    @staticmethod
    def _rows_by_category(
        category_papers: Dict[str, List[Paper]],
        row_fn: Callable[[Paper], str],
    ) -> Dict[str, Dict[str, str]]:
        """Build the legacy ``{category: {paper_key: row_str}}`` shape.

        ``row_fn`` selects the row serializer (``Paper.to_md_row`` for the
        readme/JSON, ``Paper.to_web_row`` for the web/email).
        """
        out: Dict[str, Dict[str, str]] = {}
        for category, papers in category_papers.items():
            if not papers:
                continue
            out[category] = {p.paper_key: row_fn(p) for p in papers}
        return out

    def _update_main_files(
        self, data: Dict, data_web: Dict, toc_block: str = ""
    ):
        """Update main JSON and markdown files with all scored data.

        ``json_readme_path`` holds pipe-delimited rows (archiver-friendly);
        ``json_gitpage_path`` holds the web/email row variant.
        """
        json_readme = self.config.get('json_readme_path')
        json_gitpage = self.config.get('json_gitpage_path')

        if json_readme:
            self.file_manager.update_json_file(json_readme, [data])
        if json_gitpage:
            self.file_manager.update_json_file(json_gitpage, [data_web])

        # Markdown renderings.
        if json_readme and self.config.get('md_readme_path'):
            self.content_generator.json_to_md(
                json_readme, self.config['md_readme_path'],
                task="Generate readme markdown",
                to_web=False,
                show_badge=self.config.get('show_badge', True),
                toc_block=toc_block,
            )
        if json_gitpage and self.config.get('md_gitpage_path'):
            self.content_generator.json_to_md(
                json_gitpage, self.config['md_gitpage_path'],
                task="Generate web markdown",
                to_web=True,
                show_badge=self.config.get('show_badge', True),
            )

    def _update_daily_logs(
        self, data: Dict, data_web: Dict, paper_date=None, toc_block: str = ""
    ):
        """Update dated log files (filename keyed on most-recent paper date)."""
        # Use the paper date if provided, otherwise fall back to today.
        date_str = paper_date.strftime("%Y-%m-%d") if paper_date else None

        dated_paths = get_dated_file_paths(self.config, date_str)
        self.file_manager.update_json_file(
            dated_paths['json_path'], [data], create_new=True
        )
        self.content_generator.json_to_md(
            dated_paths['json_path'], dated_paths['md_path'],
            task="Generate daily log", create_new=True, toc_block=toc_block,
        )

        # Web log files.
        self.file_manager.update_json_file(
            dated_paths['json_web_path'], [data_web], create_new=True
        )
        self.content_generator.json_to_md(
            dated_paths['json_web_path'], dated_paths['md_web_path'],
            task="Generate daily web log", create_new=True, to_web=True,
        )

    @staticmethod
    def _dedupe_email_slice(
        papers_by_category: Dict[str, List[Paper]],
        notified: Set[str],
    ) -> Tuple[Dict[str, List[Paper]], Set[str]]:
        """Drop already-notified papers from the email slice.

        Returns ``(deduped_by_category, delta_keys)`` where ``delta_keys`` is
        the set of paper keys that survived (i.e. the freshly-emailable ones
        to record after a successful send).  Empty categories are removed so
        an all-already-notified slice collapses to ``{}`` and the caller skips
        the send entirely.
        """
        deduped: Dict[str, List[Paper]] = {}
        delta: Set[str] = set()
        dropped = 0
        for cat, papers in papers_by_category.items():
            fresh: List[Paper] = []
            for paper in papers:
                if paper.paper_key in notified:
                    dropped += 1
                    continue
                fresh.append(paper)
                delta.add(paper.paper_key)
            if fresh:
                deduped[cat] = fresh
        if dropped:
            logging.info(
                "Email dedup: %d already-dispatched paper(s) dropped.", dropped
            )
        return deduped, delta

    def _send_email_notification(
        self, papers_by_category: Dict[str, List[Paper]], paper_date=None
    ) -> bool:
        """Send the Dispatch email with the most-recent-day papers.

        Builds the ``stats`` dict (total / categories / threshold) from the
        caller's slice and delegates to :meth:`EmailService.render_email`.
        Returns ``True`` on a successful send so the caller can record the
        dispatched keys (never record on failure — failed sends must retry).
        """
        recipient = self.config.get('email_recipient')
        if not recipient:
            logging.warning("No email recipient configured")
            return False

        # Use the paper date if provided, otherwise fall back to today.
        if paper_date:
            date_str = paper_date.strftime("%Y-%m-%d")
        else:
            date_str = datetime.date.today().strftime("%Y-%m-%d")

        threshold = float(self.config.get('scoring', {}).get('threshold', 0.15))
        stats = {
            "total": sum(len(v) for v in papers_by_category.values()),
            "categories": sum(1 for v in papers_by_category.values() if v),
            "threshold": threshold,
        }

        subject = f"Daily arXiv Dispatch — {date_str}"
        html_content = self.email_service.render_email(
            papers_by_category, date_str, stats
        )

        success = self.email_service.send_email(recipient, subject, html_content)
        if success:
            logging.info("Email notification sent successfully")
        else:
            logging.error("Failed to send email notification")
        return success


def main():
    """Main CLI entry point."""
    # Configure root logging once so INFO diagnostics (fetch/survive/dedup
    # counts) are visible in CI. Guarded so a pre-configured root logger
    # (e.g. via logging.basicConfig in a wrapper) is not clobbered.
    if not logging.getLogger().handlers:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        )

    parser = argparse.ArgumentParser(description="Daily arXiv paper aggregator")
    parser.add_argument(
        '--config_path', type=str, default='config.yaml',
        help='configuration file path'
    )
    parser.add_argument(
        '--update_paper_links', default=False, action="store_true",
        help='whether to update paper links etc.'
    )
    parser.add_argument(
        '--fresh-run', default=False, action="store_true",
        help='reset all JSON files (clear existing data) before running'
    )
    parser.add_argument(
        '--send-email', default=False, action="store_true",
        help='send email with today\'s papers'
    )
    parser.add_argument(
        '--email-recipient', type=str, default=None,
        help='email recipient for daily updates (overrides config)'
    )
    parser.add_argument(
        '--smtp-user', type=str, default=None,
        help='SMTP username (overrides config and env variables)'
    )
    parser.add_argument(
        '--smtp-password', type=str, default=None,
        help='SMTP password (overrides config and env variables)'
    )

    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config_path)

    if not validate_config(config):
        logging.error("Invalid configuration. Exiting.")
        return 1

    # Apply command line overrides
    config.update({
        'update_paper_links': args.update_paper_links,
        'fresh_run': args.fresh_run,
        'send_email': args.send_email or config.get('send_email', False),
    })

    # Override email recipient if provided
    if args.email_recipient:
        config['email_recipient'] = args.email_recipient

    # Override SMTP settings if provided via command line
    if args.smtp_user or args.smtp_password:
        if 'email_settings' not in config:
            config['email_settings'] = {}

        if args.smtp_user:
            config['email_settings']['smtp_user'] = args.smtp_user

        if args.smtp_password:
            config['email_settings']['smtp_password'] = args.smtp_password

    # Run the application
    app = DailyArxivApp(config)
    app.run()

    return 0


if __name__ == "__main__":
    exit(main())
