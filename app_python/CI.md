# CI Workflow for `app_python`

[![CI for app_python](https://github.com/cuprum-acid/devops-labs/actions/workflows/app_python.yml/badge.svg?branch=lab3)](https://github.com/cuprum-acid/devops-labs/actions/workflows/app_python.yml)

This project uses a CI workflow to automatically lint, test, check security, and build/push Docker images whenever there are changes to the application. Below are the key steps that the workflow performs:

## 1. **Code Quality Check**

- **Linting**: The code is checked using **Pylint** to ensure it follows best practices.
- **Code Formatting**: **Black** is used to automatically check that the code is properly formatted.

## 2. **Testing**

- **Pytest** is used to run tests to verify that the code behaves as expected.

## 3. **Security Scan**

- **Snyk** is used to scan the dependencies for known vulnerabilities and security risks.

## 4. **Docker Build & Push**

- The application is built into a Docker image using **Docker Buildx**.
- The image is then pushed to **GitHub Container Registry** and **DockerHub**.

## Key Features of This CI Workflow

- **Caching**: We cache dependencies and Docker layers to speed up the workflow.
- **Security**: Credentials (like tokens and passwords) are stored securely using GitHub Secrets.
- **Fast Feedback**: The workflow runs fast by stopping early on errors and continuing with other checks.
- **Docker Integration**: The app is automatically built into a Docker image and pushed to registries.
