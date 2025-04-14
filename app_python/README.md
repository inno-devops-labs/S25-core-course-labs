# Moscow time API

![CI/CD Pipeline](https://github.com/NikaChek/S25-core-course-labs/actions/workflows/ci.yml/badge.svg?branch=lab3)

## Project Overview

The web application that provides the current time in Moscow.

## Technologies used

* FastAPI: web framework
* pytz: Python library for precise time zone handling

## Features

* Current time display: the web application displays the current time in Moscow.
* Dynamic update: the displayed time is updated when the page is refreshed.

## Quick start without Docker

1. Clone the repository:

   ``` bash
   git clone git@github.com:NikaChek/S25-core-course-labs.git
   ```

2. Navigate to the project folder:

   ``` bash
   cd S25-core-course-labs/app_python
   ```

3. Install dependencies:

   ``` bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ``` bash
   uvicorn main:app --reload
   ```

5. Access the application in your browser at <http://127.0.0.1:8000>.

## Docker section

This application has been containerized using Docker to make deployment easier and consistent. Below are the steps to build, pull, and run the Docker container.

### How to Build the Docker Image

1. Clone the repository:

   ``` bash
   git clone git@github.com:NikaChek/S25-core-course-labs.git
   ```

2. Navigate to the project folder:

   ``` bash
   cd S25-core-course-labs/app_python
   ```

3. Build the Docker image

   ``` bash
   docker build -t moscow-time-api .
   ```

### How to Pull the Docker Image

1. Pull the image from Docker Hub

   ``` bash
   docker pull nikachek/moscow-time-api:latest
   ```

### How to Run the Docker Container

1. Start the container

   ``` bash
   docker run -p 8000:8000 moscow-time-api
   ```
  
   If you're running the image from Docker Hub, use the following command:
  
   ``` bash
   docker run -p 8000:8000 nikachek/moscow-time-api:latest
   ```

2. Access the application in your browser at <http://127.0.0.1:8000>.

## Unit Tests

This project includes unit tests to ensure the reliability of the Moscow Time API.

### Running Tests

To execute unit tests, run the following command from the app_pyrthon folder:

```bash
   pytest tests/
```

## CI/CD Workflow with GitHub Actions

This project uses **GitHub Actions** to automate testing, linting, and Docker image deployment.

### **CI/CD Pipeline Overview**

Whenever code is pushed to the `lab3` branch or a pull request is created, the **GitHub Actions CI/CD pipeline** runs the following steps:

1. **Install Dependencies** → Ensures all required Python packages are installed.
2. **Run Linter (`flake8`)** → Checks for code formatting issues.
3. **Run Tests (`pytest`)** → Runs unit tests to verify application functionality.
4. **Build and Push Docker Image** → If tests pass, a Docker image is built and pushed to **Docker Hub**.

### **How the Workflow Works**

* **CI/CD Triggers:**
  * Runs on **every push** to `lab3`.
  * Runs on **pull requests** to `lab3`.
* **Test Execution:**
  * Runs `pytest` to validate API behavior.
* **Linting:**
  * Uses `flake8` to check code style.
* **Docker Deployment:**
  * If all tests pass, the workflow **builds and pushes the Docker image** to Docker Hub.
