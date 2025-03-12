# app_python

This web application displays current time in Moscow

## CI Workflow Best Practices

- **Parallel Steps**: Linting and tests are run in parallel using a matrix strategy, improving the workflow's speed
- **Docker Build Cache**: Docker's cache mechanism is utilized to speed up builds by not rebuilding unchanged layers
- **Docker Hub Integration**: The workflow automatically logs in to Docker Hub, builds the Docker image, and pushes it to the repository
- **Snyk Vulnerability Scanning**: Integrated Snyk into the CI workflow to ensure that any security vulnerabilities are identified
