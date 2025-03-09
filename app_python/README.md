# Python Web Application: Current Date in Moscow

[![Python CI/CD Pipeline](https://github.com/creepydanunity/S25-core-course-labs/actions/workflows/python-ci.yml/badge.svg?branch=lab3)](https://github.com/creepydanunity/S25-core-course-labs/actions/workflows/python-ci.yml)

## Overview
This web application built with **FastAPI** to display the current formatted date and time in Moscow. The application dynamically updates the date whenever the page is refreshed.

## Features
- Displays the current date in Moscow (`dd.mm.YYYY HH:MM:SS` format).
- Dynamically updates on page refresh.
- Lightweight and high-performance using **FastAPI**.
- Clean HTML design.

## Installation

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/creepydanunity/S25-core-course-labs.git
   cd app_python

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the application:
    ```bash
    uvicorn main:app --reload

4. Access at:
    http://127.0.0.1:8000

## Docker

### Build the container
```sh
docker build -t fastapi-mt .
```

### Run the container
```sh
docker run -p 8000:8000 fastapi-mt
```

### Run via Docker Hub
```sh
docker pull iucd/fastapi-mt:latest
docker run -p 8000:8000 iucd/fastapi-mt
```

## Distroless Image Version

### Build the container
```sh
docker build -t fastapi-mt:distroless -f distroless.Dockerfile .
```

### Run the container
```sh
docker run -p 8000:8000 fastapi-mt:distroless
```

### Run via Docker Hub
```sh
docker pull iucd/fastapi-mt:distroless
docker run -p 8000:8000 iucd/fastapi-mt:distroless
```

## Unit Tests
Unit tests have been implemented to ensure the correctness and reliability of the application. The tests cover the following key scenarios:

1. **Homepage Loading**:
   - Ensures the main page loads successfully with a valid HTTP response and contains the expected HTML structure.

2. **Time Format Validation**:
   - Extracts the displayed Moscow time from the response and verifies that it follows the expected `dd.mm.YYYY HH:MM:SS` format.

3. **Time Accuracy Validation**:
   - Compares the extracted Moscow time with the actual Moscow time at the moment of request to ensure accuracy (within a few seconds tolerance).

### Running Tests
To execute the tests, use the following command:
```sh
pytest test_main.py
```

## Continuous Integration (CI)
The project includes a GitHub Actions CI workflow to automate testing and Docker builds. The workflow consists of:

1. **Build and Test**:
   - Checks out the repository.
   - Sets up Python and installs dependencies.
   - Runs a linter for code quality checks.
   - Executes unit tests to validate functionality.

2. **Docker Build and Push**:
   - Logs in to Docker Hub using GitHub Secrets.
   - Builds the Docker image.
   - Pushes the images (original and distroless) to Docker Hub.!

## Application Upgrade for Persistence
### Visits
- Done:
   1. Implemented a counter logic to keep track of the number of times `/` (main) page is accessed
   2. Counter number is being saved into `app_data/visits.txt` file which is mounted on the host machine to `app_python/app_data/visits.txt`
   3. `docker-compose.yml` created to include a new volume with `visits` file
   4. Endpoint `/visits` introduced to check the current number of counted visits
- How to run:
   1. Clone the repository, switch to branch `lab12` and move to the app folder:
   ```bash
   git clone https://github.com/creepydanunity/S25-core-course-labs.git
   git checkout lab12
   cd app_python
   ```
   2. Run docker-compose:
   ```bash
   docker-compose up --build -d
   ```
   3. Access web app and check `app_python/app_data/visits.txt` for counting number of visits.