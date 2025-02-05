# CI Workflow Best Practices

## Overview

Our CI pipeline is defined in [`.github/workflows/ci-go.yml`](./../.github/workflows/ci-go.yml) and is split into two jobs:

1. **build-and-test:**
    - **Checkout Code:** Retrieves the latest code.
    - **Set up Go:** Configures the desired Go version.
    - **Caching Dependencies:** Uses `actions/cache` to cache dependencies to reduce installation time.
    - **Dependency Installation:** Installs required packages from `go.mod`.
    - **Linting:** Runs `go vet` to enforce code style.
    - **Testing:** Executes unit tests with `go test`.
    - **Snyk Vulnerability Scan:** Scans for known vulnerabilities using Snyk.

2. **docker:**
    - **DockerHub Login:** Authenticates using stored Docker credentials.
    - **Build and Push:** Builds the Docker image with caching enabled (using GitHub Actions caching for Docker layers) and pushes the image to DockerHub.

## Best Practices Applied

- **Branch-Agnostic Triggers:**  
  The workflow runs on all branches, ensuring every push and pull request is tested.

- **Efficient Caching:**  
  Both pip and Docker caches are used to optimize build times and reduce redundant work.

- **Security:**
    - Sensitive data (Docker credentials and Snyk token) are managed through GitHub Secrets.
    - Vulnerability scans are integrated to catch security issues early.

- **Modular Job Design:**  
  Separating testing from Docker operations ensures that container builds only occur if the tests pass, keeping the workflow efficient and reliable.
