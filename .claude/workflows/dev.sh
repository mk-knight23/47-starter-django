#!/bin/bash
# Django Development Server Runner
# Runs the Django development server with auto-reload

set -e

echo "🚀 Starting Django Development Server"
echo "======================================"
echo ""

# Activate virtual environment
if [ -d venv ]; then
    source venv/bin/activate
else
    echo "❌ Virtual environment not found. Run setup.sh first."
    exit 1
fi

# Run migrations
echo "🗄️  Running migrations..."
python manage.py migrate --noinput

# Collect static files (in development)
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Start development server
echo ""
echo "✅ Starting server at http://localhost:8000"
echo "   Admin: http://localhost:8000/admin"
echo "   API: http://localhost:8000/api/"
echo ""
echo "Press Ctrl+C to stop"
echo ""

python manage.py runserver
