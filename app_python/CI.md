# CI Workflow Documentation - Flask Moscow Time App

This project includes a GitHub Actions CI workflow that ensures the code is always secure, clean, and deployable.

---

## 🛠 CI Workflow Structure

### 1. `build-test` Job
- Checks out code from the repository.
- Sets up Python 3.12 with pip dependency caching.
- Installs dependencies (`Flask`, `pytz`, etc.).
- Runs:
  - `flake8` for PEP8 compliance.
  - `pylint` for in-depth static analysis.
  - `pytest` for test execution

### 2. `docker` Job
- Depends on `build-test` to only run if lint/test passes.
- Uses Buildx for advanced Docker builds.
- Logs in to Docker Hub using secure GitHub secrets.
- Builds and pushes a rootless, best-practice Docker image of the app.

### 3. `security` Job
- Uses Snyk GitHub Action to scan Python dependencies and source code.
- Detects known vulnerabilities in the Python ecosystem.
- Requires a valid `SNYK_TOKEN` in GitHub secrets.

---

## Best Practices Implemented

### CI/CD Structure
- Jobs are clearly separated: build/test, docker image build, and security scanning.
- `needs:` is used to avoid unnecessary Docker builds on broken code.

### Dependency Caching
- `cache: 'pip'` used with `actions/setup-python` to speed up repeated installs.

### Code Quality Checks
- `flake8` checks for style violations.
- `pylint` ensures deeper static analysis and scores the code.
- Ensures team code remains clean and consistent.

### Docker Best Practices in CI
- Docker builds are delegated to Buildx for better support.
- Images are only pushed after successful builds and tests.
- Secrets are managed securely (`DOCKER_USERNAME`, `DOCKER_PASSWORD`).

### Security Integration (Snyk)
- Uses `snyk/actions/python-3.9@master` GitHub Action.
- Requires a valid `SNYK_TOKEN` stored in GitHub secrets.
- Helps detect and manage vulnerabilities before deployment.

---

## Visibility
Added a status badge in `README.md`:


---
