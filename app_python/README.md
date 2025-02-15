# Python App [![CI](https://github.com/MohamadSafi/S25-core-course-labs/actions/workflows/ci.yaml/badge.svg)](https://github.com/MohamadSafi/S25-core-course-labs/actions/workflows/ci.yaml)
## Overview

A simple Python web application built with Flask that displays the current time in Moscow (MSK). The time updates upon every page refresh.

## Features

- **Real-Time MSK**: Pulls the current time in Moscow and renders it in the browser.
- **Lightweight & Simple**: Only requires Flask and pytz to run.
- **Well-Documented**: This README and PYTHON.md explain setup, usage, and best practices.

## Installation

1. **Clone the repository**:

   ```
   git clone https://github.com/MohamadSafi/S25-core-course-labs.git
   cd S25-core-course-labs
   ```

2. **Create and activate a virtual environment** (recommended):

   ```
   python -m venv env
   source env/bin/activate  # Linux/Mac
   # or
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Flask application**:

   ```
   python main.py
   ```

2. **Open a browser** at http://127.0.0.1:5050 (if Flask is configured to run on port 5050).

   You should see the current time in Moscow displayed. Refresh the page to watch it update.

## Docker

### Build the Docker Image

To containerize the application, build the Docker image:

```
docker build -t billyboone/python-moscow-time:latest .
```

### Run the Docker Container

To run the container locally:

```
docker run --rm -p 5050:5050 billyboone/python-moscow-time:latest
```

Then open your browser at:

- **http://127.0.0.1:5050**

### Push the Docker Image to Docker Hub

If you want to push your image to Docker Hub:

### Pull and Run from Docker Hub

To pull and run the container from Docker Hub on another machine:

```
docker pull billyboone/python-moscow-time:latest

docker run --rm -p 5050:5050 billyboone/python-moscow-time:latest
```

## CI Workflow

We use **GitHub Actions** to automate linting, testing, and Docker image publishing.

**Workflow Steps**:

1. **Dependencies**: Installs required Python packages.
2. **Linter**: Runs `flake8` to enforce coding style.
3. **Tests**: Executes unit tests with `pytest`.
4. **Docker Login**: Logs into Docker Hub (using GitHub Secrets).
5. **Docker Build & Push**: Builds the container image and pushes it to Docker Hub if all tests pass.
