# CI Best Practices

This project implements a set of best practices for CI/CD, including:

1. **Dependency caching**
   - 'actions/cache' is used to save the pip dependency cache, which speeds up package installation during repeated builds.
   
2. **Checking the code**
   - **Linting:** Flake8 is used to check the code style.
   - **Testing:** Tests are run using pytest.

3. **Vulnerability check**
   - Snyk is integrated to automatically check dependencies for known vulnerabilities. The secret `SNYK_TOKEN` is used for Snyk operation.

4. **Building and publishing a Docker image**
   - The Docker image is assembled and published using the GitHub Action `docker/build-push-action`.
   - Caching of Docker layers is enabled using the `cache-from` and `cache-to` parameters, which speeds up the build.

5. **Secret Management**
   - All sensitive data (for example, Docker Hub and Snyk tokens) is transferred via GitHub Secrets.

6. **Build status**
   - The build status is visible directly in the repository using the status badge added to `README.md `.

These practices help maintain code quality, speed up build, and identify security issues in a timely manner.
