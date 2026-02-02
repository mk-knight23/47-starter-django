#!/bin/bash
# Django Production Deployment Workflow
# Prepares the project for production deployment

set -e

echo "🚀 Django Production Deployment"
echo "================================"
echo ""

# Activate virtual environment
if [ -d venv ]; then
    source venv/bin/activate
else
    echo "❌ Virtual environment not found. Run setup.sh first."
    exit 1
fi

# Check environment variables
echo "⚙️  Checking environment..."
if [ ! -f .env.local ]; then
    echo "❌ .env.local not found. Create it from .env.example"
    exit 1
fi

# Ensure DEBUG is False
if grep -q "DEBUG=True" .env.local; then
    echo "⚠️  WARNING: DEBUG is True in .env.local"
    echo "   Please set DEBUG=False for production"
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Run migrations
echo ""
echo "🗄️  Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --clear

# Create logs directory
mkdir -p logs

echo ""
echo "✅ Production deployment ready!"
echo ""
echo "To start with Gunicorn:"
echo "  gunicorn config.wsgi:application --bind 0.0.0.0:8000"
echo ""
echo "Or with Uvicorn:"
echo "  uvicorn config.asgi:application --host 0.0.0.0 --port 8000"
echo ""
