# CI Best Practices 

[This](/.github/workflows/python.yaml) workflow incorporates the following practices:

- **Granular Workflow Triggers**
  - **Branch and Path Filtering:** Only triggers on pushes or pull requests affecting critical parts of the repository (workflow files and application code).
  - **Controlled Execution:** Restricts pull request checks to the `main` branch, reducing unnecessary runs on feature branches.

- **Modular and Sequential Job Structure**
  - **Separation of Concerns:** Divides the CI process into distinct jobs (linting, testing, security scanning, Docker build), making it easier to identify and troubleshoot issues.
  - **Job Dependencies:** Uses the `needs` keyword to enforce a sequential flow (lint → test → security → build), ensuring that later stages run only if earlier ones succeed.

- **Consistent and Reusable Setup**
  - **Versioned Actions:** Utilizes official GitHub actions (e.g., `actions/checkout@v4`, `actions/setup-python@v4`) with explicit versioning for reproducibility.
  - **Python Environment Configuration:** Sets up Python with a specific version (3.12) and enables dependency caching (`cache: pip`), speeding up repeated runs.

- **Code Quality and Security Checks**
  - **Linting:** Implements a linter (`ruff`) to enforce code quality and style before tests run.
  - **Automated Testing:** Runs tests using `pytest` to verify functionality and prevent regressions.
  - **Security Scanning:** Integrates Snyk to automatically check for vulnerabilities in Python dependencies, using secure environment secrets to handle tokens.

- **Secure and Automated Docker Build**
  - **Credential Management:** Logs into DockerHub using secrets (`DOCKERHUB_USERNAME` and `DOCKERHUB_PASSWORD`) to safely manage credentials.
  - **Modern Container Build Practices:** Uses Docker’s Buildx for building and pushing images, ensuring compatibility with multi-platform builds.
  - **Continuous Deployment Readiness:** Automatically builds and pushes a Docker image after all quality and security checks pass.
