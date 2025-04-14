# CI/CD Best Practices for GitHub Actions

## Overview
This document outlines the best practices implemented in the GitHub Actions

## Best Practices
1. **Modular Structure**:
* `build-and-test`: Installs dependencies, runs linting, and executes unit tests.
* `security-checks`: Performs a Snyk vulnerability scan.
* `docker-build-push`: Builds and pushes the Docker image using secrets.
2. **Branch Triggers**:
* The workflow runs on `push` and `pull_request` events for the `lab3` branch only.
3. **Caching Dependencies**:
* Python dependencies are cached:
    ```bash
    cache: pip
    cache-dependency-path: |
      requirements.txt
    ```
4. **Code Quality Check**:
* `flake8` is used to enforce style consistency
    ```bash
    - name: Run Linter
      run: |
        flake8 main.py tests/test_app.py --max-line-length=88
    ```
5. **Automated Unit Tests**:
* `pytest` is used to ensure application reliability
    ```bash
    - name: Run Tests
      run: |
        pytest tests/test_app.py
    ```
6. **Security Vulnerability Scan**:
* Detect security issues in dependencies
    ```bash
    - name: Snyk Security Scan
      uses: snyk/actions/python-3.10@master
      with:
        args: --skip-unresolved app_python/
      env:
        SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
    ```
7. **Docker Build and Deployment**:
* Log In to Docker Hub using secrets
* Push to Docker Hub using secrets
8. **Job Dependencies**:
* The `security-checks` job only runs after `build-and-test` succeeds.
* The `docker-build-push` job runs only if both `build-and-test` and `security-checks` succeed.
9. **Secrets**:
* Docker Hub credentials, Snyk Token are stored securely in GitHub secrets.