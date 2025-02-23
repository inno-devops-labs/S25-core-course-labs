# CI Workflow

## Jobs
1. Build and Test
- **Checkout Repository** : Fetches the code.
- **Set Up Python** : Configures Python 3.13.
- **Install Dependencies** : Installs packages from `requirements.txt`.
- **Lint with Flake8** : Enforces code quality (errors reported but do not fail the build).
- **Run Tests** : Executes unit tests using pytest.
- **Snyk Security Scan** : Scans for vulnerabilities in dependencies.
2. Docker Build and Push
- **Log in to Docker Hub** : Authenticates with Docker Hub.
- **Build and Push** : Builds and pushes the Docker image with caching:
  - **Cache-from** : Reuses layers from the previous build.
  - **Cache-to** : Saves new layers for future builds.

## Best Practices
1. **Path Filtering** : Runs only for changes in `app_python/**`.
2. **Linting** : Uses flake8 for code quality (non-blocking).
3. **Testing** : Validates functionality with `pytest`.
4. **Security** : Scans dependencies with Snyk.
5. **Docker Caching** : Speeds up builds with inline caching.