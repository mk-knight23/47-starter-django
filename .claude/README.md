# Django Starter - Claude Workflows

This directory contains automated workflows and scripts for Django development.

## Workflows

### setup.sh
Initial project setup:
- Creates virtual environment
- Installs dependencies
- Sets up environment files
- Runs migrations
- Creates superuser

```bash
bash .claude/workflows/setup.sh
```

### dev.sh
Start development server:
- Runs migrations
- Collects static files
- Starts Django dev server

```bash
bash .claude/workflows/dev.sh
```

### test.sh
Run tests with coverage:
- Runs pytest
- Generates coverage report
- Outputs to terminal and HTML

```bash
bash .claude/workflows/test.sh
```

### deploy.sh
Prepare for production:
- Validates environment
- Runs migrations
- Collects static files
- Shows deployment commands

```bash
bash .claude/workflows/deploy.sh
```

## Scripts

### createsuperuser.sh
Create admin user without prompts:
```bash
bash .claude/scripts/createsuperuser.sh
```

### reset-db.sh
Reset database (WARNING: deletes all data):
```bash
bash .claude/scripts/reset-db.sh
```

## Git Hooks

### pre-commit.sh
Runs before commit:
- Linting with Ruff
- Formatting with Black
- Type checking with MyPy
- Quick test run

Install:
```bash
ln -f .claude/hooks/pre-commit.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### pre-push.sh
Runs before push:
- Full test suite
- Coverage check (80% minimum)

Install:
```bash
ln -f .claude/hooks/pre-push.sh .git/hooks/pre-push
chmod +x .git/hooks/pre-push
```

## Quick Start

1. Initial setup:
```bash
bash .claude/workflows/setup.sh
```

2. Start development:
```bash
bash .claude/workflows/dev.sh
```

3. Run tests:
```bash
bash .claude/workflows/test.sh
```

4. Deploy to production:
```bash
bash .claude/workflows/deploy.sh
```
