# Python Web Application

[![CI Status](https://github.com/maksalena/S25-core-course-labs/actions/workflows/ci.yml/badge.svg)](https://github.com/maksalena/S25-core-course-labs/actions/workflows/ci.yml)


## Overview

This Python web application displays the **current time in Moscow**, dynamically updating each time the page is refreshed. It is built using the Flask framework.

## Features

- Displays the current Moscow time.
- Updates dynamically when refreshed.
- Visits counting logic.

## Installation

### Prerequisites

- **Python 3.7+** must be installed on your system. If not installed, use Homebrew:

  ```bash
  brew install python3
  ```

## Steps to Install and Run

1. Clone the repository:

  ```bash
git clone <repository_url>
cd app_python
  ```

2. (Optional) Set up a virtual environment:

  ```bash
python3 -m venv venv
source venv/bin/activate
  ```

3. Install dependencies:

  ```bash
pip install -r requirements.txt
  ```
  
4. Run the application:

  ```bash
python3 app.py
  ```
  
5. Open your browser and navigate to:
<http://127.0.0.1:5000/>

## Requirements

The application relies on the following dependencies:

- **Flask**: A lightweight web framework for Python.
- **pytz**: Library for accurate timezone handling.

You can install these dependencies using:

  ```bash
pip install -r requirements.txt
  ```
  
## .gitignore

This project includes a .gitignore file to prevent unnecessary files from being tracked.

## Containerization - Docker

Prerequisites:

- Docker installed on your system ([Install Docker](https://docs.docker.com/get-docker/))
- Python application in the `app_python` folder
- A public Docker Hub account ([Sign up here](https://hub.docker.com/))

## Steps

### How to Build the Docker Image?

- Navigate to the `app_python` directory:

     ```bash
     cd app_python
     ```

- Build the Docker image:

     ```bash
     docker build -t your_dockerhub_username/app_python:latest .
     ```

### How to Pull the Docker Image?

- Pull the image from Docker Hub:

     ```bash
     docker pull your_dockerhub_username/app_python:latest
     ```

### How to Run the Docker Image?

- Run the image:

     ```bash
     docker run -p 8080:8080 your_dockerhub_username/app_python:latest
     ```

- Open your browser and visit: `http://127.0.0.1:8080`

## Unit Tests

1. **Test `/` route response**:
   - Ensures the Moscow time page loads successfully.
   - Validates status code `200 OK`.

2. **Test `/` route content**:
   - Confirms the page contains the correct "Current Moscow Time:" text.
   - Ensures the response includes valid HTML.

### Running Tests Locally

```bash
python -m unittest discover tests/
```

### GitHub Actions Workflow

This project uses GitHub Actions for Continuous Integration (CI). The CI process:

- Installs dependencies
- Runs a linter (flake8)
- Runs unit tests
- Logs in to Docker Hub, builds the image, and pushes it

## Author

Alyona Maksimova

Email: <a.maksimova@innopolis.university>
