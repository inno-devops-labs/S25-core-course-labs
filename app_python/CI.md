# CI Best Practices

## Overview

This document outlines the best practices implemented in the GitHub Actions CI workflow for the app_python project.

## Best Practices

### 1. Automated Testing and Linting

Runs unit tests with pytest to ensure code correctness.

Uses flake8 for linting to enforce code quality.

### 2. Dependency Caching

Caches Python dependencies using actions/cache to speed up workflows.

Caches Docker layers to optimize image builds.

### 3. Security Scanning

Integrates Snyk to scan dependencies for vulnerabilities.

### 4. Efficient Job Dependencies

docker job depends on build-and-test, ensuring tests pass before building images.

Security checks run independently to avoid blocking builds.

### 5. Optimized Workflow Triggers

Runs on push and pull_request for relevant branches (main, lab3).

Limits execution to changes in .github/workflows/ and app_python/.

By following these best practices, the CI workflow ensures reliability, security, and efficiency.
