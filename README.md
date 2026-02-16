# Example Project: Project Zenith

A modern, lightweight local development stack using **FastAPI** for the backend and a **Vanilla HTML/CSS/JS** frontend.

## Project Structure
- `app.py`: FastAPI backend application.
- `index.html`: Modern dashboard frontend.
- `requirements.txt`: Python dependencies.
- `.venv-fastapi/`: Task-isolated virtual environment (recommended).

## Prerequisites
- Python 3.14+
- `pip`

## Quick Start

### 1. Environment Setup
Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv .venv-fastapi
source .venv-fastapi/bin/activate
pip install -r requirements.txt
```

### 2. Run the Backend
Start the FastAPI server (it will run on [http://localhost:5001](http://localhost:5001)):

```bash
python3 app.py
```

### 3. Open the Frontend
Simply open `index.html` in your web browser. It will automatically attempt to connect to the backend at `localhost:5001`.

## API Endpoints
- `GET /api/status`: Returns the current system status and a greeting message.

## Development Standards
This project follows the isolation standards defined in the `LOCAL_DEVELOPMENT_GUIDE.md`. Specifically:
- Use isolated virtual environments for tasks.
- Maintain a branch-per-task Git workflow.
- Dependencies are pinned in `requirements.txt`.
