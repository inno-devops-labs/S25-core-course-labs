# Continuous Integration (CI) Best Practices

## Overview

This document outlines the best practices implemented in the **Web App CI Workflow** for ensuring code quality, security, and automation in the development process.

## CI Workflow Badge

[![Web App CI Workflow](https://github.com/vladislav77777/S25-core-course-labs/actions/workflows/app_javascript.yaml/badge.svg?branch=lab_03)](https://github.com/vladislav77777/S25-core-course-labs/actions/workflows/app_javascript.yaml)

## Best Practices Implemented

### 1. **Code Linting**

- Uses `eslint` to enforce JavaScript coding standards.
- Uses `stylelint` to ensure CSS consistency.
- Prevents stylistic errors and enforces best practices.

### 2. **Dependency Management**

- Uses `npm ci` for deterministic package installations.
- Caches dependencies to speed up builds.
- Ensures a stable and reproducible environment.

### 3. **Automated Testing**

- Runs Jest unit tests to validate application functionality.
- Mocks timers and dependencies to optimize test execution.
- Ensures all test cases pass before deployment.

### 4. **Security Scanning**

- Integrates **Snyk Security Scan** to detect vulnerabilities.
- Uses a severity threshold of `high` for security alerts.
- Prevents merging insecure dependencies.

### 5. **Docker Integration**

- Builds and pushes a Docker image to **Docker Hub**.
- Uses `docker/login-action@v2` for secure authentication.
- Automates containerization and deployment.

### 6. **GitHub Actions Optimization**

- Uses **`actions/checkout@v4`** for efficient repo access.
- Caches `npm` dependencies to speed up workflows.
- Defines specific paths for triggering CI to avoid unnecessary runs.

