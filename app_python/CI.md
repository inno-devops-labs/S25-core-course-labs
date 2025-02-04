## Best Practices Applied

1. **Selective triggering**: The pipeline triggers on pushes to specific directories 
(`.github/workflows/**`, `app_python/**`), ensuring that only relevant changes trigger the CI process.
2. **Caching dependencies**: Cache Python dependencies to speed up builds by storing dependencies between workflow runs.
3. **Environment setup**: Set up the Python environment with the specified version.
4. **Dependency installation**: Install project dependencies.
5. **Code linting**: Run flake8 for code style and syntax checks.
6. **Unit testing**: Run unit tests to ensure code correctness and catch regressions.
7. **Vulnerability scanning**: Use Snyk to scan and address security vulnerabilities in dependencies.
8. **Docker image build and push**: Build and push the Docker image to Docker Hub for easy deployment.
9. **Secret Management**: Use GitHub secrets for securely managing sensitive credentials in the pipeline.


