# Moscow Time Web Application

A simple Python web application built with **FastAPI** that displays the current time in **Moscow (MSK)**.

---

# Workflow Status

[![CI/CD Pipeline](https://github.com/Nikoali01/S25-core-course-labs/actions/workflows/ci.yml/badge.svg?branch=lab_3&event=push)](https://github.com/Nikoali01/S25-core-course-labs/actions/workflows/ci.yml)

---

## Overview

This application serves an HTML page displaying the current time in **Moscow (MSK)**. It uses the `pytz` library to ensure accurate timezone handling and includes an image of Moscow for visual appeal.

---

## Features

- Displays the current time in **Moscow** in a bold, centered format.
- Includes an image of Moscow for visual appeal.
- Lightweight and minimalistic implementation.

---

## Local Installation

### Prerequisites

- Python 3.8 or higher installed.
- Install the required dependencies using `pip`.

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Nikoali01/S25-core-course-labs
   git checkout lab1
   cd app_python
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the Application**
    ```bash
    http://127.0.0.1:8000/time/moscow
    ```

## Docker

### Introduction
The application can be containerized using Docker to ensure consistency across different environments. This section provides instructions on how to build, pull, and run the Docker image.

### How to Build?

To build the Docker image, navigate to the `app_python` directory and run the following command:

```bash
docker build -t region-time-api .
```

### How to Pull?

You can pull the project from Dockerhub, example in my case:

```bash
docker pull nickwidbestie/region-time-api:latest
```

### How to Run?

#### Running Pulled Image

After pulling the image, you can run it with the following command.

```bash
docker run -d -p 80:80 nickwidbestie/region-time-api:latest
```

#### Running Locally Built Image

After building the image locally, you can run it with the following command:

```bash
docker run -d -p 80:80 region-time-api
```

Once the container is running, you can access the application at:

```bash
http://localhost/time/moscow
```


## Unit Tests

This project includes unit tests implemented using the `pytest` framework. The tests ensure the correctness of the `get_location_time` function by covering the following scenarios:
- Valid timezone input (e.g., `Europe/Moscow`).
- Invalid timezone input (raises a `ValueError` with an appropriate error message).
- Edge-case timezones (e.g., `Etc/GMT+12`).
- Timezones with special characters (e.g., `America/New_York`).

To run the tests locally, execute the following command from the root directory:
```bash
pytest app_python/tests/
```

## CI Workflow

This project uses **GitHub Actions** for continuous integration and deployment. The CI workflow automates testing, security checks, and Docker image management to ensure code quality and reliability. Below is a detailed breakdown of the workflow:

1. **Checkout Repository**:
   - Clones the repository to the GitHub Actions runner using the `actions/checkout@v3` action.

2. **Set Up Python**:
   - Configures the environment with Python 3.9 using the `actions/setup-python@v4` action.

3. **Cache Dependencies**:
   - Caches installed Python dependencies to improve build efficiency. The cache key is based on the contents of `app_python/requirements.txt`.

4. **Install Dependencies**:
   - Installs Python packages listed in `app_python/requirements.txt` using `pip`.

5. **Lint Code**:
   - Ensures code quality by running `flake8` on the `app_python` folder to enforce PEP 8 standards.

6. **Run Tests**:
   - Executes unit tests located in `app_python/tests/` using `pytest` to validate application functionality.

7. **Install Snyk**:
   - Installs the **Snyk CLI** globally using `npm`.

8. **Run Snyk Vulnerability Check**:
   - Scans `app_python/requirements.txt` for vulnerabilities using **Snyk**, ensuring secure dependencies. The Snyk API token is securely stored as a GitHub secret (`SNYK_TOKEN`).

9. **Log in to Docker Hub**:
   - Authenticates with Docker Hub using credentials stored as GitHub secrets (`DOCKER_USERNAME` and `DOCKER_PASSWORD`).

10. **Build Docker Image**:
    - Builds a Docker image using the `Dockerfile` located in the `app_python` folder. The image is tagged with the commit SHA for traceability.

11. **Push Docker Image**:
    - Pushes the built Docker image to Docker Hub for deployment.

---

### Workflow Configuration

The CI workflow is defined in `.github/workflows/ci.yml`. It is triggered on:
- Every push to the `lab_3` branch.
- Opening a pull request against the `lab_3` branch.

---

### Enhancements

1. **Dependency Caching**:
   - Added caching for Python dependencies to reduce redundant downloads and improve build times.

2. **Security Checks**:
   - Integrated **Snyk** to identify and address vulnerabilities in dependencies, ensuring a secure application.

3. **Code Quality**:
   - Enforced code quality with `flake8` for linting and `pytest` for unit testing.

4. **Docker Optimization**:
   - Ensured the Docker image is built and pushed securely to Docker Hub, with tagging based on the commit SHA for traceability.