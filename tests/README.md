# 🧪 Tests for CV-ArXiv-Daily

This directory contains comprehensive tests for the cv-arxiv-daily project, including tests for the new daily paper filtering functionality.

## 📁 Test Structure

```
tests/
├── README.md                           # This file
├── conftest.py                         # Test fixtures and configuration
├── test_basic_functionality.py         # Basic project functionality tests
├── test_refactored_functionality.py    # Core feature tests
├── test_daily_filtering.py            # NEW: Daily paper filtering tests
├── fixtures/                          # Test data files
└── __pycache__/                       # Compiled test files
```

## 🎯 Test Categories

### 1. Basic Functionality Tests (`test_basic_functionality.py`)
- ✅ Directory creation
- ✅ Configuration loading
- ✅ Project structure validation
- ✅ Import system
- ✅ Dependencies

### 2. Core Feature Tests (`test_refactored_functionality.py`)
- ✅ ArXiv client operations
- ✅ GitHub integration
- ✅ Email service
- ✅ File management
- ✅ Content generation
- ✅ Utility functions

### 3. Daily Filtering Tests (`test_daily_filtering.py`) 🆕
- ✅ **Mixed date filtering**: Tests email filtering with papers from different dates
- ✅ **Same date handling**: Tests behavior when all papers are from same date
- ✅ **Empty results**: Tests handling of no papers found
- ✅ **Date identification**: Tests most recent date detection
- ✅ **Content formatting**: Tests markdown table and web format output
- ✅ **Code URL integration**: Tests GitHub code link fetching
- ✅ **CLI integration**: Tests end-to-end workflow

## 🚀 Running Tests

### Quick Start
```bash
# Run all tests
./scripts/run_tests.sh

# Or use pytest directly
python -m pytest tests/ -v
```

### Specific Test Categories
```bash
# Basic functionality only
pytest tests/test_basic_functionality.py -v

# Core features only
pytest tests/test_refactored_functionality.py -v

# Daily filtering only (new feature)
pytest tests/test_daily_filtering.py -v
```

### Advanced Test Options
```bash
# Run with detailed output
pytest tests/ -v -s

# Run with coverage report
pytest tests/ --cov=src --cov-report=term-missing

# Run with HTML coverage report
pytest tests/ --cov=src --cov-report=html
```

## 🔍 Key Test Features

### Daily Filtering Test Highlights

The new `test_daily_filtering.py` thoroughly tests the core feature change:

- **Email gets most recent day only**: Validates that email contains only papers from the most recent date
- **Main report gets all papers**: Validates that main files contain all papers regardless of date
- **Proper date handling**: Tests various date scenarios (mixed dates, same dates, no papers)
- **Content format validation**: Ensures proper markdown table and web format output
- **Integration testing**: Tests the complete workflow from ArXiv API to file output

### Mock Objects

Tests use comprehensive mock objects to simulate ArXiv API responses:

- `MockArxivResult`: Simulates ArXiv paper objects
- `MockAuthor`: Simulates paper author objects
- `MockDate`: Simulates date objects
- `MockSearchResults`: Simulates ArXiv search results

### Test Fixtures

Common test data is provided through pytest fixtures:

- `client`: ArXivClient instance
- `mixed_date_papers`: Papers from different dates for filtering tests
- `same_date_papers`: Papers from the same date
- Various configuration and data fixtures from `conftest.py`

## 📊 Test Coverage

Current test coverage includes:

- ✅ ArXiv API client with new filtering logic
- ✅ Paper processing and formatting
- ✅ Date filtering and most recent date detection
- ✅ Content generation (both table and web formats)
- ✅ GitHub code URL integration
- ✅ CLI integration and workflow
- ✅ Error handling and edge cases

## 🐛 Debugging Tests

### Common Issues

1. **Import errors**: Make sure you're in the project root directory
2. **Missing dependencies**: Run `uv sync --dev` to install test dependencies
3. **Virtual environment**: Ensure `.venv` is activated

### Debugging Commands

```bash
# Run single test with detailed output
pytest tests/test_daily_filtering.py::test_daily_filtering_with_mixed_dates -v -s

# Run tests with pdb debugger
pytest tests/test_daily_filtering.py --pdb

# Run tests and stop on first failure
pytest tests/ -x
```

## 📝 Writing New Tests

When adding new functionality, follow this pattern:

1. **Add fixtures** in `conftest.py` for reusable test data
2. **Create test file** named `test_[feature_name].py`
3. **Use descriptive test names** that explain what is being tested
4. **Mock external dependencies** (ArXiv API, file system, etc.)
5. **Test both success and failure cases**
6. **Update this README** with new test information

### Example Test Structure

```python
def test_new_feature_with_specific_scenario(client, fixture_data):
    """Test that new feature handles specific scenario correctly."""

    # Arrange
    mock_setup_here()

    # Act
    result = client.new_method(test_params)

    # Assert
    assert expected_behavior
    assert result_validation
```

## 🏆 Test Results

All tests should pass consistently. If you see failures:

1. Check the specific test output for details
2. Verify your environment setup
3. Ensure all dependencies are installed
4. Check for any local configuration issues

**Current Status**: ✅ 27 tests passing

---

*Tests ensure the daily paper filtering feature works correctly while maintaining backward compatibility with existing functionality.*