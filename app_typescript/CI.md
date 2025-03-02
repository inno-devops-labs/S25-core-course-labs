# CI Best Practices

## 1. **Version Control and Triggers**

- The workflow runs on `push` and `pull_request` events.
- It runs only when changes in `app_typescript` folder occurs.

## 2. **Code Quality and Linting**

- Uses **ESLint** to enforce code style and detect potential errors.
- Runs **Prettier** in check mode to ensure consistent code formatting.
- Ensures no direct formatting changes are made in CI, preventing unintended commits.

## 3. **Automated Testing**

- Uses **vitest** to run unit tests.
- Helps catch regressions early by running tests in each PR.

## 4. **Security Scanning**

- Integrates **Snyk** to check for vulnerabilities in dependencies.
- Ensures no unresolved security issues affect production builds.
- Uses GitHub secrets to securely pass authentication tokens.

## 5. **Docker Image Management**

- Uses **Docker Buildx**.
- Builds and pushes two types of images:
    - A **basic image** using `Dockerfile`.
    - A **distroless image** using `distroless.Dockerfile`.
- Implements **caching** to speed up builds and reduce redundant work.
- Authenticates to **Docker Hub** securely using GitHub secrets.

## 6. **Job Dependencies and Parallel Execution**

- Defines explicit dependencies (`needs`) to optimize execution order.
- Ensures `snyk` runs only after linting and testing are successful.
- Ensures `docker-push` runs only if linting, testing, and security checks pass.

## 7. **Optimized Caching and Performance**

- Uses **pip caching** to speed up dependency installation.
- Docker images use `cache-from` and `cache-to` to minimize build time.