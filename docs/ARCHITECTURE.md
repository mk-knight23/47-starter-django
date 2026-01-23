# Architecture: 22-django-starter

## Overview
A high-performance full-stack starter kit integrating Django 4 (Backend) and React 19 (Frontend). It follows a "Monolithic Orchestration" pattern where Django handles the secure API layer, ORM, and administrative tasks, while React 19 provides a high-fidelity, technical management interface.

## Tech Stack
-   **Frontend**: React 19
-   **Build Tool**: Vite 6
-   **Styling**: Tailwind CSS v4
-   **Animations**: Framer Motion 12
-   **Backend**: Python 3.12 / Django 4.2+
-   **Package Managers**: npm (JS) and uv (Python)

## Core Logic
-   **Backend Orchestrator**: `manage.py` and `web_project/` handle the Django runtime, migrations, and security protocols (CSRF, XSS).
-   **Frontend Hub**: `src/App.tsx` provides the primary dashboard for developer interactions and framework diagnostics.
-   **Terminal Simulation**: Animated command-line interface for educational bootstrapping sequences.
-   **Security Layer**: Integrated battle-tested Django security features with modern React 19 state management.

## Performance
-   Native React 19 rendering for millisecond-range UI updates.
-   Vite 6 optimized bundling for instant frontend availability.
-   Tailwind v4 native architecture for minimal CSS overhead in complex management layouts.
-   Django optimized ORM queries for efficient database communication.
