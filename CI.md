# Continuous Integration (CI) Implementation

## Overview

This document outlines the CI workflow implementation and best practices applied to our Python and Node.js applications.

## CI Workflow Components

### 1. Dependencies Installation

- Uses pip/npm caching to speed up dependency installation
- Installs all required packages from requirements.txt/package.json
- Upgrades pip to latest version for better compatibility

### 2. Code Quality Checks

- Implements flake8 for Python linting
- Uses ESLint for Node.js linting
- Enforces PEP 8 style guide for Python
- Checks for syntax errors and undefined names
- Sets maximum complexity threshold
- Enforces line length limits

### 3. Testing

- Runs unit tests using pytest for Python
- Uses Jest for Node.js testing
- Provides verbose output for better debugging
- Tests are run in isolated environment

### 4. Docker Integration

#### Standard Images

- Authenticates with Docker Hub
- Builds Docker images from Dockerfile
- Uses multi-stage builds for smaller images
- Implements build caching for faster builds

#### Distroless Images

- Builds security-optimized distroless images
- Uses separate Dockerfile for distroless builds
- Reduces attack surface by removing shell and unnecessary tools
- Implements separate build caching for distroless images
- Tags images with :distroless suffix

### 5. Security Scanning

- Integrates Snyk for vulnerability scanning
- Checks dependencies for known vulnerabilities
- Sets severity threshold for failing builds
- Provides detailed security reports

## Best Practices Implemented

1. **Path Filtering**

   - Workflows run only when relevant files change
   - Separate workflows for Python and Node.js applications
   - Prevents unnecessary builds

2. **Caching Strategy**

   - Implements pip/npm cache
   - Uses Docker layer caching
   - Separate build caches for standard and distroless images
   - Reduces build times and resource usage

3. **Security**

   - Secrets stored in GitHub Secrets
   - Regular vulnerability scanning
   - Automated security updates
   - Distroless images for enhanced security

4. **Workflow Optimization**
   - Parallel job execution where possible
   - Efficient step ordering
   - Minimal build times
   - Build cache persistence

## Status Badges

### Python Application

[![Python Application CI](https://github.com/AlexStrNik/S25-core-course-labs/actions/workflows/python-app.yml/badge.svg)](https://github.com/AlexStrNik/S25-core-course-labs/actions/workflows/python-app.yml)

### Node.js Application

[![Node.js Application CI](https://github.com/AlexStrNik/S25-core-course-labs/actions/workflows/nodejs-app.yml/badge.svg)](https://github.com/AlexStrNik/S25-core-course-labs/actions/workflows/nodejs-app.yml)
