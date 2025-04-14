# Continuous Integration (CI) Best Practices

This document outlines the best practices implemented in our GitHub Actions CI workflow to ensure efficient, reliable, and maintainable automation.

## 1. **Trigger Workflows Only When Necessary**
- The workflow is triggered **on pull requests** to the `lab3` branch.
- It runs **only when files inside `app_go/` are modified**.
- This prevents unnecessary workflow executions and saves CI resources.

## 2. **Run Security Checks Before Building Docker Image**
- The `security` job runs **before the Docker image is built** to ensure that vulnerabilities are caught early.
- It uses **Snyk** to check for security vulnerabilities in the Go code.
- This job checks for any security issues in the code before proceeding to the Docker build.

## 3. **Log in to Docker Hub and Build Docker Image**
- After successful security checks, the workflow proceeds to **log in to Docker Hub** using credentials stored in GitHub Secrets (`DOCKER_USERNAME` and `DOCKER_PASSWORD`).
- The workflow **builds the Docker image** from the `app_go` directory using the `docker build` command.
- This Docker image is tagged as `latest` for further use in development and production environments.

## 4. **Push Docker Image to Docker Hub**
- After building the Docker image, it is **pushed to Docker Hub** to make it available for deployment.

## 5. **Ensure Code Checkout Before Any Steps**
- The `checkout` step is **required before accessing the repository**.
- Added:
  ```yaml
  - name: Checkout Code
    uses: actions/checkout@v3
  ```
- Without this, subsequent steps would fail due to missing code files.

## 6. **Integrate Security Checks with Snyk**
- The workflow includes a security scan using Snyk to detect vulnerabilities in dependencies.
- Implemented Snyk with:
  ```
    - name: Run Snyk to check for vulnerabilities
    uses: snyk/actions/golang@master
    with:
        command: code test
    env:
        SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
  ```
- This ensures that security vulnerabilities are identified early in the development cycle.

## 7. **Define Job Dependencies for Better Workflow Execution**
- The ```build-and-push-docker``` job ***depends on successful completion*** of:
  - ***security***
- Implemented with:
  ```
  needs: 
  - security
  ```
- This guarantees that the Docker image is built only after security checks succeed.


By following these best practices, the CI workflow is now faster, more efficient, and easier to maintain.