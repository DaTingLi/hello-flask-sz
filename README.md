# hello-flask-sz

A minimal Flask web service for CI/CD demonstration.

## Features

- `GET /` - Returns welcome message
- `GET /health` - Health check endpoint

## Quick Start

```bash
# Install dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run app
python app.py
```

## Deployment

- Port: 8003
- Health check: `http://localhost:8003/health`

## CI/CD

- CI: Runs on push/PR (format, lint, test, build)
- CD: Auto-deploys on merge to main
