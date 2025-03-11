# Python Web Application: Current Moscow time

## Project Overview

This Python web application is designed to display the current time in Moscow, dynamically updating the time on each page refresh. The application is built using the **FastAPI** framework, ensuring high performance, developer-friendly design, and adherence to modern coding standards.

## Technologies used

- **FastAPI:** developer-friendly web framework which ensures safe and effective app programming.
- **pytz:** Python library for precise time zone handling, ensuring accurate conversion and retrieval of the current time in Moscow (or any other timezone).

## Features

1. **Dynamic Time Updates:**
The application displays the current Moscow time, refreshing dynamically on each page reload.
2. **Modular Design:**
The logic for fetching the Moscow time is encapsulated in a separate function, promoting reusability and readability.
3. **Error Handling:**
The application gracefully handles unexpected errors using a ```try-except``` block, ensuring reliability in various scenarios.

## Installation and Usage

Clone the repository:

```bash
git clone https://github.com/Pupolina7/S25-core-course-labs.git
```

Navigate to the folder:

```bash
cd S25-core-course-labs/
```

Create virtual environment:

commands for MacOS

```bash
python -m venv env
source env/bin/activate
```

Navigate to the ```app_python``` folder:

```bash
cd app_python/
```

Install necessary dependencies:

```bash
pip install -r requirements.txt
```

Run the application locally:

```bash
uvicorn app:app --reload
```

Go to localhost:

```bash
http://127.0.0.1:8000
```

## Docker

### How to build?

Navigate to ```app_python``` if you are not already in:

```bash
cd app_python/
```

Build the Docker image locally:

```bash
docker build -t moscow-time-app .
```

### How to pull?

Pull the Docker image from Docker Hub:

```bash
docker pull pupolina7/moscow-time-app:latest
```

### How to run?

Run the container locally:

```bash
docker run -p 8000:8000 pupolina7/moscow-time-app:latest
```

Go to localhost:

```bash
http://localhost:8000
```

## Unit Tests

This project includes unit tests to ensure the correctness of the application.

### Running Tests

Navigate to ```app_python``` if you are not already in:

```bash
cd app_python/
```

Run tests and see the report:

```bash
pytest test_app.py
```

Expected result:

```bash
============================= test session starts =============================
...
collected 3 items                                                              

tests/test_app.py ...                                                  [100%]

============================== 3 passed in 0.12s ==============================
```

## CI Workflow

![CI/CD Pipeline](https://github.com/Pupolina7/S25-core-course-labs/actions/workflows/python_ci.yml/badge.svg)

### Overview

This project uses **GitHub Actions** to automate building, testing, and deploying the application. The CI/CD pipeline consists of:

1. **Dependency Installation**
2. **Code Linting**
3. **Running Tests**
4. **Docker Login, Build & Push**

### How CI Workflow works

- **On every push or pull request to ```master```**, GitHub Actions:
  1. Installs dependencies.
  2. Runs a Python linter (```flake8```) to enforce code style.
  3. Runs all unit tests using ```pytest```.

- **On successful testing**, the workflow:
  1. Logs into Docker Hub.
  2. Builds the Docker image.
  3. Pushes the image to Docker Hub.

## Security Scan with Snyk

This project integrates **Snyk** for vulnerability scanning of Python dependencies.

### How It Works

- Every **push or pull request** triggers a **Snyk security scan**.
- If vulnerabilities are found, the workflow fails, preventing unsafe deployments.

## New Counter Feature

This version of the application implements a counter that tracks the number of times the application is accessed. The count is persisted to a file and can be viewed via a new endpoint.

### Endpoints

- **GET /**  
  Increments the counter and returns a message with the current count.
- **GET /visits**  
  Returns the current visit count as JSON.

### Volume Mapping

The Docker Compose file mounts a volume (`./visits`) to `/app/visits` in the container so that the visits file is persisted on the host.

### How to Verify

1. Run the application:

```bash
docker-compose up -d
```
