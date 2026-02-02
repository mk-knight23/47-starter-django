#!/bin/bash
# Create Django Superuser
# Quick script to create a superuser without prompts

set -e

echo "👤 Creating Django Superuser"
echo "============================="
echo ""

# Get user input
read -p "Email: " email
read -sp "Password: " password
echo
read -sp "Confirm Password: " password_confirm
echo

if [ "$password" != "$password_confirm" ]; then
    echo "❌ Passwords do not match"
    exit 1
fi

# Create superuser using Django shell
python manage.py shell << EOF
from users.models import User
try:
    user = User.objects.create_superuser(
        email='$email',
        password='$password',
        first_name='Admin',
        last_name='User'
    )
    print(f"✅ Superuser created: {user.email}")
except Exception as e:
    print(f"❌ Error creating superuser: {e}")
    exit(1)
EOF

echo ""
echo "✅ Superuser created successfully!"
echo "   Email: $email"
echo "   Login at: http://localhost:8000/admin"
echo ""
