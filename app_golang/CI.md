# CI for Go App

## Overview

This CI pipeline automates linting, testing, security scanning, and Docker image deployment for a Go application. It ensures high code quality, security, and functionality before deploying any changes.

## Workflow Triggers

The pipeline runs on:

- **Push Events**: When changes are made to the `app_golang/` directory or the CI workflow file.
- **Pull Requests**: When modifications affect `app_golang/` or the CI workflow file.

## Jobs in the Pipeline

### 1. Linting (Golangci-lint)

Ensures that the code adheres to Go best practices and is free from style and syntax errors.

- Uses **golangci-lint** for fast and efficient linting.
- Caches Go modules to speed up execution.
- Installs `golangci-lint` from the official installation script.

### 2. Testing (Go Test)

Runs unit tests to validate the correctness and functionality of the application.

- Uses **Go test** for executing unit tests.
- Caches dependencies to optimize speed.
- Fails the pipeline if any test case fails.

### 3. Snyk Security Scan

Detects and reports vulnerabilities in the application dependencies.

- Uses **Snyk** to scan the `app_golang/` directory.
- Requires a `SNYK_TOKEN` secret for authentication.
- Skips unresolved dependencies to avoid unnecessary failures.

### 4. Build and Push Docker Image

Automates building and pushing a Docker image to a container registry.

- Logs into **Docker Hub** using `secrets.DOCKER_USERNAME` and `secrets.DOCKER_PASSWORD`.
- Builds a Docker image with the tag `latest`.
- Pushes the image to the repository.

## Best Practices Implemented

### Dependency Caching

- Caches Go build and module dependencies using **GitHub Actions cache action** to improve speed.
- Reduces redundant downloads, enhancing efficiency and speeding up subsequent builds.

### Strict Failure Handling

- Linting and testing must pass before security scans and Docker image building.
- Each job ensures that failures are caught early to prevent further issues down the pipeline.

### Security Enforcement

- Integrates **Snyk** to scan for vulnerabilities in dependencies.
- Ensures that security issues are identified and addressed before deploying the application.

### Docker Best Practices

- Uses **Buildx** for better Docker build performance and multi-platform support.
- Ensures only validated and tested code is pushed to the Docker registry.

### Environment Variables and Secrets

- `SNYK_TOKEN` → Required for security scanning with Snyk.
- `DOCKER_USERNAME / DOCKER_PASSWORD` → Used for authenticating with Docker Hub for image pushing.
