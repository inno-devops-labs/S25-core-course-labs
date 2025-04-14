# Continuous Integration (CI) Best Practices

This document outlines the best practices implemented in our CI workflow.

## Workflow Structure
- **Linting**: Uses Flake8 to enforce code style.
- **Testing**: Runs unit tests using pytest.
- **Build**: Builds and pushes a Docker image to Docker Hub.

## Optimizations
- **Caching**: Pip dependencies are cached to speed up builds.
- **Parallel Jobs**: Linting, testing, and building are split into separate jobs for better parallelism.
- **Environment Variables**: Sensitive data is stored in GitHub Secrets.

## Workflow Status
[![Python CI Workflow](https://github.com/UTKANOS-RIBA/S25-core-course-labs/actions/workflows/main.yml/badge.svg?branch=Lab3)](https://github.com/UTKANOS-RIBA/S25-core-course-labs/actions/workflows/main.yml)
