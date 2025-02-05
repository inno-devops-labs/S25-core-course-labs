# Continuous Integration (CI) Best Practices

This document explains the key practices we follow in our CI workflow for the Go Web Application. Our CI pipeline is designed to be efficient, secure, and easy to maintain.

## Overview

Our CI workflow is split into three main jobs:

- **Security:** Checks for known vulnerabilities using Snyk.
- **Build & Test:** Installs dependencies, runs linters, and executes unit tests.
- **Docker:** Builds and pushes both standard and distroless Docker images.

This separation allows us to handle each concern independently, ensuring that security checks, code quality, and deployment processes run in isolation.

## Best Practices

### 1. Targeted Triggers

- **Selective Execution:** The workflow is set to run only when changes occur in the `app_go` folder on the `lab3` and `master` branches. This avoids unnecessary builds when unrelated parts of the repository are modified.

### 2. Separation of Concerns

- **Distinct Jobs:** The CI workflow is divided into Security, Build & Test, and Docker jobs. Each job focuses on a specific task, such as vulnerability scanning, code linting, unit testing, and Docker image building. This separation helps to keep the pipeline clean and makes it easier to debug and maintain.

### 3. Caching for Efficiency

- **Go Module Caching:** The `go mod tidy` step installs dependencies and is optimized by caching the `go.sum` file. This speeds up the process of fetching dependencies for each build.
- **Docker Layer Caching:** Docker builds are optimized by caching layers using `cache-from` and `cache-to`. This approach minimizes redundant rebuilding of Docker layers, significantly speeding up the image-building process.

### 4. Security Measures

- **Vulnerability Scanning:** Snyk is integrated into the pipeline to continuously scan for known vulnerabilities in the Go code. This proactive security measure helps us address vulnerabilities early before they can affect production environments.

### 5. Code Quality Enforcement

- **Linting and Testing:** We use `go vet` and `go fmt` to ensure code adheres to Go’s best practices and formatting standards. Unit tests are executed using `go test` to verify that the application behaves as expected. This ensures that any code changes are thoroughly checked before being merged or deployed.

### 6. Efficient Resource Usage

- **Optimized Workflow Runs:** The CI workflow is triggered only when relevant changes occur, saving time and resources. By caching dependencies and Docker layers, we reduce build times and resource usage, ensuring faster feedback and smoother development cycles.

### 7. Documentation and Transparency

- **Visibility:** A status badge in the README provides immediate feedback on the build status. This helps team members stay informed about the current build state.
- **Clear Documentation:** The CI process is well documented, with details available in this file and the README. This makes it easy for new contributors to understand the pipeline setup and follow best practices for continuous integration.
