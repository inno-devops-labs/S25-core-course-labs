# Continuous Integration (CI) Best Practices

This document explains the key practices we follow in our CI workflow. Our CI pipeline is designed to be efficient, secure, and easy to maintain.

## Overview

Our CI workflow is split into three main jobs:

- **Security:** Checks for known vulnerabilities using Snyk.
- **Build & Test:** Installs dependencies, runs linters (Flake8 and Pylint), and executes unit tests.
- **Docker:** Builds and pushes both standard and distroless Docker images.

This separation allows us to handle each concern independently, ensuring that security checks, code quality, and deployment processes run in isolation.

## Best Practices

### 1. Targeted Triggers

- **Selective Execution:** The workflow is set to run only when changes occur in the `app_python` folder on the `lab3` and `master` branches. This avoids unnecessary builds when unrelated parts of the repository are modified.
  
### 2. Separation of Concerns

- **Distinct Jobs:** Splitting the workflow into Security, Build & Test, and Docker jobs makes it easier to pinpoint issues. Each job handles a specific aspect of the CI process, reducing complexity and improving maintainability.

### 3. Caching for Efficiency

- **Pip Dependency Caching:** We cache pip dependencies to minimize the time spent on installing packages for every build.
- **Docker Layer Caching:** Docker builds are optimized by caching build layers using `cache-from` and `cache-to`. This speeds up the image building process and makes repeated builds faster.

### 4. Security Measures

- **Vulnerability Scanning:** The integration of Snyk ensures that our code is continuously checked for known security vulnerabilities. This proactive approach helps us address issues before they affect production.

### 5. Code Quality Enforcement

- **Linting and Testing:** Before code is merged or deployed, it is checked using Flake8 and Pylint to enforce coding standards and catch common errors. Running unit tests with pytest ensures that the application behaves as expected.
  
### 6. Efficient Resource Usage

- **Optimized Workflow Runs:** By triggering the workflow only on relevant changes and using caching, we conserve computational resources and reduce build times. This leads to faster feedback and a smoother development process.

### 7. Documentation and Transparency

- **Visibility:** A status badge in the README provides immediate feedback on the build status.
- **Clear Documentation:** This file and the README offer a clear explanation of our CI setup, making it easier for team members to understand and follow our CI practices.
