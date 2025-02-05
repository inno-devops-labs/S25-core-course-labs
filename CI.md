# CI for Python Project

This document outlines the best practices implemented in the CI pipeline for the Python project.

## Overview
The CI pipeline is built using GitHub Actions. It includes the following steps:
- **Python Setup and Dependency Management**
- **Code Linting**
- **Automated Testing**
- **Docker Build and Deployment**
- **Security Vulnerability Scanning**

## Pipeline Overview

### 1. **Python Setup and Dependency Management**
- **Job**: `python`
- **Key Points**:
  - **Python 3.9 Setup**: The pipeline ensures that Python 3.9 is used in the environment by leveraging the `actions/setup-python` action.
  - **Dependency Caching**: To speed up the process, the `actions/cache` action caches Python dependencies using `pip` based on the `requirements.txt` file.
  - **Install Dependencies**: The required dependencies are installed from `requirements.txt` located in the `app_python` directory. The dependencies are upgraded and installed via `pip`.

### 2. **Code Linting**
- **Job**: `linter`
- **Key Points**:
  - **Linter Setup**: The pipeline uses `flake8` for static code analysis to ensure code style compliance and catch potential issues.
  - **Install and Run Linter**: The linter is run after installing dependencies to validate Python code quality.

### 3. **Automated Testing**
- **Job**: `tests`
- **Key Points**:
  - **Test Setup**: `pytest` is used for running automated tests. The tests are executed with the `--maxfail=1`, `--disable-warnings`, and `-q` flags to limit output and stop after the first failure.
  - **Testing Dependencies**: `pytest` is installed as part of the setup process.

### 4. **Docker Build and Deployment**
- **Job**: `docker`
- **Key Points**:
  - **Docker Image Build**: The Docker image is built from the `Dockerfile` located in the `app_python` directory. The `docker build` command uses caching to optimize build times by leveraging `chr1st1na/app_python:latest` as the cache source.
  - **Docker Image Push**: After building the Docker image, it is pushed to Docker Hub under the `chr1st1na/app_python:latest` tag. The Docker login credentials are securely retrieved from GitHub Secrets.

### 5. **Security Vulnerability Scanning**
- **Job**: `snyk`
- **Key Points**:
  - **Snyk Integration**: Snyk is used to scan the dependencies for known security vulnerabilities. This is done by running `snyk test` with the `--skip-unresolved` flag to handle unresolved vulnerabilities.
  - **Installation and Scan**: Snyk is installed via `npm`, and the scan is run on the dependencies specified in `app_python/requirements.txt`.

## Best Practices Implemented

### Dependency Caching
We use `actions/cache` to cache Python dependencies. This reduces the build time and makes the pipeline more efficient, as dependencies are not reinstalled on every run.

### Efficient Docker Builds
Docker caching is enabled using the `--cache-from` option, ensuring that the build process is faster by reusing previously built layers.

### Static Code Analysis
`flake8` is used to ensure that code adheres to style guides and best practices. It is an essential part of maintaining code quality and preventing bugs related to poor code style.

### Automated Testing
We use `pytest` for automated testing to ensure that all code changes are tested before being merged. We limit the output to avoid excessive verbosity, only reporting the first failure (`--maxfail=1`).

### Security Scanning(may be added)
Snyk is integrated into the pipeline to detect vulnerabilities in the dependencies, ensuring that we proactively address security risks.

## Conclusion
This CI pipeline helps to automate key development tasks, such as dependency management, code quality checks, automated testing, Docker deployment, and vulnerability scanning. By following these practices, we ensure that the project remains secure, efficient, and maintainable.
