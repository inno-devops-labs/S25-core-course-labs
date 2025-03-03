# Python Sample Application

[![CI Status](https://github.com/Raleksan/S25-core-course-labs/actions/workflows/app_python.yaml/badge.svg)](https://github.com/Raleksan/S25-core-course-labs/actions/workflows/app_python.yaml?event=push)

## Overview

This is a simple python web application that shows current time in Moscow on the `/` page.
It also returns on endpoint `/visits` number of visits to main page, application metrics on `/metrics` endpoint,
and health status on `/health` endpoint.

## Copy sources

- Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/raleksan/S25-core-course-labs -b lab2
cd S25-core-course-labs/app_python
```

## Installation

- _Optional:_ activate nix-shell environment for Nix-based systems

```bash
nix-shell -p python312 python312Packages.pip
```

- Install virtual environment and dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

- Run the application:

```bash
python3 app.py
```

- Application usage: open <http://127.0.0.1:8000> or

```bash
curl 127.0.0.1:8000
```

## Unit Tests

- To run the unit tests, use the following command:

```bash
pytest tests/tests.py
```

## Docker

- Build Docker container

```bash
docker build --tag raleksan/app_python:v0.1 .
```

- Push image into Dockerhub

```bash
docker push raleksan/app_python:v0.1
```

- Pull image from Dockerhub

```bash
docker pull raleksan/app_python:v0.1
```

- Run image

```bash
docker run -p 8000:8000 raleksan/app_python:v0.1
```

- Application usage: open <http://127.0.0.1:8000> or

```bash
curl 127.0.0.1:8000
```

## Distroless Image Version

- Build Docker container

```bash
docker build -f distroless.dockerfile --tag raleksan/app_python_distroless:v0.1 .
```

- Push image into Dockerhub

```bash
docker push raleksan/app_python_distroless:v0.1
```

- Pull image from Dockerhub

```bash
docker pull raleksan/app_python_distroless:v0.1
```

- Run image

```bash
docker run -p 8000:8000 raleksan/app_python_distroless:v0.1
```

- Application usage: open <http://127.0.0.1:8000> or

```bash
curl 127.0.0.1:8000
```

## GitHub Actions Workflow

The CI process includes the following steps:

- Runs the Black linter to ensure code formatting consistency.
- Runs unit tests using `pytest` to verify functionality.
- Performs a `Snyk` security scan to identify vulnerabilities.
- Builds a Docker image and pushes it to Docker Hub.

### CI Jobs

1. **Linting (Black)**
   - Checks that Python code in the `app_python` directory follows to the Black formatting style.

2. **Testing (Pytest)**
   - Installs dependencies and runs `pytest` on the test suite.

3. **Security Scan (Snyk)**
   - Uses `Snyk` to check for vulnerabilities in dependencies and uploads results to GitHub Code Scanning.

4. **Build and Push Docker Image**
   - Builds the Docker image using Buildx and pushes it to Docker Hub under the provided credentials.
