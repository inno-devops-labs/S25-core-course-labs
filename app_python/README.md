# Moscow Time Web App

Simple web application displaying current Moscow time, built with FastAPI

![Workflow Status](https://github.com/dExNight/S25-core-course-labs/actions/workflows/python-app.yml/badge.svg)

## Features
- Real-time Moscow time display
- Auto-update every second
- Clean minimal interface
- REST API endpoint

## Installation
```bash
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Usage
```bash
cd app/
uvicorn main:app --reload
```

Visit http://localhost:8000 in your browser

## Testing
```bash
pytest -v
```

## API Endpoints
- `GET /` - Main page with time display
- `GET /time` - JSON endpoint returning current Moscow time


# Docker

## Local build
```bash
docker build -t moscow-time-app .
docker run -p 8000:8000 moscow-time-app
```

## Docker Hub Image
```bash
# Download image
docker pull dexnight/moscow-time-app:latest
# Run retrieved docker container
docker run -p 8000:8000 dexnight/moscow-time-app:latest
```

## Usage
After running either local or Docker Hub image, access:
- Web Interface: http://localhost:8000

- API Documentation: http://localhost:8000/docs

### Distroless Version

A minimal, secure version of the container is available:

```bash
# Build
docker build -t python-app-distroless -f distroless.Dockerfile .

# Run
docker run -p 8000:8000 python-app-distroless
```

The distroless version provides:
- Smaller image size (73.5MB vs 154MB)

- Enhanced security

- Faster deployment


## Unit Testing

The project is covered by automated tests using pytest and FastAPI TestClient

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v
```

## Persistence

The application tracks and persists the number of visits:

- Visit counts are stored in a file within the visits directory
- Data persists between container restarts when using the volume mount
- Current visit count is visible on the main page and available via the `/visits` endpoint