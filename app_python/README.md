# Python Web Application
[![CI Pipeline](https://github.com/Kartofanych/S25-core-course-labs/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/Kartofanych/S25-core-course-labs/actions/workflows/ci.yml)

## Overview

This project is a time-tracking web application that displays the current Moscow time and provides real-time updates to
the user. The application is built using Flask.

## Features

- Real-time clock update using JavaScript and Flask.
- Clean and user-friendly interface.
- Easy deployment using requirements.txt.

## Prerequisites

Make sure you have Python 3.x and libraries from requirements.txt installed on your system.

## Docker

### How to build?
```
podman build -t app_python .
```

### How to pull?
```
podman pull docker.io/kartofanych/app_python:latest
```
   
### How to run?
```
podman run -p 8080:8080 app_python
```

## Unit Tests

To run the unit tests, execute the following command:
```
pytest tests/
```
м
## CI

1. **Dependencies**: Installs Python dependencies.
2. **Linter**: Runs `flake8` to check for code style issues.
3. **Tests**: Runs unit tests using `pytest`.
4. **Docker Build**: Builds the Docker image.
5. **Docker Push**: Pushes the Docker image to Docker Hub.
6. **Snyk**: Scans the project for vulnerabilities in dependencies.

To view the workflow, check the `.github/workflows/ci.yml` file.

## Vulnerability Scanning

This project uses [Snyk](https://snyk.io/) to identify and address vulnerabilities in dependencies. To view the latest scan results, check the Snyk dashboard.