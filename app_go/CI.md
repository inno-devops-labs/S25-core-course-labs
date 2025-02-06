# CI Workflow for Go Application

## Jobs

1. Build and Test
- **Set Up Go**: Configures Go 1.23.
- **Cache Dependencies**: Caches Go modules to speed up builds.
- **Install Dependencies**: Downloads dependencies using `go mod download`.
- **Lint Code**: Uses `golangci-lint` for linting (errors reported but do not fail the build).
- **Run Tests**: Executes unit tests using `go test`.
- **Snyk Security Scan** : Scans for vulnerabilities in dependencies.

2. Docker Build and Push
- **Log in to Docker Hub**: Authenticates with Docker Hub.
- **Build and Push**: Builds and pushes the Docker image with caching:
  - **Cache-from**: Reuses layers from the previous build.
  - **Cache-to**: Saves new layers for future builds.


## Best Practices

- **Path Filtering**: Runs only for changes in `app_go/**`.
- **Dependency Caching**: Speeds up builds by caching Go modules.
- **Linting**: Enforces code quality with `golangci-lint`.
- **Testing**: Validates functionality with `go test`.
- **Docker Caching**: Optimizes Docker builds with inline caching.
