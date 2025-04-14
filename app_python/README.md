# Flask Web Application: Moscow Time

[![Flask Web Application (Moscow Time)](https://github.com/Mohammed-Nour/S25-core-course-labs/actions/workflows/python-app.yml/badge.svg)](https://github.com/Mohammed-Nour/S25-core-course-labs/actions/workflows/python-app.yml)

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Running the Application](#running-the-application)
5. [Testing](#testing)
6. [Unit Tests](#unit-tests)
7. [Docker](#docker)
8. [Distroless Image Version](#distroless-image-version)
9. [CI Workflow](#ci-workflow)
10. [Code Quality Checks](#code-quality-checks)
11. [Author](#author)

---

## Overview

The application displays the current time in the Moscow timezone (`Europe/Moscow`). It is built using Flask, a lightweight Python web framework, and uses `pytz` for timezone handling.

---

## Prerequisites

Before proceeding, ensure you have the following installed:

- **Python 3.x**: Flask requires Python 3.6 or later. If you don't have Python installed, follow the official [Python installation guide](https://www.python.org/downloads/).
- **pip3**: Python's package installer. It usually comes preinstalled with Python.
- **Virtual Environment**: A virtual environment is recommended to isolate the project dependencies.

---

## Installation

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone git@github.com:Mohammed-Nour/S25-core-course-labs.git
cd S25-core-course-labs/app_python
```

### 2. Set Up a Virtual Environment

A virtual environment is used to isolate the application's dependencies. Follow the steps below to set it up:

#### Linux/macOS

1. Install the `venv` module (if not already installed):

    ```bash
    sudo apt install python3-venv
    ```

2. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

#### Windows

1. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    ```bash
    venv\Scripts\activate
    ```

### 3. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip3 install -r requirements.txt
```

---

## Running the Application

1. Ensure the virtual environment is activated (you should see `(venv)` in your terminal prompt).
2. Set the `FLASK_APP` environment variable:
   - **Linux/macOS**:

     ```bash
     export FLASK_APP=app.py
     ```

   - **Windows**:

     ```bash
     set FLASK_APP=app.py
     ```

3. Run the Flask application:

   ```bash
   flask run
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000/`.

   > **Note**: The application will start a development server on `http://127.0.0.1:5000/`. You can stop the server by pressing `Ctrl+C` in the terminal.

---

## Testing

To ensure the application works correctly:

1. Run the application and verify that the displayed time matches the current time in Moscow.
2. Refresh the page to confirm that the time updates dynamically.

---

## Unit Tests

Unit tests have been implemented to validate the functionality of the application. These tests ensure that the application behaves as expected and adheres to best practices. The tests are written using the `pytest` framework and cover the following scenarios:

- **Home Route**: Ensures the home route (`/`) returns a 200 status code.
- **HTML Structure**: Verifies that the response contains an `<h1>` tag with the current time in Moscow.
- **Time Accuracy**: Validates that the time displayed on the page matches the current time in Moscow.
- **Time Format**: Ensures the time is displayed in the correct format (`HH:MM:SS`).
- **Timezone**: Verifies that the time is correctly localized to the Moscow timezone.

### **Running the Tests**

To run the unit tests, follow these steps:

1. Ensure the virtual environment is activated.
2. Install the test dependencies (if not already installed):

   ```bash
   pip3 install -r requirements.txt
   ```

3. Run the tests using `pytest`:

   ```bash
   pytest tests app.py
   ```

   > **Note**: The `pytest` command will automatically discover and run all test files in the `tests` directory.

---

## Docker

This application is containerized using Docker, following best practices for building and running Docker images.

### How to Build the Docker Image

1. Navigate to the `app_python` directory:

   ```bash
   cd S25-core-course-labs/app_python
   ```

2. Build the Docker image:

   ```bash
   docker build -t oshaheen1882051/app_python:app_python-prod-1.0.0 --no-cache=True .
   ```

   - The `--no-cache=True` flag ensures a clean build by ignoring cached layers.

### How to Run the Docker Image

1. Run the Docker container:

   ```bash
   docker run -d -p 5000:5000 --name app_python oshaheen1882051/app_python:app_python-prod-1.0.0
   ```

2. Access the application at `http://localhost:5000`.

### How to Push the Docker Image to Docker Hub

1. Log in to Docker Hub (if not already logged in):

   ```bash
   docker login
   ```

2. Push the Docker image:

   ```bash
   docker push oshaheen1882051/app_python:app_python-prod-1.0.0
   ```

### How to Pull the Docker Image from Docker Hub

1. Pull the Docker image:

   ```bash
   docker pull oshaheen1882051/app_python:app_python-prod-1.0.0
   ```

2. Run the container as described in the "How to Run the Docker Image" section.

---

## Distroless Image Version

This application is also available in a **Distroless** version, which is a minimal Docker image that only includes the application and its runtime dependencies, without unnecessary tools or package managers.

### How to Build the Distroless Docker Image

1. Navigate to the `app_python` directory:

   ```bash
   cd S25-core-course-labs/app_python
   ```

2. Build the Distroless Docker image:

   ```bash
   docker build -t oshaheen1882051/app_python:app_python-distroless-prod-1.0.0 --file distroless.Dockerfile --no-cache=True .
   ```

   - The `--file distroless.Dockerfile` flag specifies the custom Dockerfile for the Distroless build.
   - The `--no-cache=True` flag ensures a clean build by ignoring cached layers.

### How to Run the Distroless Docker Image

1. Run the Distroless Docker container:

   ```bash
   docker run -d -p 5000:5000 --name app_python_distroless oshaheen1882051/app_python:app_python-distroless-prod-1.0.0
   ```

2. Access the application at `http://localhost:5000`.

### How to Push the Distroless Docker Image to Docker Hub

1. Log in to Docker Hub (if not already logged in):

   ```bash
   docker login
   ```

2. Push the Distroless Docker image:

   ```bash
   docker push oshaheen1882051/app_python:app_python-distroless-prod-1.0.0
   ```

### How to Pull the Distroless Docker Image from Docker Hub

1. Pull the Distroless Docker image:

   ```bash
   docker pull oshaheen1882051/app_python:app_python-distroless-prod-1.0.0
   ```

2. Run the container as described in the "How to Run the Distroless Docker Image" section.

---

## CI Workflow

This repository uses GitHub Actions to automate the build, test, and deployment processes. The CI workflow is defined in the file and incorporates the following key features:

- **Trigger Conditions**:  
  The workflow runs on:
  - **Push events** on the `lab3` and `master` branches when changes occur in the `app_python` folder.
  - **Pull requests** targeting the `master` branch (also filtered to changes in the `app_python` folder).

- **Workflow Jobs**:  
  The CI pipeline is divided into three main jobs:
  1. **Security**:  
     - Runs Snyk vulnerability checks to detect and flag known security issues in the project.
  2. **Build & Test**:  
     - Installs project dependencies.
     - Executes linting using Flake8 and Pylint.
     - Runs unit tests using pytest.
  3. **Docker**:  
     - Login into Docker Hub.
     - Sets up the necessary build environment with QEMU and Docker Buildx.
     - Builds and pushes both a standard Docker image and a distroless version.
  
- **Efficiency and Best Practices**:  
  - The workflow makes use of caching for pip dependencies and Docker layers to speed up build times.
  - The integration of Snyk enhances security by continuously scanning for vulnerabilities.
  - The status badge at the top of this README provides immediate visibility into the current build status.

---

## Code Quality Checks

To ensure the code adheres to best practices and coding standards, the following tools are used:

### 1. **Pylint**

Pylint is a static code analysis tool that checks for errors, enforces coding standards, and provides suggestions for improving code quality.

Run Pylint on the `app.py` file:

```bash
pylint app.py
```

### 2. **Flake8**

Flake8 is a tool that combines PyFlakes, pycodestyle, and McCabe complexity checks to ensure the code follows PEP 8 standards and is free of common errors.

Run Flake8 on the `app.py` file:

```bash
flake8 app.py
```

---

## Author

- **Name**: Mohamad Nour Shahin
- **Email**: <mo.shahin@innopolis.university>