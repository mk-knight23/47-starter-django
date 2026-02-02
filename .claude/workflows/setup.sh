#!/bin/bash
# Django Project Setup Workflow
# This script sets up a new Django project from scratch

set -e

echo "🚀 Django Starter Setup"
echo "========================"
echo ""

# Check Python version
echo "📋 Checking Python version..."
python3 --version || { echo "❌ Python 3 not found. Please install Python 3.10+"; exit 1; }

# Create virtual environment
echo ""
echo "🔧 Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
echo "📦 Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Copy environment file
echo "⚙️  Setting up environment..."
if [ ! -f .env.local ]; then
    cp .env.example .env.local
    echo "✅ Created .env.local - Please update with your values"
else
    echo "ℹ️  .env.local already exists"
fi

# Run migrations
echo ""
echo "🗄️  Running migrations..."
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo ""
echo "👤 Creating superuser..."
echo "Please enter superuser credentials:"
python manage.py createsuperuser

# Collect static files
echo ""
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Create logs directory
mkdir -p logs

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start the development server:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Admin will be available at: http://localhost:8000/admin"
echo ""
