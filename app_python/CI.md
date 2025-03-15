# CI for Python App

## Overview

This CI pipeline automates linting, testing, security scanning, and Docker image deployment for a Python application. It ensures high code quality and security before deploying any changes.

## Workflow Triggers

The pipeline runs on:

- **Push Events**: When changes are made to the `app_python/` directory.
- **Pull Requests**: When modifications affect `app_python/` or the CI workflow file.

## Jobs in the Pipeline

### 1. Linting (Ruff)

Ensures that the code follows Python best practices and is free from style and syntax errors.

- Uses **Ruff** for fast linting.
- Caches Python dependencies to speed up execution.

### 2. Testing (Pytest)

Runs unit tests to validate the correctness of the application.

- Uses **pytest** for test execution.
- Caches dependencies to optimize speed.
- Fails the pipeline if any test case does not pass.

### 3. Snyk Security Scan

Detects and reports vulnerabilities in the application dependencies.

- Uses **Snyk** to scan the `app_python/` directory.
- Requires a `SNYK_TOKEN` secret for authentication.
- Skips unresolved dependencies to avoid unnecessary failures.

### 4. Build and Push Docker Image

Automates building and pushing a Docker image to a container registry.

- Logs into **Docker Hub** using `secrets.DOCKER_USERNAME` and `secrets.DOCKER_PASSWORD`.
- Builds a Docker image with the tag `latest`.
- Pushes the image to the repository.

## Best Practices Implemented

### Dependency Caching

- Caches dependencies using **GitHub Actions cache action** to improve speed.
- Reduces redundant installations, enhancing efficiency.

### Strict Failure Handling

- Linting and testing must pass before proceeding to security checks and building and pushing an image.

### Security Enforcement

- Integrates **Snyk** to scan for vulnerabilities.
- Ensures that security issues are identified before deploying the application.

### Parallel Execution

- Linting and testing run in parallel to reduce execution time.
- Security scans are executed only after passing tests.

### Docker Best Practices

- Uses **Buildx** for better Docker build performance.
- Ensures only validated code is pushed to production.

### Environment Variables and Secrets

- `SNYK_TOKEN` → Required for security scanning.
- `DOCKER_USERNAME / DOCKER_PASSWORD` → Used for Docker Hub authentication.
