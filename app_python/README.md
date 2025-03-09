## Overview
A web application that displays Moscow time, built using Python and Flask.

## Requirements
- Python 3.x must be installed.

## Installation via Console

1. Navigate to the `app_python` directory.

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the Flask application
    ```bash
   python app.py
   
 Once the application is running, open it in your browser at http://localhost:8080.
 
## Installation via Docker

### 📥 From Docker Hub  
1. Pull the image:  
   ```bash
   docker pull vechkanovvv/app_python:v1

2. Run the container:
   ```bash
   docker run -d -p 8080:8080 vechkanovvv/app_python:v1

### 🛠️ Via Console (Build Locally)

1. Build the image:
   ```bash
   docker build -t vechkanovvv/app_python:v1 .
2. Run the container:
   ```bash
   docker run -d -p 8080:8080 vechkanovvv/app_python:v1

Now your application is running at http://localhost:8080

### CI Workflow

- **Trigger:** On push or pull request to the `master` branch.
- **Build-Test-Lint Job:**  
  - Installs dependencies.
  - Runs tests with `pytest`.
  - Checks code style using `flake8`.
- **Docker Build-Push Job:**  
  - Runs after tests pass.
  - Logs into Docker Hub using GitHub secrets.
  - Builds the Docker image from the `app_python` directory and pushes it as `latest`.

*Docker Hub credentials (`DOCKERHUB_USERNAME` and `DOCKERHUB_PASSWORD`) are stored as GitHub secrets.*

**Status**:

![CI](https://github.com/VechkanovVV/S25-core-course-labs/actions/workflows/python.yml/badge.svg)
