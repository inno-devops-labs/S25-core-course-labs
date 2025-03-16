# Best Practices in Go Application CI

- __Trigger Conditions__: Runs on pull requests to `master` and specific file/folders changes.
- __Consistent Environment__: Uses `ubuntu-22.04` and sets a working directory.
- __Go Version__: Specifies Go version (`1.23.5`).
- __Code Quality__: Lints code with `go fmt` for consistency.
- __Testing__: Runs tests using `go test`.
- __Security__: Scans for vulnerabilities with Snyk.
- __Job Order__: Runs testing first, then builds the Docker image if tests pass.
- __Docker__: Builds and pushes Docker images with proper setup and login actions.
- __Caching__: Speeds up builds using Docker and pip caching.
- __Secrets__: Keeps sensitive data safe with GitHub Secrets.
