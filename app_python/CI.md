# Continuous Integration (CI) Best Practices

## Overview

This document outlines the best practices implemented in the **Python CI Workflow** for ensuring code quality, security, and automation in the development process.

## CI Workflow Badge

[![Python CI Workflow](https://github.com/vladislav77777/S25-core-course-labs/actions/workflows/app_python.yaml/badge.svg?branch=lab_03)](https://github.com/vladislav77777/S25-core-course-labs/actions/workflows/app_python.yaml)

## Best Practices Implemented

### 1. **Code Linting**

- Uses `flake8` to enforce PEP8 coding standards.
- Prevents stylistic errors and ensures consistency in the codebase.
- Configured to allow a maximum line length of 88 characters.

### 2. **Dependency Management**

- Installs dependencies from `requirements.txt` to ensure consistency across environments.
- Uses `pip` to upgrade itself before installing dependencies.
- Verifies that all required packages are installed correctly.

### 3. **Automated Testing**

- Runs unit tests using `unittest` to validate application functionality.
- Ensures all test cases pass before merging changes.

### 4. **Security Scanning**

- Integrates **Snyk Security Scan** to detect vulnerabilities in dependencies.
- Runs security checks with a severity threshold of `high`.

### 5. **Docker Integration**

- Builds and pushes a Docker image to **Docker Hub**.
- Uses `docker/login-action@v2` for secure authentication.
- Automates containerization and deployment.

### 6. **GitHub Actions Optimization**

- Uses **`actions/checkout@v4`** for efficient repo access.
- Runs jobs in parallel (`build`, `testing`, `docker`) to speed up workflows.
- Defines specific paths for triggering CI to reduce unnecessary runs.
