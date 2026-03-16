#!/usr/bin/env bash

# Setup Script
# Automates initial project setup

set -e

echo "🚀 Setting up project..."

# Detect package manager
if [ -f "package.json" ]; then
    echo "📦 Installing Node.js dependencies..."
    npm install
fi

if [ -f "requirements.txt" ]; then
    echo "🐍 Installing Python dependencies..."
    pip install -r requirements.txt
fi

if [ -f "pyproject.toml" ]; then
    echo "🐍 Installing Python dependencies (poetry)..."
    poetry install
fi

echo "✅ Setup complete!"
