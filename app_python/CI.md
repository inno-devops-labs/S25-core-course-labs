# CI Workflow

## Best practices

### Dependency Caching

Cached pip dependencies using cache-dependency-path to speed up installation

### Using linter

Runs flake8 before tests to catch issues early

### Security Checks

Uses Snyk for vulnerability scanning and stores credentials securely in GitHub Secrets.

### Optimized Docker Workflow

Logs into Docker Hub automatically and pushes images only if tests and security checks pass

### Automated Triggers

Runs automatically on PRs affecting app_python/.

