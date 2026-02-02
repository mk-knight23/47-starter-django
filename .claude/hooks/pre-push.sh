#!/bin/bash
# Pre-push Hook for Django
# Runs full test suite before pushing

echo "🚀 Running pre-push checks..."

# Activate virtual environment
if [ -d venv ]; then
    source venv/bin/activate
fi

# Run full test suite with coverage
echo "🧪 Running full test suite..."
pytest --cov=. --cov-report=term --cov-fail-under=80

echo "✅ Pre-push checks passed!"
echo "📢 Ready to push!"
