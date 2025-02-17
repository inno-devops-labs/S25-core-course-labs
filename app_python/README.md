# Python Web Application: Moscow Time

## Overview

This application displays the **current time in Moscow** using `Flask` and `pytz`.  
It is a lightweight service intended to demonstrate a simple time-based web application.

## Features

- **Timezone Awareness**: Automatically fetches the time in `Europe/Moscow`.
- **Easy Setup**: Minimal configuration required; just install dependencies and run.
- **Refresh for Updated Time**: On each page refresh, you get the latest Moscow time.

## Prerequisites

- Python 3.7+ (to run locally)
- Docker (ro run via Docker)
- Internet connection (to install packages)

## Installation

1. **Clone the Repository**  

   ```bash
   git clone https://github.com/anyarylova/S25-core-course-labs

   ```

2. **Navigate to the `app_python` Folder**

   ```bash
   cd app_python

   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt

   ```

   This will install
   - Flask
   - pytz  

4. **Run the Application**

   ```bash
   python app.py

   ```

5. **Open Your Browser**
   - Visit <http://localhost:5000> to see the current Moscow time.

## Docker

### Build and Run the Container Locally

1. **Build the Docker Image**  

   ```bash
   docker build -t username/appname .
   ```

2. **Run the Container**  

   ```bash
   docker run --rm -p 5000:5000 username/appname
   ```

3. **Push the Image to the Docker Hub**  

   ```bash
   docker push username/appname
   ```

### Pull and Run the Container from the Docker Hub

1. **Pull the Image from the Docker Hub**  

   ```bash
   docker pull anyarylova/app_python
   ```

2. **Run the Container**  

   ```bash
   docker run --rm -p 5000:5000 anyarylova/app_python
   ```

## Unit Tests

Python’s built-in `unittest` framework is used for the project. Unit tests cover status codes, content, time format and HTML structure of the web application. To run the tests:

1. **Install Dependencies**

   ```bash
   pip install -r requirements.txt

   ```

2. **Run the Application**

   ```bash
   python app.py

   ```

3. **Run Tests Locally**

   ```bash
   python -m unittest test_app.py

   ```

## CI Workflow

CI workflow created using GitHub Actions to build and test the project. The file `ci.yml` includes the following actions:

1. **Dependencies**: Install project dependencies.

2. **Linter**: Check code quality using `flake8`.

3. **Tests**: Automatically run unit tests.

4. **Docker**: Build and push a Docker image to DockerHub.

5. **Snyk Check**: Identify and address vulnerabilities.

## Contributors

- **Anna Rylova** - Developer.

[![ci](https://github.com/anyarylova/S25-core-course-labs/actions/workflows/ci.yml/badge.svg)](https://github.com/anyarylova/S25-core-course-labs/actions/workflows/ci.yml)
