# Continuous Integration Best Practices

## Workflow Enhancements
- **Workflow Status Badge**: A workflow status badge used in `README.md`.
- **Dependency Caching**: Caching of pip dependencies to have faster build process.
- **Linting**: Added `flake8` to check code style before running tests.
- **Automated Testing**: Added `pytest` with reports.
- **Docker Caching**: Docker build caching to have faster image build process.
- **DockerHub Deployment**: Auto push of image to DockerHub.

## Security Enhancements
- **Snyk Vulnerability Scan**: Added a vulnerability check with `Snyk`.

## CI/CD Automation
- The workflow is automatically triggered on every `push` and `pull request`.
- If there are issues, the build will be blocked.
