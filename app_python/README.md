# Moscow Time Web Application

![Python App CI](https://github.com/raydenoir/S25-core-course-labs/actions/workflows/app_python.yml/badge.svg)

Simple Python web application for Lab 1 that displays the current time in Moscow. It is built using the FastAPI framework and Jinja2 templating for rendering the HTML page.

## Requirements

- Python 3.9+
- Dependencies listed in `requirements.txt`
  or
- Docker

## Docker

### How to build?

```bash
docker build -t app_python:alpine .
```

### How to pull

```bash
docker pull raydenoir/app_python:alpine
```

### How to Run

```bash
docker run -p 127.0.0.1:<desired_port>:8000 -d --name app_python-alpine app_python:alpine
```

## Docker Distroless Image Version

### How to build?

```bash
docker build -f distroless.Dockerfile -t app_python:distroless .
```

### How to pull

```bash
docker pull raydenoir/app_python:distroless
```

### How to Run

```bash
docker run -p 127.0.0.1:<desired_port>:8000 -d --name app_python-distroless app_python:distroless
```

## Manual Setup

1. Clone the repository

2. Make sure you're in the python application directory

   ```bash
   cd ./app_python
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
uvicorn app.main:app --reload
```

## Using the Application

Go to <http://127.0.0.1:8000/time> (in case it runs locally)

## Unit Tests

To run unit tests, use

```bash
pytest
```

## Continuous Integration (CI)

### Workflow Triggers

- The CI workflow runs **only when files inside the `app_python/` directory change**.

### Workflow Steps

1. **Dependencies**: Installs required dependencies.
2. **Linter**: Runs `flake8` to ensure code quality.
3. **Tests**: Runs `pytest` to validate functionality.
4. **Static Code Analysis**: Performs static code analysis with Snyk.
5. **Docker Build & Push (Distroless)**: Builds and pushes the `distroless` Docker image.

Test results and Snyk findings are uploaded as artifacts.

The Docker image is built using the `distroless.Dockerfile` and pushed to Docker Hub as `app_python:distroless`.
