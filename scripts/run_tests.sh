#!/bin/bash
# Test runner script for cv-arxiv-daily

echo "Running tests for cv-arxiv-daily..."
echo "=================================="

# Install test dependencies
echo "Installing test dependencies..."
uv sync --dev

# Run tests with pytest
echo "Running pytest..."
uv run pytest tests/ -v

# Check test results
if [ $? -eq 0 ]; then
    echo "=================================="
    echo "All tests passed! ✅"
else
    echo "=================================="
    echo "Some tests failed! ❌"
    exit 1
fi