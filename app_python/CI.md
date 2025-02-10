# CI Pipeline Best Practices

- **Job Separation**: Divided pipeline into linting, testing, security scanning, and Docker build jobs for clarity and maintainability.

- **`working-directory` Usage**: Ensures tasks run in the correct directory (`app_python`).

- **Efficient Dependency Management**: Installs dependencies from `requirements.txt` and upgrades `pip`.
  
- **Parallel Job Execution**: Runs linting, testing, and security scanning in parallel to speed up the pipeline.

- **Security with Snyk**: Uses **Snyk** for vulnerability scanning, with API token stored in GitHub Secrets.

- **Docker Integration**: Secures Docker Hub login and only builds and pushes Docker image after passing jobs.
