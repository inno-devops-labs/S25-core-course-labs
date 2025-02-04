# Flask Web Application – Moscow Time

## Overview
This is a simple **Flask web application** that displays the **current time in Moscow (MSK)** and updates upon page refresh.  

The project follows **best practices**, including:
- Clean code with **PEP8** standards.
- Proper **virtual environment** management.
- Minimal and clear **requirements.txt**.
- Well-structured **Markdown documentation**.

---

## Installation & Setup
- Clone the repository.
- Install **requirements** from requirements.txt.
- Open folder **app_python**.
- Run **app.py**.

---

## Docker
**How to build?**  
  
- Use **docker build -t utkanosss/moscow-time-app .**  
  
**How to pull?**  
  
- Use **docker pull utkanosss/moscow-time-app**  
  
**How to run?**  
  
- Use **docker run --rm -p 5000:5000 utkanosss/moscow-time-app**

---

Repository link: https://hub.docker.com/repository/docker/utkanosss/moscow-time-app/general

---

## Continuous Integration (CI) Workflow

This project uses GitHub Actions to automate the build, test, and deployment processes. The CI workflow is defined in the [`.github/workflows/python-ci.yml`](.github/workflows/python-ci.yml) file.

### Workflow Overview

The CI workflow consists of the following jobs:

1. **Linting**:
   - Runs Flake8 to enforce code style and check for syntax errors.
   - Configuration: Max line length is set to 88 characters.

2. **Testing**:
   - Installs project dependencies using `pip`.
   - Runs unit tests using `pytest`.
   - Caches Python dependencies to speed up the workflow.

3. **Security Scanning**:
   - Uses [Snyk](https://snyk.io/) to scan for vulnerabilities in the project dependencies.
   - Requires a `SNYK_TOKEN` secret to authenticate with Snyk.

4. **Docker Build and Push**:
   - Builds a Docker image for the application.
   - Pushes the Docker image to Docker Hub.
   - Requires `DOCKER_USERNAME` and `DOCKER_PASSWORD` secrets to authenticate with Docker Hub.


Workflow status check in CI.md
