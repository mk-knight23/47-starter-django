#!/bin/bash
# Django Test Runner
# Runs tests with coverage reporting

set -e

echo "🧪 Running Django Tests"
echo "========================"
echo ""

# Activate virtual environment
if [ -d venv ]; then
    source venv/bin/activate
else
    echo "❌ Virtual environment not found. Run setup.sh first."
    exit 1;
fi

# Run tests with coverage
echo "Running tests with coverage..."
pytest --cov=. --cov-report=html --cov-report=term --verbose

echo ""
echo "✅ Tests complete!"
echo "📊 Coverage report: htmlcov/index.html"
echo ""
