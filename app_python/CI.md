# GitHub Actions CI best practices

- Code quality checking
    - Run Ruff linter & formatter to analyze code quality before merging
- Testing
    - Run tests to ensure that app logic works correctly
- Scanning for vulnerabilities
    - Use Synk to check for known vulnerabilities
- Build & Push Docker images
    - Build and Push to DockerHub image with app
- Utilize build cache
    - Optimize building process with build cache utilizing to enhance workflow efficiency
- Manage secrets
    - Store sensitive information in GihHub Secrets to improve security
- Workflow triggers
    - Run the pipeline only on push and pull-request to the master branch
    - Do not push the docker image on DockerHub on pull-request to the master branch (push only)
    - Separate jobs (build & test, docker) and steps to improve maintainability 