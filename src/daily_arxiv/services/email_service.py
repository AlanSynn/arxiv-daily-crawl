"""Email service: renders and sends the 'Daily arXiv Dispatch' digest.

The Dispatch is a 600px-wide, table-based HTML email engineered to render
reliably in Gmail, Apple Mail, and Outlook. It is themed after Alan Synn's
"Drafting Bench" design system (alansynn.com): a sunken page, a raised
white content card, serif display titles (Newsreader → Iowan Old Style →
Georgia), mono metadata, and a single royal-blue accent reserved for the
masthead eyebrow, the section sigils, the abstract toggle, and the
score-badge tint. The coupler-curve signature — a four-bar-linkage path,
Alan's automata motif — appears as the masthead and footer divider. There
are no traffic-light score bands; the numeric score lives in a single
accent-tinted badge per paper.

Email-compat constraints:

* All CSS inline on each element. The only ``<style>`` block lives in
  ``<head>`` and contains ONLY (a) ``@media (prefers-color-scheme: dark)``
  overrides on a small reusable class set with ``!important``, (b) the
  ``.badge`` light-mode default (so the dark override can target the same
  class cleanly — the ONE exception to "all inline"), (c)
  ``@media (max-width: 520px)`` grid-collapse rules, and (d) hover /
  summary niceties.
* Tables for all layout (``role="presentation" cellpadding="0"
  cellspacing="0" border="0"``). No flexbox, no position, no shadows, no
  large radii (8px card / badge radii are OK — Apple Mail / Gmail honor
  them; Outlook ignores gracefully).
* No web-font ``@import`` (web fonts don't load in email); the families
  are kept in the font stacks so macOS / iOS picks up local Newsreader /
  Iowan Old Style / Hanken Grotesk / IBM Plex Mono if installed.
* Every dynamic string is HTML-escaped via :func:`html.escape`.
* Abstracts trimmed to ~600 chars to keep the rendered size under the
  ~102KB Gmail clip threshold.
"""

import html
import logging
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any, Dict, List, Optional, Tuple

from ..models.paper import Paper


# --- Design tokens: "Drafting Bench" (alansynn.com) -------------------------

# Light (default — applied inline on each element).
_PAPER            = "#FFFFFF"   # surface — content card (paper-raised white)
_PAGE             = "#F5F6F8"   # page/well background (paper-sunken) — outer area
_RAISED           = "#FFFFFF"   # card surface
_SUNKEN           = "#F5F6F8"   # wells / code-ish areas (reserved for future use)
_INK              = "#15171C"   # primary text
_INK_SOFT         = "#3A3F47"   # secondary text
_MUTED            = "#5E646B"   # metadata / tertiary text
_FAINT            = "#99A0A8"   # very low-emphasis (reserved for future use)
_HAIRLINE         = "#E8EAEE"   # borders / rules
_HAIRLINE_S       = "#D3D7DD"   # strong rules (reserved for future use)
_ACCENT           = "#1D4E89"   # royal blue (light)
_ACCENT_S         = "#163A6B"   # accent hover / pressed (deeper navy) — badge text
_ACCENT_TINT      = "#E8EDF4"   # pre-mixed accent-tint bg for badges (email-safe solid)
_ACCENT_TINT_BORDER = "#C7D4E3"  # accent-tint border for badges

# Type stacks — include local families so macOS / iOS picks them up if installed.
_SERIF = ("'Newsreader', 'Iowan Old Style', Georgia, "
          "'Times New Roman', serif")
_SANS  = ("'Hanken Grotesk', 'Inter', system-ui, -apple-system, "
          "BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', "
          "Arial, sans-serif")
_MONO  = ("'IBM Plex Mono', 'JetBrains Mono', ui-monospace, 'SF Mono', "
          "Menlo, Consolas, 'Liberation Mono', 'Courier New', monospace")


# --- Pure helpers -----------------------------------------------------------

def _slugify(name: str) -> str:
    """Intra-email anchor slug.

    Lowercase; runs of non-alphanumeric chars collapse to a single hyphen;
    leading/trailing hyphens stripped.  Stable within a single render so
    that ``<a href="#slug">`` always matches the section ``id="slug"``.

    This is NOT GitHub's slug function (we intentionally do not strip
    underscores-as-word-boundaries etc.) — it only needs to round-trip
    inside this email.
    """
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s)
    s = s.strip("-")
    return s or "section"


def _trim_abstract(text: str, limit: int = 600) -> str:
    """Trim to ~``limit`` chars at a sentence ('. ') or word (' ') boundary.

    Appends a single space + Unicode ellipsis (' \\u2026').  Abstracts
    already under the limit are returned unchanged; empty / whitespace-only
    abstracts return an em-dash placeholder.
    """
    if not text or not text.strip():
        return "—"
    text = text.strip()
    if len(text) <= limit:
        return text
    head = text[:limit]
    last_sentence = head.rfind(". ")
    if last_sentence >= limit // 2:
        return text[:last_sentence + 1].rstrip() + " …"
    last_space = head.rfind(" ")
    if last_space > 0:
        return text[:last_space].rstrip() + " …"
    return head.rstrip() + " …"


def _teaser(text: str, limit: int = 120) -> str:
    """One-line teaser for the top-5 block."""
    if not text or not text.strip():
        return ""
    text = text.strip()
    if len(text) <= limit:
        return text
    head = text[:limit]
    last_space = head.rfind(" ")
    if last_space > 0:
        return text[:last_space].rstrip() + " …"
    return head.rstrip() + " …"


def _esc(value: Optional[str]) -> str:
    """HTML-escape a dynamic string for safe insertion into the document."""
    return html.escape(value if value is not None else "", quote=True)


def _coupler_svg() -> str:
    """Static inline SVG of a four-bar-linkage coupler curve.

    The automata motif from Alan's site — used as the masthead and footer
    divider. Light-mode stroke / fill use ``_ACCENT`` inline; the
    ``svg .accent`` head rule overrides with ``!important`` in dark mode.
    """
    return (
        '<svg width="120" height="48" viewBox="0 0 240 96" fill="none" '
        'xmlns="http://www.w3.org/2000/svg" '
        'style="display:block; margin:0 auto; opacity:0.55;" '
        'role="img" aria-label="coupler curve">'
        # Left crank link.
        f'<line x1="8" y1="90" x2="40" y2="60" class="accent" '
        f'style="stroke:{_ACCENT}; stroke-width:2; stroke-linecap:round;"></line>'
        # Right follower link.
        f'<line x1="232" y1="90" x2="208" y2="46" class="accent" '
        f'style="stroke:{_ACCENT}; stroke-width:2; stroke-linecap:round;"></line>'
        # Left ground pivot.
        f'<circle cx="8" cy="90" r="3" class="accent" '
        f'style="fill:{_ACCENT};"></circle>'
        # Right ground pivot.
        f'<circle cx="232" cy="90" r="3" class="accent" '
        f'style="fill:{_ACCENT};"></circle>'
        # Coupler curve path.
        f'<path class="accent" style="stroke:{_ACCENT}; stroke-width:2; '
        f'stroke-linejoin:round; fill:none;" d="M 40 60 C 18 34 52 14 98 20 '
        f'C 142 26 198 10 208 46 C 215 70 176 80 138 71 C 102 62 80 86 60 77 '
        f'C 50 73 42 68 40 60 Z"></path>'
        # Coupler point.
        f'<circle cx="40" cy="60" r="3.5" class="accent" '
        f'style="fill:{_ACCENT};"></circle>'
        '</svg>'
    )


def _score_badge(score: float) -> str:
    """Numeric score badge.

    Bg / border / color come from the head ``.badge`` rule (so the
    accent-tint flips cleanly in dark mode); only font / padding / radius
    are inline.  Score is formatted to 2 decimals.
    """
    return (
        f'<span class="badge" style="font-family:{_MONO}; font-size:10px; '
        f'font-weight:500; letter-spacing:0.04em; padding:2px 6px; '
        f'border-radius:4px; line-height:1.4; white-space:nowrap; '
        f'display:inline-block;">{score:.2f}</span>'
    )


def _upvote_badge(upvotes: int) -> str:
    """Community-signal upvote badge (HuggingFace papers).

    Shares the ``.badge`` shell with :func:`_score_badge` so the accent-tint
    flips cleanly in dark mode; the content is an up-triangle + integer count,
    visually distinct from the decimal relevance score so a reader can tell a
    community-signal paper from a scored one at a glance.
    """
    return (
        f'<span class="badge" style="font-family:{_MONO}; font-size:10px; '
        f'font-weight:500; letter-spacing:0.04em; padding:2px 6px; '
        f'border-radius:4px; line-height:1.4; white-space:nowrap; '
        f'display:inline-block;">▲ {upvotes}</span>'
    )


# --- EmailService -----------------------------------------------------------

class EmailService:
    """Service for rendering and sending the daily arXiv Dispatch email."""

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize email service with configuration.

        Args:
            config: Configuration dictionary containing email settings.
        """
        self.config = config
        self.email_settings = config.get('email_settings', {})

    # ------------------------------------------------------------------ public

    def send_email(self, email_to: str, email_subject: str, email_body: str) -> bool:
        """
        Send email with daily paper updates.

        Args:
            email_to: Recipient email address.
            email_subject: Email subject.
            email_body: Email body content (HTML format).

        Returns:
            True if email sent successfully, False otherwise.
        """
        if not self._is_email_enabled():
            logging.warning("Email settings not configured or disabled")
            return False

        if not self._validate_smtp_settings():
            logging.error("SMTP settings incomplete. Check your config file.")
            return False

        msg = self._create_email_message(email_to, email_subject, email_body)
        return self._send_via_smtp(msg, email_to)

    def render_email(
        self,
        papers_by_category: Dict[str, List[Paper]],
        date_now: str,
        stats: Optional[Dict[str, Any]] = None,
    ) -> str:
        """Render the 'Daily arXiv Dispatch' HTML email.

        Args:
            papers_by_category: ``{category_name: [Paper, ...]}`` — today's
                slice (already filtered to the most-recent published day).
            date_now: ``YYYY-MM-DD`` string for the masthead.
            stats: Optional ``{"total": int, "categories": int,
                "threshold": float}``.  When ``None``, ``total`` and
                ``categories`` are derived from ``papers_by_category`` and
                the threshold clause is omitted from the meta line.

        Returns:
            Complete HTML document string (``<!DOCTYPE html>...</html>``).
        """
        if stats is None:
            total = sum(len(v) for v in papers_by_category.values())
            categories = sum(1 for v in papers_by_category.values() if v)
            stats = {"total": total, "categories": categories, "threshold": None}

        # Preserve caller's dict order; sort each section by score desc so
        # the strongest paper leads each section.
        sections: List[Tuple[str, List[Paper]]] = [
            (name, sorted(list(papers), key=lambda p: p.score, reverse=True))
            for name, papers in papers_by_category.items()
            if papers
        ]
        total_papers = sum(len(papers) for _, papers in sections)

        body_parts: List[str] = [self._render_masthead(date_now, stats)]

        if total_papers == 0:
            body_parts.append(self._render_empty_state())
        else:
            # Top-5 block only when it would not duplicate the sections.
            if total_papers > 5:
                body_parts.append(
                    self._render_top5(self._compute_top5(papers_by_category))
                )
            body_parts.append(self._render_index(sections))
            body_parts.append(self._render_sections(sections))

        body_parts.append(self._render_footer())
        return self._render_document(date_now, "".join(body_parts))

    # ----------------------------------------------------------- SMTP helpers

    def _is_email_enabled(self) -> bool:
        """Check if email functionality is enabled."""
        return self.email_settings.get('enabled', False)

    def _validate_smtp_settings(self) -> bool:
        """Validate that all required SMTP settings are present."""
        required = ['smtp_server', 'smtp_user', 'smtp_password']
        return all(self.email_settings.get(setting) for setting in required)

    def _create_email_message(
        self, email_to: str, email_subject: str, email_body: str
    ) -> MIMEMultipart:
        """Create email message with HTML and text parts."""
        msg = MIMEMultipart('alternative')
        msg['Subject'] = email_subject
        msg['From'] = self.email_settings['smtp_user']
        msg['To'] = email_to

        text_part = MIMEText(
            "This email requires HTML support to view properly.", 'plain'
        )
        html_part = MIMEText(email_body, 'html')
        msg.attach(text_part)
        msg.attach(html_part)
        return msg

    def _send_via_smtp(self, msg: MIMEMultipart, email_to: str) -> bool:
        """Send email via SMTP server."""
        try:
            # timeout=30: a stalled SMTP connection must not hang the run for
            # the CI job limit (a job killed at the limit dies before the
            # state-commit steps, losing that day's dedup state).
            with smtplib.SMTP(self.email_settings['smtp_server'],
                              self.email_settings.get('smtp_port', 587),
                              timeout=30) as server:
                server.ehlo()
                server.starttls()
                server.login(self.email_settings['smtp_user'],
                             self.email_settings['smtp_password'])
                server.send_message(msg)
            logging.info(f"Email sent successfully to {email_to}")
            return True
        except Exception as e:
            logging.error(f"Failed to send email: {e}")
            return False

    # ----------------------------------------------------------- render helpers

    @staticmethod
    def _compute_top5(papers_by_category: Dict[str, List[Paper]]) -> List[Paper]:
        """Flatten, dedupe by ``paper_key`` (keep best score), sort desc, take 5.

        Community-signal (HuggingFace) papers are excluded: their ``score``
        is the neutral ``0.0`` default (popularity lives in ``upvotes``), so
        they would pollute the relevance ranking and squeeze out scored
        arXiv papers whenever the slice is short. Dedupe is defensive — in
        the email slice each paper appears in exactly one category, but the
        flatten-then-sort should not promote a single paper twice if a caller
        ever passes duplicates.
        """
        best: Dict[str, Paper] = {}
        for papers in papers_by_category.values():
            for p in papers:
                if p.is_community_signal:
                    continue
                prev = best.get(p.paper_key)
                if prev is None or p.score > prev.score:
                    best[p.paper_key] = p
        return sorted(best.values(), key=lambda p: p.score, reverse=True)[:5]

    @staticmethod
    def _render_document(date_now: str, body_html: str) -> str:
        """Wrap rendered body parts in the full HTML document shell.

        The ``<head>`` ``<style>`` block carries ONLY:
        (1) ``@media (prefers-color-scheme: dark)`` overrides on a small
            reusable class set (``.page .surface .card .ink .muted .rule
            .accent .badge`` + ``svg .accent``) with ``!important``;
        (2) the ``.badge`` light default (outside the dark block, so the
            class owns badge bg / border / color in both modes);
        (3) ``@media (max-width: 520px)`` grid-collapse rules with
            ``!important``;
        (4) ``a:hover`` underline + ``summary`` cursor / marker niceties.

        Every visual also works without this block — light defaults are
        inline on each element (badges excepted, as noted above).
        """
        title = f"Daily arXiv Dispatch — {date_now}"
        style_block = (
            '  <style>\n'
            '    @media (prefers-color-scheme: dark) {\n'
            '      .page { background:#13171A !important; }\n'
            '      .surface { background:#1B2126 !important; }\n'
            '      .card { border-color:#2A3137 !important; }\n'
            '      .ink, .ink a { color:#E9E6E0 !important; }\n'
            '      .muted, .muted a { color:#93989D !important; }\n'
            '      .rule { background:#2A3137 !important; '
            'border-color:#2A3137 !important; }\n'
            '      .accent { color:#6BA8FF !important; }\n'
            '      .badge { background:#1C2733 !important; '
            'border-color:#2A3A4A !important; color:#8FBCFF !important; }\n'
            '      svg .accent { stroke:#6BA8FF !important; '
            'fill:#6BA8FF !important; }\n'
            '    }\n'
            '    .badge { background:' + _ACCENT_TINT + '; '
            'border:1px solid ' + _ACCENT_TINT_BORDER + '; '
            'color:' + _ACCENT_S + '; }\n'
            '    @media (max-width: 520px) {\n'
            '      .grid-card { display:block !important; '
            'width:100% !important; '
            'padding-left:0 !important; padding-right:0 !important; }\n'
            '      .grid-gutter { display:none !important; }\n'
            '    }\n'
            '    a:hover { text-decoration: underline !important; }\n'
            '    details > summary { cursor: pointer; list-style: none; }\n'
            '    details > summary::-webkit-details-marker { display: none; }\n'
            '  </style>\n'
        )
        return (
            '<!DOCTYPE html>\n'
            '<html lang="en">\n'
            '<head>\n'
            '  <meta charset="utf-8">\n'
            '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '  <meta name="color-scheme" content="light dark">\n'
            '  <meta name="supported-color-schemes" content="light dark">\n'
            f'  <title>{_esc(title)}</title>\n'
            + style_block +
            '</head>\n'
            f'<body class="page" style="margin:0; padding:0; '
            f'background:{_PAGE};">\n'
            '  <table role="presentation" cellpadding="0" cellspacing="0"'
            f' border="0" width="100%" class="page" '
            f'style="background:{_PAGE};">\n'
            '    <tr>\n'
            '      <td align="center" style="padding:24px;">\n'
            '        <table role="presentation" cellpadding="0" '
            'cellspacing="0" border="0" width="600" class="surface card" '
            f'style="background:{_PAPER}; border:1px solid {_HAIRLINE}; '
            f'width:600px; max-width:600px; border-collapse:separate;">\n'
            '          <tr>\n'
            '            <td style="padding:32px 28px;">\n'
            + body_html +
            '            </td>\n'
            '          </tr>\n'
            '        </table>\n'
            '      </td>\n'
            '    </tr>\n'
            '  </table>\n'
            '</body>\n'
            '</html>\n'
        )

    @staticmethod
    def _render_masthead(date_now: str, stats: Dict[str, Any]) -> str:
        """Masthead: eyebrow · serif hero date · mono meta · coupler divider."""
        meta_parts = [
            f"{stats.get('total', 0)} papers",
            f"{stats.get('categories', 0)} categories",
        ]
        threshold = stats.get("threshold")
        if threshold is not None:
            try:
                meta_parts.append(f"score ≥ {float(threshold):.2f}")
            except (TypeError, ValueError):
                pass
        meta_line = " · ".join(meta_parts)
        return (
            '<table role="presentation" cellpadding="0" cellspacing="0"'
            ' border="0" width="100%">'
            # Eyebrow — mono, accent, uppercase, letter-spaced.
            '<tr><td style="padding-bottom:6px;">'
            f'<div class="accent" style="font-family:{_MONO}; '
            f'color:{_ACCENT}; font-size:11px; font-weight:500; '
            f'letter-spacing:2.5px; text-transform:uppercase;">'
            'DAILY ARXIV DISPATCH</div>'
            '</td></tr>'
            # Hero date — serif, ink, big.
            '<tr><td style="padding-bottom:6px;">'
            f'<div class="ink" style="font-family:{_SERIF}; color:{_INK}; '
            f'font-size:26px; font-weight:600; line-height:1.1; '
            f'letter-spacing:-0.02em;">{_esc(date_now)}</div>'
            '</td></tr>'
            # Meta line — mono, muted.
            '<tr><td style="padding-bottom:8px;">'
            f'<div class="muted" style="font-family:{_MONO}; color:{_MUTED}; '
            f'font-size:11px;">{_esc(meta_line)}</div>'
            '</td></tr>'
            # Coupler-curve divider.
            f'<tr><td style="padding:8px 0 4px 0;">{_coupler_svg()}</td></tr>'
            '</table>'
            # 20px gap to next block.
            '<div style="height:20px; line-height:20px; font-size:1px;">'
            '&nbsp;</div>'
        )

    @staticmethod
    def _render_top5(top_papers: List[Paper]) -> str:
        """TOP 5 BY RELEVANCE — 2-column mini-card grid."""
        if not top_papers:
            return ""

        def _mini_card(paper: Paper) -> str:
            teaser = _teaser(paper.abstract, 110)
            return (
                # Nested 1-cell table = the mini-card.
                '<table role="presentation" cellpadding="0" cellspacing="0"'
                f' border="0" width="100%" class="surface card" '
                f'style="background:{_RAISED}; '
                f'border:1px solid {_HAIRLINE}; border-radius:8px; '
                f'border-collapse:separate;">'
                '<tr><td style="padding:12px;">'
                # Score badge.
                f'<div style="margin-bottom:6px;">'
                f'{_score_badge(paper.score)}</div>'
                # Title — serif.
                f'<div class="ink" style="font-family:{_SERIF}; '
                f'color:{_INK}; font-size:14px; font-weight:600; '
                f'line-height:1.25;">'
                f'<a href="{_esc(paper.abs_url)}" class="ink" '
                f'style="color:{_INK}; text-decoration:none;">'
                f'{_esc(paper.title)}</a></div>'
                # Meta — mono, muted.
                f'<div class="muted" style="font-family:{_MONO}; '
                f'color:{_MUTED}; font-size:10px; margin-top:4px;">'
                f'{_esc(paper.authors_str)} et al. · '
                f'{_esc(paper.paper_key)}</div>'
                # Teaser — mono, ink-soft.
                f'<div style="font-family:{_MONO}; color:{_INK_SOFT}; '
                f'font-size:11px; line-height:1.4; margin-top:6px;">'
                f'{_esc(teaser)}</div>'
                '</td></tr>'
                '</table>'
            )

        # Pair papers into 2-col rows; odd-one-out gets a spacer cell.
        rows_html: List[str] = []
        i = 0
        while i < len(top_papers):
            left = top_papers[i]
            right = top_papers[i + 1] if i + 1 < len(top_papers) else None
            left_cell = (
                f'<td valign="top" width="50%" class="grid-card" '
                f'style="width:50%; vertical-align:top; padding-right:4px;">'
                f'{_mini_card(left)}</td>'
            )
            if right is not None:
                right_cell = (
                    f'<td valign="top" width="50%" class="grid-card" '
                    f'style="width:50%; vertical-align:top; padding-left:4px;">'
                    f'{_mini_card(right)}</td>'
                )
            else:
                right_cell = (
                    '<td width="50%" class="grid-gutter" '
                    'style="width:50%; padding-left:4px;">&nbsp;</td>'
                )
            rows_html.append(f'<tr>{left_cell}{right_cell}</tr>')
            i += 2

        return (
            '<table role="presentation" cellpadding="0" cellspacing="0"'
            ' border="0" width="100%">'
            # Eyebrow row with hairline border-bottom.
            f'<tr><td class="rule" style="padding-bottom:6px; '
            f'border-bottom:1px solid {_HAIRLINE};">'
            f'<div class="muted" style="font-family:{_MONO}; '
            f'color:{_MUTED}; font-size:10px; font-weight:500; '
            f'letter-spacing:2px; text-transform:uppercase;">'
            'TOP 5 BY RELEVANCE</div>'
            '</td></tr>'
            '<tr><td style="padding-top:12px;">'
            '<table role="presentation" cellpadding="0" cellspacing="0"'
            ' border="0" width="100%">'
            + "".join(rows_html) +
            '</table>'
            '</td></tr>'
            '</table>'
            '<div style="height:20px; line-height:20px; font-size:1px;">'
            '&nbsp;</div>'
        )

    @staticmethod
    def _render_index(sections: List[Tuple[str, List[Paper]]]) -> str:
        """2-column chip grid: bordered pill per category with count badge."""
        def _chip(name: str, slug: str, count: int) -> str:
            count_badge = (
                f'<span class="badge" style="font-family:{_MONO}; '
                f'font-size:10px; font-weight:500; letter-spacing:0.04em; '
                f'padding:2px 6px; border-radius:4px; line-height:1.4; '
                f'white-space:nowrap; display:inline-block;">{count}</span>'
            )
            return (
                # Nested 1-cell table = the chip box.
                '<table role="presentation" cellpadding="0" cellspacing="0"'
                f' border="0" width="100%" class="surface card" '
                f'style="background:{_RAISED}; '
                f'border:1px solid {_HAIRLINE}; border-radius:8px; '
                f'border-collapse:separate;">'
                '<tr><td style="padding:8px 10px;">'
                # Name + count in a 2-cell row.
                '<table role="presentation" cellpadding="0" cellspacing="0"'
                ' border="0" width="100%">'
                '<tr>'
                # Category name (anchor link to section id).
                f'<td class="ink" style="font-family:{_MONO}; '
                f'color:{_INK}; font-size:12px; font-weight:600;">'
                f'<a href="#{slug}" class="ink" '
                f'style="color:{_INK}; text-decoration:none;">'
                f'{_esc(name)}</a>'
                '</td>'
                # Count badge (right).
                f'<td align="right" style="text-align:right;">'
                f'{count_badge}</td>'
                '</tr>'
                '</table>'
                '</td></tr>'
                '</table>'
            )

        rows_html: List[str] = []
        i = 0
        while i < len(sections):
            left_name, left_papers = sections[i]
            left_slug = _slugify(left_name)
            right_pair = sections[i + 1] if i + 1 < len(sections) else None
            left_cell = (
                f'<td valign="top" width="50%" class="grid-card" '
                f'style="width:50%; vertical-align:top; padding-right:4px;">'
                f'{_chip(left_name, left_slug, len(left_papers))}</td>'
            )
            if right_pair is not None:
                right_name, right_papers = right_pair
                right_slug = _slugify(right_name)
                right_cell = (
                    f'<td valign="top" width="50%" class="grid-card" '
                    f'style="width:50%; vertical-align:top; padding-left:4px;">'
                    f'{_chip(right_name, right_slug, len(right_papers))}</td>'
                )
            else:
                right_cell = (
                    '<td width="50%" class="grid-gutter" '
                    'style="width:50%; padding-left:4px;">&nbsp;</td>'
                )
            rows_html.append(f'<tr>{left_cell}{right_cell}</tr>')
            i += 2

        return (
            '<table role="presentation" cellpadding="0" cellspacing="0"'
            ' border="0" width="100%">'
            # Eyebrow row with hairline border-bottom.
            f'<tr><td class="rule" style="padding-bottom:6px; '
            f'border-bottom:1px solid {_HAIRLINE};">'
            f'<div class="muted" style="font-family:{_MONO}; '
            f'color:{_MUTED}; font-size:10px; font-weight:500; '
            f'letter-spacing:2px; text-transform:uppercase;">INDEX</div>'
            '</td></tr>'
            '<tr><td style="padding-top:12px;">'
            '<table role="presentation" cellpadding="0" cellspacing="0"'
            ' border="0" width="100%">'
            + "".join(rows_html) +
            '</table>'
            '</td></tr>'
            '</table>'
            '<div style="height:24px; line-height:24px; font-size:1px;">'
            '&nbsp;</div>'
        )

    @staticmethod
    def _render_sections(sections: List[Tuple[str, List[Paper]]]) -> str:
        """One block per category: section head + stacked full-width cards."""
        out: List[str] = []
        for idx, (name, papers) in enumerate(sections, start=1):
            slug = _slugify(name)
            count = len(papers)
            paper_cards = "".join(
                EmailService._render_paper_block(p) for p in papers
            )
            section_num = f"{idx:02d}"
            paper_label = "1 PAPER" if count == 1 else f"{count} PAPERS"
            out.append(
                '<table role="presentation" cellpadding="0" cellspacing="0"'
                ' border="0" width="100%" style="margin-bottom:24px;">'
                '<tr><td>'
                # Section head — hairline border-bottom row.
                '<table role="presentation" cellpadding="0" cellspacing="0"'
                ' border="0" width="100%">'
                '<tr>'
                # § NN — mono accent.
                f'<td class="accent" style="font-family:{_MONO}; '
                f'color:{_ACCENT}; font-size:11px; font-weight:500; '
                f'letter-spacing:2px; padding-right:10px; padding-bottom:8px; '
                f'vertical-align:baseline;">§ {section_num}</td>'
                # Title — serif ink (carries the id anchor + border-bottom).
                f'<td id="{slug}" width="100%" class="ink rule" '
                f'style="width:100%; font-family:{_SERIF}; color:{_INK}; '
                f'font-size:18px; font-weight:600; line-height:1.2; '
                f'padding-bottom:8px; border-bottom:1px solid {_HAIRLINE}; '
                f'vertical-align:baseline;">{_esc(name)}</td>'
                # Count — mono muted, right-aligned (also carries the border).
                f'<td align="right" class="muted rule" '
                f'style="text-align:right; font-family:{_MONO}; '
                f'color:{_MUTED}; font-size:10px; font-weight:500; '
                f'letter-spacing:1.5px; text-transform:uppercase; '
                f'padding-bottom:8px; padding-left:10px; '
                f'border-bottom:1px solid {_HAIRLINE}; '
                f'vertical-align:baseline; white-space:nowrap;">'
                f'{paper_label}</td>'
                '</tr>'
                '</table>'
                # 12px gap before paper cards.
                '<div style="height:12px; line-height:12px; font-size:1px;">'
                '&nbsp;</div>'
                # Paper cards (each has its own border + radius).
                f'{paper_cards}'
                '</td></tr>'
                '</table>'
            )
        return "".join(out)

    @staticmethod
    def _render_paper_block(paper: Paper) -> str:
        """A single paper card: title + badge row, inline abstract, link row."""
        abstract = _trim_abstract(paper.abstract, 600)
        pub_str = (
            paper.published.strftime("%Y-%m-%d") if paper.published else ""
        )
        # Link row, built from whatever the paper carries. Order: arXiv key
        # (always) · code · project · hf paper page (community-signal only —
        # surfaces the HF upvotes/comments thread).
        link_pairs: List[Tuple[str, str]] = [
            (f"arXiv:{paper.paper_key}", paper.abs_url)
        ]
        if paper.code_url:
            link_pairs.append(("code", paper.code_url))
        if paper.project_url:
            link_pairs.append(("project", paper.project_url))
        if paper.is_community_signal:
            link_pairs.append(
                ("hf", f"https://huggingface.co/papers/{paper.paper_key}")
            )
        link_row = " · ".join(
            f'<a href="{_esc(url)}" class="muted" '
            f'style="color:{_MUTED}; text-decoration:none;">'
            f'{_esc(label)}</a>'
            for label, url in link_pairs
        )
        # Badge: community-signal papers show their HF upvote count; scored
        # arXiv papers show the relevance score.
        badge = (
            _upvote_badge(paper.upvotes or 0)
            if paper.is_community_signal
            else _score_badge(paper.score)
        )
        return (
            # Nested 1-cell table = the card.
            '<table role="presentation" cellpadding="0" cellspacing="0"'
            f' border="0" width="100%" class="surface card" '
            f'style="background:{_RAISED}; border:1px solid {_HAIRLINE}; '
            f'border-radius:8px; border-collapse:separate; margin-bottom:12px;">'
            '<tr><td style="padding:14px 16px;">'
            # 2-cell row: title cell + badge cell.
            '<table role="presentation" cellpadding="0" cellspacing="0"'
            ' border="0" width="100%">'
            '<tr>'
            # Title cell — serif ink link + meta line beneath.
            f'<td valign="top" class="ink" style="vertical-align:top; '
            f'font-family:{_SERIF}; color:{_INK}; font-size:15px; '
            f'font-weight:600; line-height:1.3; padding-right:10px;">'
            f'<a href="{_esc(paper.abs_url)}" class="ink" '
            f'style="color:{_INK}; text-decoration:none;">'
            f'{_esc(paper.title)}</a>'
            f'<div class="muted" style="font-family:{_MONO}; '
            f'color:{_MUTED}; font-size:10px; margin-top:4px;">'
            f'{_esc(paper.authors_str)} et al. · '
            f'{_esc(paper.paper_key)} · {_esc(pub_str)}</div>'
            '</td>'
            # Badge cell — top-right.
            f'<td valign="top" align="right" style="vertical-align:top; '
            f'text-align:right; white-space:nowrap;">'
            f'{badge}</td>'
            '</tr>'
            '</table>'
            # Abstract — inline. No <details>/<summary> toggle: Outlook and
            # Gmail don't honor the toggle and render the summary as dead
            # text with the body forced open, so a static labelled block is
            # the only choice that looks right in every client.
            f'<div class="accent" style="font-family:{_MONO}; '
            f'color:{_ACCENT}; font-size:10px; font-weight:500; '
            f'text-transform:uppercase; letter-spacing:1.5px; '
            f'margin-top:10px;">ABSTRACT</div>'
            f'<div class="ink" style="font-family:{_SANS}; color:{_INK}; '
            f'font-size:13px; line-height:1.55; padding-top:4px;">'
            f'{_esc(abstract)}</div>'
            # Link row.
            f'<div class="muted" style="font-family:{_MONO}; color:{_MUTED}; '
            f'font-size:10px; margin-top:8px;">{link_row}</div>'
            '</td>'
            '</tr>'
            '</table>'
        )

    @staticmethod
    def _render_empty_state() -> str:
        """Centered serif-italic message when nothing matched."""
        return (
            '<table role="presentation" cellpadding="0" cellspacing="0"'
            ' border="0" width="100%">'
            '<tr><td align="center" style="padding:48px 24px;">'
            f'<div class="muted" style="font-family:{_SERIF}; '
            f'color:{_MUTED}; font-size:14px; font-style:italic; '
            f'line-height:1.6;">'
            'No new papers matched today. The filters may be narrow — '
            'check back tomorrow.'
            '</div>'
            '</td></tr>'
            '</table>'
        )

    @staticmethod
    def _render_footer() -> str:
        """Hairline · coupler mark · attribution + repo link."""
        return (
            '<table role="presentation" cellpadding="0" cellspacing="0"'
            ' border="0" width="100%">'
            # Hairline rule.
            f'<tr><td class="rule" height="1" style="background:{_HAIRLINE}; '
            f'height:1px; line-height:1px; font-size:1px;">&nbsp;</td></tr>'
            # Coupler-curve sign-off mark.
            f'<tr><td style="padding:10px 0 8px 0;">{_coupler_svg()}</td></tr>'
            # Attribution lines, centered.
            '<tr><td align="center" style="text-align:center;">'
            f'<div class="muted" style="font-family:{_MONO}; color:{_MUTED}; '
            f'font-size:10px; line-height:1.6;">'
            'drafting bench dispatch · generated by daily-arxiv'
            '</div>'
            f'<div class="muted" style="font-family:{_MONO}; color:{_MUTED}; '
            f'font-size:10px; line-height:1.6;">'
            f'<a href="https://github.com/AlanSynn/daily-arxiv" class="muted" '
            f'style="color:{_MUTED}; text-decoration:none;">'
            'github.com/AlanSynn/daily-arxiv</a> · full list in '
            'logs/PAPER_LIST.md'
            '</div>'
            '</td></tr>'
            '<tr><td style="padding-bottom:16px;"></td></tr>'
            '</table>'
        )
