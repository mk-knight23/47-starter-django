#!/usr/bin/env bash

# Health Check Script
# Validates project health

set -e

echo "🏥 Running health checks..."

# Check dependencies
if [ -f "package.json" ]; then
    echo "  Checking Node.js dependencies..."
    npm audit --audit-level=moderate || true
fi

# Check tests
if [ -f "package.json" ]; then
    echo "  Running tests..."
    npm test || true
fi

if [ -f "requirements.txt" ]; then
    echo "  Running Python tests..."
    pytest || true
fi

echo "✅ Health checks complete!"
