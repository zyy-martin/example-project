# Example Project: Project Zenith

A modern, lightweight local development stack using **FastAPI** for the backend and a **Vanilla HTML/CSS/JS** frontend.

- Python 3.14+
- PostgreSQL 15+
- `pip`

## Project Structure

- `backend/`: FastAPI application and database logic.
  - `app/main.py`: Entry point for the FastAPI server.
  - `app/database/`: Database models, connection, and initialization.
  - `requirements.txt`: Backend dependencies.
- `frontend/`: Dashboard frontend files.
  - `index.html`: Main UI.
- `scripts/`: Development and testing automation.
  - `test_e2e.sh`: Script for "clean state" testing with transient Docker DB.
- `docker-compose.yml`: Local infrastructure definition.

## Database Setup

1. **Configure Environment**: Copy `backend/.env.example` to `backend/.env` and set your `DATABASE_URL`.
2. **Initialize Database**:

    ```bash
    cd backend
    python3 -m app.database.init
    ```

## Development & Testing

### Clean-State E2E Test

To verify the entire system from scratch (spins up a fresh DB, initializes, tests, and tears down):

```bash
./scripts/test_e2e.sh
```

### Manual Quick Start

1. **Backend**:

    ```bash
    cd backend
    source ../.venv-fastapi/bin/activate
    python3 -m app.main
    ```

2. **Frontend**: Open `frontend/index.html` in your browser.

## API Endpoints

- `GET /api/status`: Returns the current system status and a greeting message.

## Teardown

### 1. Stop the Server

Press `Ctrl + C` in the terminal where the backend is running.

### 2. Deactivate Virtual Environment

```bash
deactivate
```

## Troubleshooting

### Port Already In Use

If you see an error like `[Errno 48] address already in use` for port 5001, it means another instance of the server is running. You can find and kill the process with:

```bash
# Find the process ID (PID)
lsof -i :5001

# Kill the process
kill -9 <PID>
```

## Development Standards

This project follows the isolation standards defined in the `LOCAL_DEVELOPMENT_GUIDE.md`. Specifically:

- Use isolated virtual environments for tasks.
- Maintain a branch-per-task Git workflow.
- Dependencies are pinned in `requirements.txt`.
