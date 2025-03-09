# FastAPI app

![CI Status](https://github.com/Poxidq/S25-core-course-labs/actions/workflows/ci.yml/badge.svg)


- Shows the current time in Moscow.
- Error handling for 404 (Not Found) and 500 (Internal Server Error) scenarios.
- Logging to track server activity and errors.
- Static file serving for CSS.

## Local Installation
```bash
git clone URL
cd app_python
pip install -r requirements.txt
chmod +x server.sh
server.sh
```

## Testing

```
cd app_python/app
pytest test_app.py --disable-warnings -v 

```

## Logs
Logs are saved to app.log and printed to the console.

## Docker 

```bash
docker pull jlfkajlkifj/python-web-app:latest
docker run -d -p 8000:8000 jlfkajlkifj/python-web-app:latest
```

## CI 
This project utilizes GitHub Actions for CI, which includes:

- Dependency installation & caching
- Code linting (black)
- Unit tests (pytest)
- Security scanning (Snyk)
- Docker build & push

# Moscow Time Web Application

A simple web application that displays the current time in Moscow and tracks visitor counts.

## Features

- Displays the current time in Moscow
- Tracks and displays the number of visits
- Persists visit count data using a volume

## Endpoints

- `/` - Home page showing Moscow time
- `/visits` - Shows the number of times the application has been visited

## Running with Docker Compose

```bash
docker-compose up
```

The application will be available at http://localhost:8000

## Persistence

The application maintains a visit counter that persists between container restarts using a volume mount. The counter is stored in a file named `visits` in the mounted volume.