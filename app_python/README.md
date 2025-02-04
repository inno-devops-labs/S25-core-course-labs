# Python Web Application: Current Time in Moscow

![CI Status](https://github.com/mazzz3r/S25-core-course-labs/actions/workflows/python-app.yml/badge.svg)

## What is it?

This is a simple web application developed using Python's Flask framework. The application displays the current time in Moscow and updates it upon each page refresh.

## Features

- **Real-Time Moscow Time:** Displays the current time in the Moscow timezone.
- **Simple and Clean Interface:** User-friendly interface with minimalistic design.
- **Easy to Deploy:** Simple setup process with clear instructions.

## Technologies Used

- **Python 3.8+**
- **Flask 2.3.2**
- **pytz 2023.3**

## Installation

### Prerequisites

- Python 3.8 or higher installed on your machine.
- `pip` package manager.

OR

- Docker installed on your machine. [Install Docker](https://docs.docker.com/get-docker/).

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/mazzz3r/S25-core-course-labs
   cd S25-core-course-labs/app_python
   ```

2. Create a Virtual Environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install Dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Application:

    ```bash
    python app.py
    ```

5. Access the Application:
    Open your web browser and navigate to <http://127.0.0.1:5000/> to view the current time in Moscow.

### Via Docker

#### Overview

Containerize the Python web application using Docker to ensure consistent environments across different platforms and simplify deployment.

#### Option 1: Pull and Run the Pre-Built Docker Image from Docker Hub

This option allows you to quickly deploy and test the application without building the Docker image yourself.

Steps:

1. Pull the Docker Image from Docker Hub

    ```bash
    docker pull mazzz3r/app_python:lab2
    ```

2. Run the Docker Container

    ```bash
    docker run -d -p 5000:5000 --name app_python_lab2 mazzz3r/app_python:lab2
    ```

3. Access the Application
Open your web browser and navigate to <http://localhost:5000/> to view the containerized application.

4. Stop and Remove the Container (Optional)

    ```bash
    docker stop app_python_lab2
    docker rm app_python_lab2
    ```

#### Option 2: Build and Run the Docker Image Locally

Building the Docker image from source provides a deeper understanding of the Dockerization process and allows for customization.

Steps:

1. Navigate to the app_python Directory

    ```bash
    cd app_python
    ```

2. Build the Docker Image

    ```bash
    docker build -t mazzz3r/app_python:lab2 .
    ```

    - Explanation:
      - -t mazzz3r/app_python:lab2: Tags the image with your username and a specific tag (lab2).
        - .: Specifies the current directory as the build context.

3. Run the Docker Container

    ```bash
    docker run -d -p 5000:5000 --name app_python_lab2 mazzz3r/app_python:lab2
    ```

4. Access the Application
Open your web browser and navigate to <http://localhost:5000/> to view the containerized application.

5. Stop and Remove the Container (Optional)

    ```bash
    docker stop app_python_lab2
    docker rm app_python_lab2
    ```

## Usage

- View Current Time: Upon accessing the application, the current time in Moscow is displayed.
- Refresh for Update: Refresh the browser page to see the updated time.

## Continuous Integration (CI) Workflow

This project implements a comprehensive CI workflow using GitHub Actions. The workflow automates building, testing, and deploying our application.

### Workflow Steps

1. **Dependencies Installation**
   - Sets up Python 3.9 environment
   - Installs required packages from requirements.txt
   - Implements caching for faster builds

2. **Code Quality Checks**
   - Runs Flake8 linter
   - Enforces PEP 8 style guide
   - Checks for syntax errors and code complexity

3. **Automated Testing**
   - Executes pytest suite
   - Validates core functionality
   - Ensures code reliability

4. **Security Scanning**
   - Uses Snyk to scan dependencies
   - Checks for known vulnerabilities
   - Monitors project dependencies

5. **Docker Integration**
   - Logs into Docker Hub
   - Builds Docker image
   - Pushes image to registry

### Triggering the Workflow

The CI pipeline automatically runs on:

- Push to main branch
- Pull request to main branch

For detailed information about our CI implementation and best practices, see [CI.md](CI.md).

## Unit Tests

The application includes comprehensive unit tests to ensure reliability and correct functionality.

### Running Tests

To run the tests:

```bash
cd app_python
pytest
```

### Test Coverage

The tests cover:

- Home page functionality
- Moscow time formatting
- Response status codes
- Content verification

For detailed information about the tests and testing practices, see `PYTHON.md`.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the Repository
2. Create a Feature Branch

    ```bash
    git checkout -b feature/YourFeature
    ```

3. Commit Your Changes

    ```bash
    git commit -m "Add Your Feature"
    ```

4. Push to the Branch

    ```bash
    git push origin feature/YourFeature
    ```

5. Open a Pull Request
