# CI/CD Best Practices for GitHub Actions

## Overview
This document outlines the best practices implemented in the GitHub Actions

## Best Practices
1. **Workflow Triggers**: The pipeline runs on `push` and `pull_request` events for the `lab3` branch.
2. **Job Structure**:
* `build-and-test-node`: Handles dependency installation, linting, and testing.
* `security-checks-node`: Runs security scans using Snyk
* `docker-build-push-node`: Builds and pushes a secure Docker image
3. **Dependency Caching**: Uses `cache: 'npm'` in setup-node to speed up dependency installation.
4. **Environment Variables**: Uses GitHub Secrets (`DOCKER_USERNAME, DOCKER_PASSWORD, SNYK_TOKEN`) to manage sensitive credentials securely.