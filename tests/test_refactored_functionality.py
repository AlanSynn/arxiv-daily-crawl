"""Test refactored functionality for arxiv-digest."""

import tempfile
import os
from unittest.mock import patch

from src.arxiv_digest.core.config import load_config, validate_config
from src.arxiv_digest.services.arxiv_client import ArXivClient
from src.arxiv_digest.services.email_service import EmailService
from src.arxiv_digest.processors.file_manager import FileManager
from src.arxiv_digest.processors.content_generator import ContentGenerator
from src.arxiv_digest.utils.file_utils import ensure_directory_exists
from src.arxiv_digest.utils.date_utils import format_authors, get_dated_file_paths


def test_config_validation():
    """Test configuration validation."""
    # Valid config (new categories schema)
    valid_config = {
        'base_url': 'https://test.com',
        'max_results': 10,
        'categories': [{'name': 'Test', 'cat_codes': ['cs.GR']}],
    }
    assert validate_config(valid_config) is True

    # Invalid config - missing required key
    invalid_config = {
        'base_url': 'https://test.com'
    }
    assert validate_config(invalid_config) is False

    # Invalid config - no categories
    invalid_config_no_cats = {
        'base_url': 'https://test.com',
        'max_results': 10,
    }
    assert validate_config(invalid_config_no_cats) is False


def test_arxiv_client_initialization():
    """Test ArXiv client can be initialized and exposes the new + legacy APIs."""
    client = ArXivClient()
    assert client is not None
    assert hasattr(client, 'fetch_category')      # new primary API
    assert hasattr(client, 'get_daily_papers')     # deprecated compat wrapper


def test_email_service_initialization():
    """Test email service can be initialized."""
    config = {'email_settings': {'enabled': True}}
    service = EmailService(config)
    assert service is not None
    assert hasattr(service, 'send_email')


def test_file_manager_initialization():
    """Test file manager can be initialized."""
    manager = FileManager()
    assert manager is not None
    assert hasattr(manager, 'update_json_file')


def test_content_generator_initialization():
    """Test content generator can be initialized."""
    generator = ContentGenerator()
    assert generator is not None
    assert hasattr(generator, 'json_to_md')


def test_format_authors():
    """Test author formatting utility."""
    # Mock author objects with proper __str__ implementation
    class MockAuthor:
        def __init__(self, name):
            self.name = name
        def __str__(self):
            return self.name
    
    authors = [MockAuthor('John Doe'), MockAuthor('Jane Smith')]
    
    # Test full author list
    result = format_authors(authors)
    assert 'John Doe' in result
    assert 'Jane Smith' in result
    
    # Test first author only
    result = format_authors(authors, first_author=True)
    assert result == 'John Doe'
    
    # Test empty list
    result = format_authors([])
    assert result == ""


def test_file_utils():
    """Test file utility functions."""
    with tempfile.TemporaryDirectory() as tmpdir:
        test_dir = os.path.join(tmpdir, 'test_subdir')
        ensure_directory_exists(test_dir)
        assert os.path.exists(test_dir)


def test_dated_file_paths():
    """Test dated file path generation."""
    config = {'log_dir': './logs'}
    
    with patch('src.arxiv_digest.utils.date_utils.datetime') as mock_datetime:
        mock_datetime.date.today().strftime.return_value = '2024-01-15'
        
        paths = get_dated_file_paths(config, '2024-01-15')
        
        assert isinstance(paths, dict)
        assert '2024-01-15' in str(paths)


def test_file_manager_json_operations():
    """Test file manager JSON operations."""
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = FileManager()
        json_file = os.path.join(tmpdir, 'test.json')
        
        test_data = [{'Test Category': {'paper1': 'content1'}}]
        
        # Test creating new file
        result = manager.update_json_file(json_file, test_data, create_new=True)

        assert os.path.exists(json_file)
        assert 'Test Category' in result
        assert result['Test Category']['paper1'] == 'content1'


def test_file_manager_dated_update_merges_never_replaces():
    """Regression: dated snapshots must merge, not be replaced (bug N2).

    The dated snapshot filename is keyed on the newest PAPER date, so a
    weekend run (no new papers) or a partial fetch re-writes the same file.
    Replacing it would truncate a complete snapshot into the new subset;
    merging preserves previously-persisted rows.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        manager = FileManager()
        json_file = os.path.join(tmpdir, 'daily_2025-06-13.json')

        full = [{'Cat': {'p1': 'row1', 'p2': 'row2'}}]
        partial = [{'Cat': {'p2': 'row2-new'}}]

        manager.update_json_file(json_file, full)
        result = manager.update_json_file(json_file, partial)

        # The partial fetch must not drop the pre-existing p1 row...
        assert result['Cat']['p1'] == 'row1'
        # ...and must refresh the row it does carry.
        assert result['Cat']['p2'] == 'row2-new'


def test_render_email_basic():
    """render_email produces Digest HTML from real Paper objects."""
    from datetime import date
    from src.arxiv_digest.models.paper import Paper

    config = {'email_settings': {'enabled': True}}
    service = EmailService(config)

    p1 = Paper(
        paper_key="2506.14513", title="MotionSmith: A <Cool> Tool & More",
        authors_str="Alan Synn",
        abstract="We present a system for authoring motion. " * 30,
        published=date(2025, 6, 17), updated=date(2025, 6, 17),
        primary_category="cs.GR", all_categories=["cs.GR", "cs.HC"],
        entry_id="http://arxiv.org/abs/2506.14513",
        abs_url="http://arxiv.org/abs/2506.14513", code_url=None,
        category="Character Motion", score=0.82, matched_keywords=["motion"],
    )
    p2 = Paper(
        paper_key="2506.14000", title="World Models for Robots",
        authors_str="Jane Doe", abstract="Interactive video generation model.",
        published=date(2025, 6, 17), updated=date(2025, 6, 17),
        primary_category="cs.LG", all_categories=["cs.LG"],
        entry_id="http://arxiv.org/abs/2506.14000",
        abs_url="http://arxiv.org/abs/2506.14000",
        code_url="https://github.com/x/y",
        category="World Models", score=0.61, matched_keywords=["world model"],
    )
    html = service.render_email(
        {"Character Motion": [p1], "World Models": [p2]},
        "2025-06-17", {"total": 2, "categories": 2, "threshold": 0.15},
    )

    assert html is not None
    assert "<!DOCTYPE html>" in html
    assert "DAILY ARXIV DISPATCH" in html
    assert "2025-06-17" in html
    assert "MotionSmith" in html
    assert "World Models for Robots" in html
    # HTML-escaping of dynamic content (html.escape with quote=True).
    assert "&lt;Cool&gt;" in html
    assert "&amp; More" in html
    # Top-5 block: only 2 papers, total<=5 -> SKIP per spec (no eyebrow).
    assert "TOP 5 BY RELEVANCE" not in html
    # Dot-leader index eyebrow present.
    assert "INDEX" in html
    # Abstract trimmed (p1 abstract > 600 chars -> ellipsis appended).
    assert "…" in html or "..." in html
    # Code link rendered for p2.
    assert "github.com/x/y" in html
    # Intra-email anchor present and resolves to a matching section id.
    assert 'href="#world-models"' in html
    assert 'id="world-models"' in html


def test_render_email_empty():
    """render_email handles the empty state gracefully."""
    config = {'email_settings': {'enabled': True}}
    service = EmailService(config)

    html = service.render_email({}, "2025-06-17")

    assert "<!DOCTYPE html>" in html
    assert "No new papers matched today" in html
    # No sections / index / top-5 in the empty state.
    assert "INDEX" not in html
    assert "TOP 5 BY RELEVANCE" not in html


def test_render_email_top5_block_when_many_papers():
    """Top-5 block appears once total papers exceed 5."""
    from datetime import date
    from src.arxiv_digest.models.paper import Paper

    config = {'email_settings': {'enabled': True}}
    service = EmailService(config)

    papers = [
        Paper(
            paper_key=f"2506.{i:05d}", title=f"Paper {i}",
            authors_str="Author", abstract="Short abstract.",
            published=date(2025, 6, 17), updated=date(2025, 6, 17),
            primary_category="cs.GR", all_categories=["cs.GR"],
            entry_id=f"http://arxiv.org/abs/2506.{i:05d}",
            abs_url=f"http://arxiv.org/abs/2506.{i:05d}",
            code_url=None, category="Character Motion",
            score=0.1 * i, matched_keywords=[],
        )
        for i in range(1, 9)  # 8 papers, all in one category
    ]
    html = service.render_email({"Character Motion": papers}, "2025-06-17")

    assert "TOP 5 BY RELEVANCE" in html
    # Top-5 should surface the highest-scoring paper first.
    assert "Paper 8" in html


def test_cli_integration():
    """Test that CLI components can be imported and used together."""
    from src.arxiv_digest.cli.main import DailyArxivApp
    
    # Mock config
    config = {
        'base_url': 'https://test.com',
        'kv': {'Test': 'test query'},
        'max_results': 5,
        'email_settings': {'enabled': False}
    }
    
    # Test app initialization
    app = DailyArxivApp(config)
    assert app is not None
    assert hasattr(app, 'run')
    assert app.config == config


def test_query_generation_with_proper_spacing():
    """Fielded queries must keep spaces around OR operators (regression for the
    bare-keyword spacing bug that caused UnexpectedEmptyPageError)."""
    import tempfile
    import yaml
    import re

    # Legacy keywords block is shimmed into a Category; the kv shim then exposes
    # the fielded query string per topic.
    test_config = {
        'base_url': 'https://test.com',
        'max_results': 10,
        'keywords': {
            'Test Category': {
                'filters': [
                    'SingleWord',
                    'Another',
                    'Multi Word Term',
                    'IK',
                    'Sim2Real',
                    'Physics-based Animation'
                ]
            }
        }
    }

    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(test_config, f)
        config_path = f.name

    try:
        config = load_config(config_path)
        query = config['kv']['Test Category']

        # New format wraps each keyword in an abs: field; single words bare,
        # multi-word phrases quoted.
        assert ' OR ' in query
        assert 'abs:SingleWord OR abs:Another' in query
        assert 'abs:IK OR abs:Sim2Real' in query
        assert 'abs:"Multi Word Term"' in query
        assert 'abs:"Physics-based Animation"' in query

        # No ORs glued directly to letters (the original bug).
        bad_ors = re.findall(r'[a-zA-Z]OR[a-zA-Z]', query)
        assert len(bad_ors) == 0, f"Found ORs without proper spacing: {bad_ors}"

    finally:
        os.unlink(config_path)


def test_notified_store_roundtrip_and_prune():
    """notified_store round-trips keys and prunes by arXiv YYMM age."""
    import tempfile
    from datetime import date
    from src.arxiv_digest.processors.notified_store import (
        load_notified, save_notified, prune_old, _key_year_month,
    )

    # Modern + legacy key parsing.
    assert _key_year_month("2506.14513") == (2025, 6)
    assert _key_year_month("9707123") == (1997, 7)        # legacy bare YYMM
    assert _key_year_month("cond-mat/0102003") == (2001, 2)
    assert _key_year_month("garbage") is None             # unparseable -> kept

    today = date(2025, 6, 17)
    keys = {"2506.14513", "2506.14000", "2504.00001", "2401.99999", "weird-key"}
    # max_age_days=30 -> keep_months=1 -> keep May 2025 (05) onward; 2504.* drops.
    pruned = prune_old(keys, max_age_days=30, today=today)
    assert "2506.14513" in pruned
    assert "2506.14000" in pruned
    assert "weird-key" in pruned          # unparseable always kept
    assert "2504.00001" not in pruned
    assert "2401.99999" not in pruned

    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "nested", "notified_papers.json")
        written = save_notified(path, keys, max_age_days=30, today=today)
        assert os.path.exists(path)
        assert written == pruned
        # Round-trip: load reads the {"notified": [...]} shape back.
        reloaded = load_notified(path)
        assert reloaded == pruned


def test_notified_store_load_tolerates_missing_and_corrupt():
    """load_notified never raises; missing/empty/corrupt -> empty set."""
    import tempfile
    from src.arxiv_digest.processors.notified_store import load_notified

    with tempfile.TemporaryDirectory() as tmpdir:
        # Missing file.
        assert load_notified(os.path.join(tmpdir, "nope.json")) == set()

        # Legacy bare-list shape.
        legacy = os.path.join(tmpdir, "legacy.json")
        with open(legacy, "w") as f:
            f.write('["2506.14513", "2506.14000"]')
        assert load_notified(legacy) == {"2506.14513", "2506.14000"}

        # {key: ...} dict shape.
        as_dict = os.path.join(tmpdir, "dict.json")
        with open(as_dict, "w") as f:
            f.write('{"2506.14513": "2025-06-17"}')
        assert load_notified(as_dict) == {"2506.14513"}

        # Corrupt JSON -> empty set, no raise.
        corrupt = os.path.join(tmpdir, "corrupt.json")
        with open(corrupt, "w") as f:
            f.write('{not valid json')
        assert load_notified(corrupt) == set()


def test_dedupe_email_slice_drops_already_notified():
    """_dedupe_email_slice keeps only unseen keys and collapses empty cats."""
    from datetime import date
    from src.arxiv_digest.models.paper import Paper
    from src.arxiv_digest.cli.main import DailyArxivApp

    def _paper(key, cat):
        return Paper(
            paper_key=key, title=f"T {key}", authors_str="A",
            abstract="abs", published=date(2025, 6, 17),
            updated=date(2025, 6, 17), primary_category="cs.GR",
            all_categories=["cs.GR"], entry_id=f"http://arxiv.org/abs/{key}",
            abs_url=f"http://arxiv.org/abs/{key}", code_url=None,
            category=cat, score=0.5, matched_keywords=[],
        )

    slice_in = {
        "Motion": [_paper("2506.14513", "Motion"),   # already notified
                   _paper("2506.14000", "Motion")],   # new
        "World":  [_paper("2506.13000", "World")],   # already notified -> cat empties
    }
    notified = {"2506.14513", "2506.13000"}

    deduped, delta = DailyArxivApp._dedupe_email_slice(slice_in, notified)

    # Only the unseen Motion paper survives; World collapses and is dropped.
    assert set(deduped.keys()) == {"Motion"}
    assert [p.paper_key for p in deduped["Motion"]] == ["2506.14000"]
    assert delta == {"2506.14000"}


def test_send_email_notification_reads_scoring_dataclass():
    """_send_email_notification must read threshold off the ScoringConfig
    dataclass (regression: it once called .get() on it and crashed the whole
    run at the final email step)."""
    from datetime import date
    from unittest.mock import patch
    from src.arxiv_digest.models.paper import Paper
    from src.arxiv_digest.cli.main import DailyArxivApp

    # A real config: load_config turns 'scoring' into a ScoringConfig dataclass.
    config = {
        'base_url': 'https://test.com', 'max_results': 5,
        'categories': [{'name': 'X', 'cat_codes': ['cs.GR']}],
        'scoring': {'threshold': 0.42},
        'email_recipient': 'someone@example.com',
    }
    from src.arxiv_digest.core.config import _parse_scoring
    config['scoring'] = _parse_scoring(config['scoring'])

    app = DailyArxivApp(config)
    paper = Paper(
        paper_key="2506.14513", title="T", authors_str="A", abstract="x",
        published=date(2025, 6, 17), updated=date(2025, 6, 17),
        primary_category="cs.GR", all_categories=["cs.GR"],
        entry_id="http://arxiv.org/abs/2506.14513",
        abs_url="http://arxiv.org/abs/2506.14513", code_url=None,
        category="X", score=0.9, matched_keywords=[],
    )

    # Mock the actual SMTP send; we only care that the threshold is read
    # without AttributeError and render_email is handed the right value.
    with patch.object(app.email_service, 'send_email', return_value=True) as m_send, \
         patch.object(app.email_service, 'render_email', return_value="<html/>") as m_render:
        result = app._send_email_notification({"X": [paper]}, date(2025, 6, 17))

    assert result is True
    m_send.assert_called_once()
    # render_email receives the stats dict carrying the configured threshold.
    _papers, _date, stats = m_render.call_args.args
    assert stats["threshold"] == 0.42