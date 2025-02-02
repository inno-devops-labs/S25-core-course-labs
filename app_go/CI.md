# CI Best Practices

## Optimizations Implemented

- **Dependency Caching**: Uses GitHub Actions Cache to avoid redundant downloads.
- **Selective Workflow Triggers**: Runs only when `app_go/` changes.
- **Linting & Security Checks**: Includes `golangci-lint` and `Snyk`.
- **Docker CI/CD**: Automates building and pushing Docker images.

## Security Checks

- Integrated **Snyk** to scan dependencies for vulnerabilities.
