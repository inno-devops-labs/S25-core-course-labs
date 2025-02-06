# Continuous Integration (CI) Documentation

[![Python application](https://github.com/favelanky/S25-core-course-labs/actions/workflows/python-app.yml/badge.svg)](https://github.com/favelanky/S25-core-course-labs/actions/workflows/python-app.yml)

## Overview

This repository implements a robust CI/CD pipeline using GitHub Actions. The workflow automates testing, linting, security scanning, and Docker image building for our Python application.

## Implemented Best Practices

### 1. Caching Strategy
- **Pip Dependencies**: Using GitHub Actions' built-in pip caching
- **Docker Layers**: Implementing BuildX cache for faster Docker builds
- Cache keys are based on OS and commit SHA for proper invalidation

### 2. Security Measures
- Comprehensive vulnerability scanning with Snyk for both Python dependencies and Docker images
- Limited permissions using the principle of least privilege
- Security scanning with Bandit for Python code analysis
- Secure handling of Docker Hub credentials using secrets
- Full history fetch for better security analysis

### 3. Testing and Quality
- Comprehensive pytest suite with coverage reporting
- Flake8 linting with strict rules
- Complexity checks and line length enforcement

### 4. Performance Optimizations
- Job timeout limits to prevent hanging builds
- Efficient Docker layer caching
- Parallel job execution where possible
- Conditional Docker image pushing (only on main branch)

### 5. Docker Best Practices
- Using BuildX for efficient, multi-platform builds
- Layer caching for faster builds
- Proper tagging strategy
- Secure credential handling
- Container vulnerability scanning with Snyk

## Workflow Details

The workflow is triggered on:
- Push to any branch
- Pull request to any branch

### Job Steps:
1. Code checkout
2. Python setup with caching
3. Dependencies installation
4. Snyk Python dependency scanning
5. Security scanning with Bandit
6. Linting
7. Testing with coverage
8. Docker image building and pushing
9. Snyk Docker image scanning

## Security Scanning

### Snyk Integration
The workflow includes two Snyk scanning steps:
1. **Python Dependencies Scan**: Checks for vulnerabilities in Python packages
2. **Docker Image Scan**: Analyzes the built Docker image for security issues

To set up Snyk:
1. Create a Snyk account at https://snyk.io
2. Generate a Snyk API token
3. Add the token as a GitHub secret named `SNYK_TOKEN`

## Maintenance

To maintain the CI pipeline:
1. Regularly update GitHub Action versions
2. Monitor workflow execution times
3. Review and update dependency versions
4. Check security scanning reports from both Bandit and Snyk
5. Maintain Docker Hub credentials
6. Monitor and address Snyk security alerts

## Status Badge

The status badge at the top of this document shows the current state of the CI pipeline. Green indicates passing builds, red indicates failures. 