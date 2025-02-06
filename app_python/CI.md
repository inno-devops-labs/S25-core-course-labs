# CI

This document describes the recommendations used to optimize the CI workflow in this project.

## 1. Dependency Caching
- By caching dependencies, we avoid reinstalling them every time we run, unless "requirements.txt "it won't change.

## 2. Linting
- The quality of the code is important for ease of maintenance and reading. Layout tools help identify common errors early in the development process.

## 3. Testing
- Automated testing using pytest ensures that new changes do not disrupt existing functionality.

## 4. Docker Integration
- Containerization simplifies deployment and ensures consistency across environments. We build and push a Docker image to Docker Hub as part of the CI workflow.

## 5. Vulnerability Scanning
- We integrate Snyk into the CI workflow to scan for vulnerabilities in the project's dependencies.