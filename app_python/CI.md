# Continuous Integration (CI) Documentation

## Overview
The project follows best practices for Continuous Integration (CI) using GitHub Actions. The CI pipeline is designed to ensure code quality, security, and automation of the build and test process.

## CI Workflow Steps
The CI workflow consists of the following steps:

1. **Install Dependencies**: 
   - Sets up Python 3.12.
   - Installs required dependencies using `pip`.
   
2. **Run Linter**:
   - Uses `ruff` to enforce code quality and best practices.
   
3. **Run Tests**:
   - Uses `pytest` to execute unit tests.
   - Ensures all tests pass before proceeding.
   
4. **Docker Build & Push**:
   - Logs into Docker Hub.
   - Builds the Docker image.
   - Pushes the image to a registry if required.
   
5. **Snyk Vulnerability Scan**:
   - Scans dependencies for security vulnerabilities.
   - Provides feedback on potential risks and mitigation.
   - Integrated into the CI workflow using the `snyk/actions` GitHub Action.

## Workflow Status Badge
![CI Status](https://github.com/dantetemplar/fork-S25-core-course-labs/actions/workflows/ci.yml/badge.svg)

## CI Best Practices Implemented
- **Local CI Testing**: GitHub Actions workflows were tested locally using [`act`](https://github.com/nektos/act) to avoid unnecessary commits and ensure proper functioning before pushing to the repository.
- **Optimized Build Cache**: Leveraged caching for dependencies to speed up the CI process and reduce redundant installations.
- **Minimal CI Triggering**: Configured the workflow to run only when relevant files change, preventing unnecessary builds.
- **Security Checks**: Integrated Snyk to detect and address security vulnerabilities in dependencies.
- **PR-based Workflow**: Enforced testing and linting before merging changes to the main branch.
- **Workflow Visibility**: Added status badges to track build and test results in real-time.

## Running CI Workflows Locally
To test workflows locally before pushing changes, install `act` and run:
```bash
act -P ubuntu-latest=ghcr.io/catthehacker/ubuntu:act-latest
```
This ensures that workflows execute as expected without creating unnecessary commits.

## References
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker GitHub Actions Documentation](https://docs.docker.com/ci-cd/github-actions/)
- [Snyk GitHub Actions Integration](https://docs.snyk.io/integrations/snyk-ci-cd-integrations/github-actions-integration)
