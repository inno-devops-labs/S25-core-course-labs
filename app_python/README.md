# App Title
**Moscow Time Web Application**

[![CI](https://github.com/spaghetti-cod3r/devops/actions/workflows/ci.yml/badge.svg?branch=lab3)](https://github.com/spaghetti-cod3r/devops/actions/workflows/ci.yml)

# Description
This is a simple Python Flask web application that fetches the current time in Moscow using TimeAPI and displays it in a visually appealing HTML interface.

# Features
- Fetches the current time in Moscow via an external API.
- Displays the time in a clean and responsive web interface.
- Handles errors gracefully and provides fallback behavior in case of issues.

# Unit Testing
The unit tests in this project are designed to ensure the reliability of core functionalities, including home page loading, API error handling, and time format validation. We applied best practices such as clear naming conventions, mocking external dependencies, and focusing each test on a single behavior. The tests follow the AAA Pattern to keep them organized and maintainable.

# Installation

## 1. On Linux Environment

### Requirements
- Linux OS
- Python 3.x
- Web browser

1. Clone the repository

2. Create a virtual environment (Recommended)
   ```bash
   python3 -m venv venv
   ```

3. Activate the created virtual environment
   ```bash
   source venv/bin/activate
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

7. To exit the app, press ```Ctrl + C```

## 2. Using Docker

### Requirements
- Docker
- Web browser

1. Pull the dockerized image from docker hub
   ```bash
   docker pull spaghettic0der/moscow-time:latest
   ```

2. Run the image on any free port (e.g. 8000)
   ```bash
   docker run -p<Your-Selected-Port>:8000 spaghettic0der/moscow-time:latest
   ```

3. Open your browser and navigate to:
   ```bash
   http://127.0.0.1:<Your-Selected-Port>
   ```

4. To stop the app, press ```Ctrl + C```

## 3. Using Docker (Distroless Image)

### Requirements
- Docker
- Web browser

1. Pull the dockerized image from docker hub
   ```bash
   docker pull spaghettic0der/distro-moscow-time:v1.0.1
   ```

2. Run the image on any free port (e.g. 8000)
   ```bash
   docker run -p<Your-Selected-Port>:8000 spaghettic0der/distro-moscow-time:v1.0.1
   ```

3. Open your browser and navigate to:
   ```bash
   http://127.0.0.1:<Your-Selected-Port>
   ```

4. To stop the app, press ```Ctrl + C```


# CI Workflow

This repository uses GitHub Actions to automate continuous integration (CI) for testing and building Docker images. The CI workflow is defined in the `.github/workflows/ci.yml` file and is triggered on `push` and `pull_request` events.


## Workflow Overview

The CI workflow performs the following steps:

1. **Checkout Code**: The latest code is checked out from the repository using the `actions/checkout` action.

2. **Set up Python**: The workflow sets up Python 3.11 using the `actions/setup-python` action.

3. **Install Dependencies**: Installs project dependencies including `Flask`, `requests`, `pytest`, `pytest-mock`, and `flake8` using `pip`.

4. **Run Linter**: The code is linted using `flake8` to ensure that it adheres to style guidelines and to catch potential issues before running tests.

5. **Run Tests**: The tests are run using `pytest` to ensure that the code is functioning correctly.

6. **Log in to Docker Hub**: The workflow logs into Docker Hub using credentials stored in GitHub Secrets (`DOCKER_USERNAME` and `DOCKER_PASSWORD`).

7. **Build Docker Image**: A Docker image is built from the `app_python` directory. The image is tagged with the `latest` tag and pushed to the repository on Docker Hub.

8. **Push Docker Image**: The Docker image is pushed to Docker Hub so it can be used in production or development environments.

## Triggering the Workflow

This workflow is triggered on the following events:
- **Push**: When code is pushed to `lab3` branch, and changes are made withing app_python directory.
- **Pull Request**: When a pull request is opened or updated on the `lab3` branch, and changes are made withing app_python directory.

## Secrets Required

To successfully run this workflow, the following secrets must be added to the GitHub repository:
- `DOCKER_USERNAME`: Your Docker Hub username.
- `DOCKER_PASSWORD`: Your Docker Hub password or an access token.

## Example of Workflow Trigger

The workflow can be triggered by pushing code or opening a pull request, like this:

```bash
git push origin main
```
