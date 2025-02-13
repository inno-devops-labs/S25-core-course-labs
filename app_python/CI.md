# Continuous Integration (CI) Pipeline

### Overview
This document describes the CI/CD pipeline implemented for the `app_python` project. The workflow ensures code quality, security, and automated testing before deployment.

## Workflow Steps

### 1. **Build and Test Stage**
- **Checkout Code:** The repository is checked out using GitHub Actions.
- **Setup Python Environment:** Python 3.11 is installed.
- **Dependency Management:**
  - Dependencies are cached using GitHub Actions' cache.
  - Missing dependencies are installed via `pip`.
- **Security Scan (Snyk):**
  - The project is scanned for vulnerabilities in dependencies.
- **Linting (Flake8):**
  - Code is checked for style violations.
- **Unit Tests (Pytest):**
  - Tests are run using `pytest` with coverage reports.

### 2. **Docker Build & Deployment Stage**
- **Login to Docker Hub:** Authentication is performed using GitHub Secrets.
- **Docker Image Build:**
  - Caching is enabled for faster builds.
  - The `latest` tag is assigned to the built image.
- **Push to Docker Hub:**
  - The built image is pushed to the registry.

## Technologies Used
- **GitHub Actions** for CI/CD automation
- **Flake8** for code linting
- **Pytest** for unit testing
- **Snyk** for security scanning
- **Docker** for containerization

## How to Run CI Locally
If you want to test the pipeline locally before pushing:

1. **Run Linter:**
   ```bash
   flake8 app_python/
   ```
2. **Run Unit Tests:**
   ```bash
   PYTHONPATH=. pytest --cov=app_python.app --cov-report=xml
   ```
3. **Run Docker Build Locally:**
   ```bash
   docker build -t local/app_python app_python/
   ```