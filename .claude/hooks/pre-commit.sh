#!/bin/bash
# Pre-commit Hook for Django
# Runs linting and formatting before commit

echo "🔍 Running pre-commit checks..."

# Check Python files
echo "🐍 Checking Python files with Ruff..."
ruff check .

# Format with Black
echo "🎨 Formatting Python files with Black..."
black .

# Check types with MyPy
echo "🔎 Checking types with MyPy..."
mypy .

# Run tests
echo "🧪 Running tests..."
pytest

echo "✅ Pre-commit checks passed!"
