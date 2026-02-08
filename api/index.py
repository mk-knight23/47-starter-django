"""
Vercel serverless entry point for Django.
"""
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Set environment variables
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Import Django WSGI handler
from django.core.wsgi import get_wsgi_application

# Create application
application = get_wsgi_application()

# Vercel expects 'app' variable
app = application
