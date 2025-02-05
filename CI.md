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
- Limited permissions using the principle of least privilege
- Security scanning with Bandit
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

## Workflow Details

The workflow is triggered on:
- Push to any branch
- Pull request to any branch

### Job Steps:
1. Code checkout
2. Python setup with caching
3. Dependencies installation
4. Security scanning
5. Linting
6. Testing with coverage
7. Docker image building and pushing

## Maintenance

To maintain the CI pipeline:
1. Regularly update GitHub Action versions
2. Monitor workflow execution times
3. Review and update dependency versions
4. Check security scanning reports
5. Maintain Docker Hub credentials

## Status Badge

The status badge at the top of this document shows the current state of the CI pipeline. Green indicates passing builds, red indicates failures. 