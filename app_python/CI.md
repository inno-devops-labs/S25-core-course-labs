# Continuous Integration (CI) Best Practices

This document outlines the best practices implemented in our CI workflows.

## Workflow Enhancements

1. **Caching**:
   - Dependencies and Docker layers are cached to improve workflow efficiency.
   - Example: `actions/cache` is used to cache Python virtual environments and Docker build layers.

2. **Snyk Vulnerability Scanning**:
   - Snyk is integrated into the `test.yml` workflow to identify and address vulnerabilities in dependencies.


3. **Workflow Status Badges**:
   - Badges are added to the `README.md` for visibility into the status of tests, linting, and Docker builds. however the bage for tests is currently red due to my mistake. I pushed not working ci in main branch and get red status. Then all work were completed in lab3 branch

4. **Trigger Conditions**:
   - Workflows are triggered on differently for different test. 

5. **Docker Build Optimization**:
   - Docker Buildx is used to enable advanced build features, and layers are cached to speed up builds.

## How to Use

- **Run Tests**: The `test.yml` workflow runs unit tests and Snyk vulnerability scans.
- **Lint Code**: The `linter.yml` workflow ensures code style consistency using `flake8`.
- **Build and Push Docker Image**: The `docker.yml` workflow builds and pushes a Docker image to Docker Hub.
