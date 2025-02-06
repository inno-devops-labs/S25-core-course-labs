# Python Web Application - Current Time in Moscow

## Overview
This is a simple Python web application on the Flask displays the current time in Moscow.
It uses the `pytz` library to handle the time zone for Moscow.

## Features
- Displays the current time in the Moscow timezone.
- Time updates automatically on page refresh.

## Requirements
- Python
- Flask
- pytz

### Running the Application

```bash
pip install -r requirements.txt
python lab1.py
```

# Docker

## The application automatically installs all dependencies and runs inside the container.

## How to build?

```bash
docker build -t lab2:latest .
```

## How to run?

```bash
docker run -d -p 5000:5000 lab2
```
## How to pull?

```bash
docker pull ksenon9/lab2:latest
docker run -p 5000:5000 ksenon9/lab2:latest
```

# Unit Tests
This project includes unit tests to ensure the correctness of the application. The tests are located in the `lab3_tests.py` file and are run automatically as part of the CI workflow.
To run the tests locally, use the following command:

```bash
pytest lab3_tests.py
```

# CI Workflow

This project uses GitHub Actions for Continuous Integration (CI). The CI workflow is defined in the `.github/workflows/python-ci.yml` file and automates the process of building, testing, and deploying the application.

## Workflow Steps

1. **Dependencies**: Installs the necessary Python dependencies
   
2. **Linter**: The linter (Flake8) checks the project for style issues and potential errors.

3. **Tests**: Runs the unit tests to ensure that the application behaves as expected.

4. **Docker Integration**:
   - Logs into Docker Hub using credentials stored in GitHub Secrets.
   - Builds the Docker image for the project.
   - Pushes the Docker image to Docker Hub.

## Secrets Configuration

For the Docker Hub login step, you need to set up the following GitHub secrets:
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

# Badge
[![Python CI](https://github.com/Akvadevka/S25-core-course-labs/actions/workflows/python-ci.yml/badge.svg)](https://github.com/Akvadevka/S25-core-course-labs/actions/workflows/python-ci.yml)