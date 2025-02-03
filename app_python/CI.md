# Python Web App - CI Best Practices

-----

## Best Practices

### Workflow and Efficiency

1. **Build Cache**: Dependency caching using `actions/cache@v3` to reduce installation time for Python packages.
2. **Conditional Execution**: Docker image building and pushing are executed only on pushes to avoid unnecessary builds.
3. **Workflow Status Badge**: Added a workflow status badge to the `README.md` file for quick visibility of CI pipelint status.

### Security

1. **Snyk Integration**: Snyk vulnerability checks to identify and address security issues in dependencies. The scan is configured to report vulnerabilities with a severity threshold `high`.
2. **Secrets Management**: All credentials (Docker username and passwork, Docker Hub username, Snyk token) are stored securely using GitHub Repository Secrets.

-----
