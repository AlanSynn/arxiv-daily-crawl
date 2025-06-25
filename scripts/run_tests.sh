#!/bin/bash
# Test runner script for cv-arxiv-daily
# This script runs all tests and provides helpful output

echo "🧪 Running tests for cv-arxiv-daily..."
echo "========================================="

# Activate virtual environment if it exists
if [ -d ".venv" ]; then
    echo "📦 Activating virtual environment..."
    source .venv/bin/activate
fi

# Run basic functionality tests
echo ""
echo "🔧 Running basic functionality tests..."
python -m pytest tests/test_basic_functionality.py -v

# Run refactored functionality tests
echo ""
echo "⚙️ Running refactored functionality tests..."
python -m pytest tests/test_refactored_functionality.py -v

# Run daily filtering tests (new feature)
echo ""
echo "📅 Running daily filtering tests..."
python -m pytest tests/test_daily_filtering.py -v

# Run all tests with coverage if pytest-cov is available
echo ""
echo "📊 Running all tests with summary..."
if python -c "import pytest_cov" 2>/dev/null; then
    echo "🎯 Running with coverage..."
    python -m pytest tests/ --cov=src --cov-report=term-missing
else
    echo "📋 Running all tests..."
    python -m pytest tests/ -v
fi

echo ""
echo "✅ Test run completed!"
echo ""
echo "💡 To run specific tests:"
echo "   Basic tests:     pytest tests/test_basic_functionality.py"
echo "   Features tests:  pytest tests/test_refactored_functionality.py"
echo "   Filtering tests: pytest tests/test_daily_filtering.py"
echo ""
echo "🔍 To run tests with more detail:"
echo "   pytest tests/ -v -s"
echo ""
echo "📈 To run with coverage:"
echo "   pytest tests/ --cov=src --cov-report=html"