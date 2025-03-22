# CI Workflow for `app_ruby`

[![CI for app_ruby](https://github.com/cuprum-acid/devops-labs/actions/workflows/app_ruby.yml/badge.svg)](https://github.com/cuprum-acid/devops-labs/actions/workflows/app_ruby.yml)

This project uses a CI workflow to automatically lint, test, check security, and build/push Docker images whenever there are changes to the application. Below are the key steps that the workflow performs:

## 1. **Code Quality Check**

- **Linting**: The code is checked using **RuboCop** to enforce Ruby style and best practices.
- **Code Formatting**: **RuboCop** also ensures that the code is properly formatted.

## 2. **Testing**

- **RSpec** is used to run tests and verify that the application works as expected.

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
