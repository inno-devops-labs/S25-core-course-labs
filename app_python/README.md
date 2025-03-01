# Moscow time app

![CI Workflow Status](https://github.com/Egor-Salnikov/S25-core-course-labs/ci/badge.svg)

This application provides an endpoint that displays the current Moscow time. It's built with [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Linting and Formatting](#linting-and-formatting)

## Installation

1. **Clone the repository:**

    ```bash
        git clone git@github.com:Egor-Salnikov/S25-core-course-labs.git
        cd devops/S25-core-course-labs/app_python
    ```

2. **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    export PYTHONPATH=$PYTHONPATH:$(pwd)
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Build docker image**

    For this you'll need a docker runing in your environment

    ```bash
    docker build --no-cache -t time_app .
    ```

2. **Run the FastAPI server:**

    ```bash
    docker run -d -p 8000:8000 time_app
    ```

3. **Access the main endpoint:**

    Visit `http://localhost:8000` to see the current Moscow time displayed.

3. **Access the visits endpoint:**

    Visit `http://localhost:8000/visits` to see the number of visits.

## Unit tests

Tests are written using `pytest`.

1. **Run tests:**

    ```bash
    pytest tests
    ```

## Linting and Formatting

This project uses `flake8` for linting and `black` for code formatting.

1. **Linting with Flake8:**

    ```bash
    flake8 .
    ```

2. **Formatting with Black:**

    ```bash
    black .
    ```
