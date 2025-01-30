# Moscow time app

This application provides an endpoint that displays the current Moscow time. It's built with [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Linting and Formatting](#linting-and-formatting)

## Installation

1. **Clone the repository:**

    ```bash
        git clone https://github.com/yourusername/my-fastapi-app.git
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

1. **Run the FastAPI server:**

    ```bash
    python run.py
    ```

2. **Access the main endpoint:**

    Visit `http://127.0.0.1:8000` to see the current Moscow time displayed.

## Testing

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
