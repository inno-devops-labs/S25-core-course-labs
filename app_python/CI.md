# Continuous Integration (CI) Best Practices

[![CI workflow python app](https://github.com/zDragonLORD1010/S25-core-course-labs/actions/workflows/app_python_ci.yml/badge.svg)](https://github.com/zDragonLORD1010/S25-core-course-labs/actions/workflows/app_python_ci.yml)

### 1. Workflow structure and optimization

- **Separate Jobs for Efficiency:**
  - The CI workflow is split into **build-and-test**, **docker**, and **security-scan jobs**.
  - This structure ensures that failures are detected early, and builds are not pushed if tests fail.

- **Using `needs` to control execution flow:***
  - The `docker` and `security-scan` jobs depend on `build-and-test` to **ensure only passing builds proceed further**.

- **Caching dependencies for faster builds:**
  - GitHub Actions caches Python dependencies using `pip cache dir` to reduce redundant installations.

### 2. Essential CI Workflow Steps

- **Dependency installation:**
  - Uses `pip install --upgrade pip` to ensure the latest package manager version.
  - Installs dependencies from requirements.txt before running tests and security scans.

- **Code linting with `flake8`:**
  - Ensures code follows Python best practices and avoids syntax errors.
  - Configured in the workflow to stop the pipeline if critical linting errors occur.

- **Automated testing with `pytest`:**
  - Ensures that all unit tests pass before proceeding.
  - Prevents broken code from being deployed.

- **Security scanning with `Snyk`:**
  - Identifies vulnerabilities in dependencies.
  - Uses `--skip-unresolved` to prevent failures due to optional dependencies.

### 3. Docker Integration

- **Secure login to Docker Hub:**
  - Uses GitHub Secrets (**_DOCKER_USERNAME_** and **_DOCKER_PASSWORD_**) to authenticate securely.

- **Building and pushing Docker images:**
  - The image is built and tag, then push to Docker Hub securely:
```bash
docker build -t app_python:latest .
docker tag app_python:latest ${{ secrets.DOCKER_USERNAME }}/app_python:latest
docker push ${{ secrets.DOCKER_USERNAME }}/app_python:latest
```

### 4. CI Workflow Enhancements

- **Adding a CI status Badge**

- **Optimizing workflow efficiency**
  - Uses parallel jobs to speed up execution.
  - Ensures failing steps prevent further execution to avoid wasted resources.

- **Enhancing Docker security**
  - Docker images are scanned for vulnerabilities before deployment.
