# CI Best Practices

This document outlines the best practices implemented in the GitHub Actions CI workflow for a Go web application.

## 1. Triggers
The code uses triggers for `push` and `pull_request` events to the `master` branch, and also ensures the workflow only runs when changes occur in the `app_golang` directory.

## 2. Dependency Installation with Caching
Dependencies are automatically installed from `go.mod`, and caching is used to speed up the CI process.

## 3. Linting
The code utilizes `golangci-lint` to verify its adherence to Go language standards and identify potential errors.

```yaml
    - name: Linter
      run: |
        go install github.com/golangci/golangci-lint/cmd/golangci-lint@v1.56.2
        golangci-lint run ./...
```

## 4. Unit Testing
Unit tests are used in the CI to verify the correctness of the web application's functionality.
```yaml
    - name: UnitTests
      run: go test ./... 
```

## 5. Docker Image Build
The application is Dockerized for deployment in various environments.
```yaml
    - name: docker build and push
      uses: docker/build-push-action@v4
      with:
        context: ./app_golang
        push: true
        tags: ${{ secrets.DOCKER_USERNAME }}/golang-web-app:latest
        cache-from: type=gha,scope=primary
        cache-to: type=gha,scope=primary
```

## 6. Security Checks
Snyk is used to scan the Go project for vulnerabilities.
```yaml
    - name: Run Snyk to check for vulnerabilities
      uses: snyk/actions/golang@master
      env:
        SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      with:
        args: test ./app_golang
```

## 7. Using Secrets
Secrets are used in the project for Docker login and the Snyk token to enhance deployment security.

## 8. Job Dependencies
Jobs are executed in the correct sequence by specifying dependencies.
```yaml
    needs: build
```