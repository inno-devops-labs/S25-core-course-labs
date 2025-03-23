![CI Workflow Status](https://github.com/Friedox/S25-core-course-labs/actions/workflows/ci.yml/badge.svg)

# Python Web App

## Overview

This web application displays the current time in Moscow using the Flask framework. The time is shown both digitally and on an analog clock.

## Features

- **Time Display**: Shows the current time in Moscow.
- **Flask Framework**: Used for handling web requests and rendering templates.
- **Modular Design**: Code is separated into Python, CSS, and JavaScript files.

## Installation

1. Clone the repository:

    ```bash
    git clone git clone https://github.com/Friedox/S25-core-course-labs.git
    ```

2. Navigate to the project directory:

    ```bash
    cd app_python
    ```

3. Set up a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

    ```bash
    venv\Scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the application:

    ```bash
    python app.py
    ```

7. Open the browser and go to `http://127.0.0.1:5000/` to check the app

## Docker

### Build the Docker Image

To build the Docker image for this application, run the following command:

   ```bash
   docker build -f Dockerfile -t app-python .
   ```

### Run the Docker Image

   ```bash
   docker run --name app-python-container -p 5000:5000 app-python
   ```

### Pull the Docker Image

   ```bash
   docker pull your-docker-username/app-python:latest
   ```

## Unit Tests

This repository includes unit tests to ensure the application works as expected. The tests use [pytest](https://docs.pytest.org/) and can be run locally by installing the dependencies and executing:

```bash
pytest
```

## Visit Counter

- The app now counts the number of times the main page (`/`) is visited.
- The counter is saved to a file called `visits.txt` inside `/app/data`.
- A Docker volume maps `./data` on the host to `/app/data` inside the container, ensuring the counter persists between container restarts.
- You can check the current visit count:
  - By visiting the endpoint: `http://localhost:5000/visits`
  - By opening the file on the host:
    ```bash
    cat ./data/visits.txt
    ```
- To reset the counter manually:
    ```bash
    echo 0 > ./data/visits.txt
    ```

## Continuous Integration (CI)

This project uses GitHub Actions for CI. The workflow is triggered on pushes and pull requests to the `main` branch and includes the following steps:

- **Dependencies**: Installs the required Python packages.
- **Linter**: Runs `flake8` to check code style.
- **Tests**: Executes unit tests using `pytest`.

Once these steps pass, the workflow proceeds with Docker operations:

- **Login**: Logs into Docker Hub using stored secrets.
- **Build**: Builds the Docker image using the provided Dockerfile.
- **Push**: Tags and pushes the Docker image to Docker Hub.

For further details, refer to the [GitHub Actions workflow configuration](.github/workflows/ci.yml).