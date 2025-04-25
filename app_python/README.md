# Python Web Application: Moscow Time

[![Python application](https://github.com/Fridorovich/S25-core-course-labs/actions/workflows/ci.yml/badge.svg)](https://github.com/Fridorovich/S25-core-course-labs/actions/workflows/ci.yml)

## Overview
This is a simple Python web application that displays the current time in Moscow. The application is built using FastAPI with Python 3.12+ based on standard Python type hints.

## Features
- Displays the current time in Moscow.
- Automatically updates the time upon page refresh.
- Interactive API documentation provided by FastAPI.

## Installation
To run this application locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Fridorovich/S25-core-course-labs/tree/lab1/app_python.git
    cd app_python
2. **Set up a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
4. **Run the application**:
    ```bash
    uvicorn main:app --reload
5. **Access the application**:
    Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Docker
This application is containerized using Docker. Below are instructions for building, running and deploying the Docker image.

### Building the Docker Image

1. Navigate to the `app_python` directory:
    ```bash
    cd app_python
    ```

2. Build the Docker image:
    ```bash
    docker build -t your_dockerhub_username/python-app:latest .
    ```
   Replace `your_dockerhub_username` with your Docker Hub username.

### Running the Docker Container

1. Run the Docker container:
    ```bash
    docker run -d -p 80:80 your_dockerhub_username/python-app:latest
    ```

2. Access the application:
    Open your browser and go to [http://localhost:80/](http://localhost:80/).

### Pushing the Docker Image to Docker Hub

1. Log in to Docker Hub:
    ```bash
    docker login
    ```

2. Push the Docker image:
    ```bash
    docker push your_dockerhub_username/python-app:latest
    ```

### Pulling and Running the Docker Image from Docker Hub

1. Pull the Docker image:
    ```bash
    docker pull your_dockerhub_username/python-app:latest
    ```

2. Run the Docker container:
    ```bash
    docker run -d -p 80:80 your_dockerhub_username/python-app:latest
    ```
   
## Unit Tests

The application includes comprehensive unit tests written using the `pytest` framework. These tests ensure the correctness of the application's functionality.

### Key Tests

1. **`test_get_moscow_time`**:
   - Verifies that the `/` endpoint correctly returns the current time in Moscow.
   - Ensures the response contains the `"moscow_time"` key.
   - Validates that the time format matches `YYYY-MM-DD HH:MM:SS`.

2. **`test_invalid_endpoint`**:
   - Checks the application's behavior when accessing invalid endpoints.
   - Confirms that a `404 Not Found` status code is returned.

3. **test_time_updates_on_reload**:
   - Checks time updates after reloading the page.

### How to Run Tests Locally

To execute the unit tests locally, follow these steps:

1. Ensure all dependencies are installed:
    ```bash
    pip install -r requirements.txt
    ```

2. Install `pytest` if it's not already installed:
    ```bash
    pip install pytest
    ```

3. Run the tests:
    ```bash
    pytest tests/
    ```
   
## CI Workflow

Continuous Integration (CI) is implemented using GitHub Actions to automate testing, linting, and Docker image building/pushing processes.

### CI Workflow Steps

1. **Checkout Code**: Clones the repository.
2. **Set Up Python**: Installs Python 3.9.
3. **Install Dependencies**: Caches and Installs project dependencies from `requirements.txt`.
4. **Run Linter**: Executes `flake8` to check code quality.
5. **Run Tests**: Executes all unit tests using `pytest`.
6. **Docker Login**: Logs into Docker Hub using secrets (`DOCKER_PASSWORD`).
7. **Build and Push Docker Image**: Builds the Docker image and pushes it to Docker Hub.

### Viewing CI Workflow Status

You can view the status of the CI workflow in the "Actions" tab of this repository on GitHub.