# Getting Started with Django Starter

This guide will help you set up and run the Django Starter project.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10 or higher** - [Download Python](https://www.python.org/downloads/)
- **Node.js 18 or higher** - [Download Node.js](https://nodejs.org/)
- **Git** - [Download Git](https://git-scm.com/downloads)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mk-knight23/47-starter-django.git
cd 47-starter-django
```

### 2. Backend Setup (Django)

#### Option A: Automated Setup (Recommended)

```bash
bash .claude/workflows/setup.sh
```

This automated script will:
- Create a Python virtual environment
- Install all dependencies
- Copy environment configuration files
- Run database migrations
- Prompt you to create a superuser
- Collect static files

#### Option B: Manual Setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Copy environment file
cp .env.example .env.local

# Edit .env.local with your configuration
# nano .env.local  # or use your preferred editor

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

### 3. Frontend Setup (React)

```bash
# Install dependencies
npm install

# Note: The frontend is already configured and ready to run
```

## Running the Application

### Start Backend Server

```bash
# Activate virtual environment (if not already active)
source venv/bin/activate

# Start development server
python manage.py runserver
```

Or use the workflow script:
```bash
bash .claude/workflows/dev.sh
```

Backend will be available at:
- **Admin**: http://localhost:8000/admin
- **API Root**: http://localhost:8000/api/
- **Auth**: http://localhost:8000/api/auth/

### Start Frontend Server

Open a new terminal and navigate to the project directory:

```bash
npm run dev
```

Frontend will be available at:
- **Application**: http://localhost:5173

## Default Login

Use the superuser credentials you created during setup to access:
- Django Admin: http://localhost:8000/admin
- API: Use token authentication at `/api/auth/login/`

## Project Structure Overview

```
47-starter-django/
├── config/              # Django configuration (settings, URLs, WSGI)
├── users/               # Custom user app with email authentication
├── apps/                # Django applications
│   └── blog/           # Example CRUD app (Posts, Categories, Tags)
├── static/             # Static files (CSS, JS, images)
├── templates/          # Django templates
├── media/              # User uploaded files
├── src/                # React frontend
├── .claude/            # Claude workflows and scripts
├── logs/               # Application logs
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Common Tasks

### Create a New Django App

```bash
python manage.py startapp myapp apps/
```

This creates a new app in the `apps/` directory. Don't forget to:
1. Add `'apps.myapp.apps.MyappConfig'` to `INSTALLED_APPS` in `config/settings.py`
2. Create URLs in `apps/myapp/urls.py` and include them in `config/urls.py`

### Run Migrations

```bash
# Create new migrations after model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

Or use the script:
```bash
bash .claude/scripts/createsuperuser.sh
```

### Collect Static Files

```bash
python manage.py collectstatic
```

### Reset Database

**WARNING: This will delete all data!**

```bash
bash .claude/scripts/reset-db.sh
```

### Run Tests

```bash
bash .claude/workflows/test.sh
```

Or manually:
```bash
pytest --cov=. --cov-report=html
```

### Access Django Shell

```bash
python manage.py shell
```

Example usage:
```python
from users.models import User
user = User.objects.create_user(email='test@example.com', password='testpass')
user.is_staff = True
user.save()
```

## Configuration

### Environment Variables

Edit `.env.local` to configure:

```bash
# Secret key (generate with: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
SECRET_KEY=your-secret-key-here

# Debug mode (set to False in production)
DEBUG=True

# Allowed hosts
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=sqlite:///db.sqlite3

# CORS (for frontend)
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

### Database Configuration

**Development (SQLite - Default):**
```bash
DATABASE_URL=sqlite:///db.sqlite3
```

**Production (PostgreSQL):**
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

Install PostgreSQL adapter:
```bash
pip install psycopg[binary]
```

## API Usage

### Authentication

1. **Register:**
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "securepass", "password_confirm": "securepass"}'
```

2. **Login (get token):**
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "securepass"}'
```

3. **Use token:**
```bash
curl -X GET http://localhost:8000/api/users/me/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

### Blog Endpoints

```bash
# List posts
curl http://localhost:8000/api/blog/posts/

# Create post (requires authentication)
curl -X POST http://localhost:8000/api/blog/posts/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"title": "My Post", "content": "Post content", "status": "PUBLISHED"}'

# Get post detail
curl http://localhost:8000/api/blog/posts/my-post/
```

## Troubleshooting

### Port Already in Use

If port 8000 is in use:
```bash
# Use a different port
python manage.py runserver 8001
```

### Migration Errors

```bash
# Reset migrations (WARNING: deletes data)
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
python manage.py makemigrations
python manage.py migrate
```

### Static Files Not Loading

```bash
# Recollect static files
python manage.py collectstatic --clear --noinput
```

### Import Errors

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## Development Tools

### Django Admin

Access at: http://localhost:8000/admin

Features:
- User management
- Blog post management
- Content management
- Site configuration

### Django Debug Toolbar

Automatically enabled in DEBUG mode. Provides:
- SQL query analysis
- Request/response information
- Template rendering times
- Cache information

### API Testing

Use tools like:
- **Postman** - https://www.postman.com/
- **Insomnia** - https://insomnia.rest/
- **HTTPie** - `pip install httpie`

Example with HTTPie:
```bash
http POST http://localhost:8000/api/auth/login/ email=user@example.com password=pass
```

## Production Deployment

See the main README.md for detailed deployment instructions.

Quick start:

1. Set `DEBUG=False` in `.env.local`
2. Set strong `SECRET_KEY`
3. Configure production database
4. Collect static files
5. Run with Gunicorn:
```bash
gunicorn -c config/gunicorn.py config.wsgi:application
```

## Next Steps

- Explore the custom user model in `users/models.py`
- Check out the blog app example in `apps/blog/`
- Review API views and serializers
- Customize the admin dashboard
- Add your own apps and features

## Support

For issues and questions:
- GitHub Issues: https://github.com/mk-knight23/47-starter-django/issues
- Documentation: Check the `docs/` directory
- Django Docs: https://docs.djangoproject.com/
- DRF Docs: https://www.django-rest-framework.org/

Happy coding! 🚀
