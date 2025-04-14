# Python Sample Application

![workflow](https://github.com/mihdenis85/s25-core-course-labs/actions/workflows/app_python.yaml/badge.svg)

## Overview

This is a simple python web application that shows current Moscow time.

## Installation and running

- Clone this repository and go to the project directory:

```bash
git clone https://github.com/mihdenis85/S25-core-course-labs.git -b lab1
cd S25-core-course-labs/app_python
```

- Install virtual environment and all dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- Run the application (via `gunicorn`) and test:

```bash
python -m gunicorn --bind 0.0.0.0:8080 app:app
curl localhost:8080
```

## Docker

### Build

```bash
cd S25-core-course-labs/app_python
docker build --tag docker_username/app_python:v1.0 .
```

Instead of docker username, use your own one.

### Pull and Run

```bash
docker pull mihdenis85/app_python:v1.0
docker run -p 8080:8080 mihdenis85/app_python:v1.0
```

## Unit Tests

1. Application availability

   Verifies that the application is accessible and operational.

2. HTML integrity

   Ensures that the returned HTML is well-formed and free from errors.

3. Time accuracy

   Confirms that the displayed time is correct, excluding milliseconds.

## CI Workflow

### Setup

1. CI starts with linting by `black` linter (`lint` job).
2. Then it installs dependencies and after that it runs `pytest` (`test` job).

### SNYK

After two jobs above completed, `snyk_check` job runs.

### Building Docker image & Deploying

1. First of all the job starts with logging into Dockerhub using
   `DOCKER_USERNAME` and `DOCKER_TOKEN` repo secrets.
2. Then it builds and pushes an image to the Dockerhub.
3. The build process is cached to enhance the efficiency of future pipeline executions.
