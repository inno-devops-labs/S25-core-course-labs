# CI/CD Best Practices

## 1. Workflow optimization
- Uses GitHub Actions cache to speed up builds.
- The build stops on errors to save resources.
- The Docker build process minimizes redundant builds.

## 2. Security
- Detects vulnerabilities in dependencies(Snyk).
- Uses GitHub Secrets for storing sensitive credentials.
- Ensures code quality before deployment.

## 3. CI/CD Workflow Breakdown
- `flake8` checks for coding style violations.
- Runs Django unit tests to verify application behavior.
- The app is containerized and uploaded to Docker Hub.
- Snyk scans dependencies for vulnerabilities.
