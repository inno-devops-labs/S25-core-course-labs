# Continuous Integration (CI) Best Practices

[![Python application CI](https://github.com/TheAnushervon/S25-core-course-labs/actions/workflows/app_python.yml/badge.svg?branch=lab3)](https://github.com/TheAnushervon/S25-core-course-labs/actions/workflows/app_python.yml) <br> 

### Targeted Workflow Triggers

The workflow is triggered on both **push** and **pull_request** events when changes occur in:
- `app_python/**`
- `.github/workflows/app_python.yml`

This ensures that CI checks run for direct pushes as well as for pull requests.

### Default Working Directory

Setting a default working directory of `./app_python` avoids the need to manually change directories in each command.

### Dependency Caching

Utilize `actions/cache` to store Python dependencies, which reduces build time by avoiding repeated installations.

### Code Quality & Testing

Early linting with **flake8** and running Django tests help catch issues early in the pipeline.

### Security Scanning

Integrate **Snyk** vulnerability checks to identify security issues. (Configured with `continue-on-error` so that vulnerabilities are reported without failing the build.)

### Optimized Docker Builds

Use Docker **Buildx** with caching to enable efficient image builds and push them to Docker Hub.
