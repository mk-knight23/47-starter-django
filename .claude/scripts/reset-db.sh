#!/bin/bash
# Reset Django Database
# WARNING: This will delete all data!

set -e

echo "⚠️  WARNING: This will delete all data!"
echo "======================================"
echo ""
read -p "Are you sure? (yes/no): " confirm

if [ "$confirm" != "yes" ]; then
    echo "Aborted."
    exit 0
fi

# Activate virtual environment
if [ -d venv ]; then
    source venv/bin/activate
fi

# Delete database file
echo "🗑️  Deleting database..."
rm -f db.sqlite3
rm -f db.sqlite3-shm
rm -f db.sqlite3-wal

# Run migrations
echo "🗄️  Running migrations..."
python manage.py migrate

# Create superuser
echo ""
echo "👤 Creating superuser..."
bash .claude/scripts/createsuperuser.sh

echo ""
echo "✅ Database reset complete!"
echo ""
