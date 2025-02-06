# CI Implementation Documentation

## Workflow Overview
The CI pipeline is implemented using GitHub Actions and includes security scanning with Snyk. The workflow runs on Ubuntu latest and is triggered by:
- Push events to the master branch
- Pull requests to the master branch
- Changes in the app_python directory

## Key Features

### 1. Path-Based Triggering
```yaml
on:
  push:
    branches: [ "master" ]
    paths:
      - 'app_python/**'
  pull_request:
    branches: [ "master" ]
    paths:
      - 'app_python/**'
```
This ensures the workflow only runs when relevant files are modified.

### 2. Dependency Management
```yaml
- name: Cache pip packages
  uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('app_python/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```
- Implements caching for pip packages
- Uses hash of requirements.txt for cache key
- Includes fallback restore-keys

### 3. Security Scanning with Snyk
```yaml
- name: Run Snyk to check for vulnerabilities
  uses: snyk/actions/python@master
  env:
    SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
  with:
    args: --skip-unresolved app_python/
  continue-on-error: true
```
- Scans Python dependencies for known vulnerabilities
- Uses Snyk's official GitHub Action
- Configured to continue on error for development flexibility

### 4. Code Quality Checks
```yaml
- name: Lint with flake8
  run: |
    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```
- Enforces code style with flake8
- Checks for syntax errors and undefined names
- Monitors code complexity

### 5. Testing
```yaml
- name: Run tests
  run: |
    pytest test_app.py -v
```
- Executes unit tests with verbose output
- Ensures all tests pass before proceeding

### 6. Docker Integration
```yaml
- name: Login to DockerHub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKER_USERNAME }}
    password: ${{ secrets.DOCKER_PASSWORD }}

- name: Build and push Docker image
  uses: docker/build-push-action@v5
  with:
    context: ./app_python
    push: true
    tags: marketer7/flask-time:latest
```
- Automates Docker image building and publishing
- Uses secure credential management
- Tags images consistently

## Best Practices Implemented

### 1. Security
- Secret management using GitHub Secrets
- Snyk vulnerability scanning
- Minimal permissions model
- Secure Docker practices

### 2. Performance
- Dependency caching
- Path-based workflow triggering
- Efficient job organization

### 3. Reliability
- Consistent environment using ubuntu-latest
- Specific Python version (3.9)
- Clear error reporting

### 4. Maintainability
- Well-documented workflow
- Modular step organization
- Clear step naming

## Adding Status Badge
![CI Status](https://github.com/MarketerKA/S25-core-course-labs/workflows/Python%20Flask%20App%20CI/badge.svg)