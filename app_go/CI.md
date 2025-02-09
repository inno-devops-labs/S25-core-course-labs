# CI Best Practices

## 1. Workflow Optimization

- Used caching for dependencies (`actions/cache@v3`).
- Minimized redundant package installations.
- Used separate jobs for application build & test and containerization

## 2. Security Enhancements

- Integrated Snyk to scan for security vulnerabilities.

## 3. Performance Improvements

- Separated build and test steps for better pipeline observability.
- Used `needs:` to avoid unnecessary runs.
