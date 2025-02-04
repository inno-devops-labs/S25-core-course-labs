# Go CI Best Practices

## Specific Workflow Triggers

The pipeline runs only on pull requests to `master` branch.

Also, path filtering is done to ensure that the workflow runs only on pull requests changing Go related files: `.github/workflows/app_go.yml` and `app_go/**`.

## Dependencies Management

Uses a `go.mod` file to ensure consistent environment.

Also, caches the dependencies' files to speed up package downloading.

## Code Quality Checks

Runs a linter and a formatter through a `Makefile` to catch potential problems before merging the branch.

## Automated Testing

Runs tests using a `Makefile` to ensure that code changes do not cause problems with previous features.

## Security Scanning

Uses Snyk for security vulnerability scanning to detect problems in dependencies.

## Code Coverage Reporting

Uploads test coverage report as an artifact for further analysis.

## Docker Image Management

Builds and pushes distroless image to improve security and reduce attack surface.

Uses GitHub Actions caching to speed up building.

## Secret Management

Uses GitHub Secrets for storing tokens to improve security.

## Modular Workflow

Separating steps for each major task (setup, linting, testing, security, Docker) to improve maintainability.
