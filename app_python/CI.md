# Continuous Integration (CI) Best Practices

This document outlines the best practices implemented in our GitHub Actions CI workflow to ensure efficient, reliable, and maintainable automation.

## 1. **Trigger Workflows Only When Necessary**
- The workflow is triggered only on changes to the `lab3` branch.
- It runs **only when files inside `app_python/` are modified**.
- This prevents unnecessary workflow executions and saves CI resources.

## 2. **Use Fail-Fast Strategy**
- The `fail-fast: true` setting ensures that if one job in a matrix fails, all remaining jobs stop immediately.
- This saves execution time and provides quicker feedback to developers.

## 3. **Use Dependency Caching for Faster Builds**
- **Pip dependencies are cached** to avoid redundant installations across workflow runs.
- Implemented caching with:
  ```yaml
  - name: Cache Python dependencies
    uses: actions/cache@v3
    with:
      path: ~/.cache/pip
      key: ${{ runner.os }}-pip-3.11-${{ hashFiles('**/requirements.txt') }}
      restore-keys: |
        ${{ runner.os }}-pip-3.11-
  ```
- This speeds up dependency installation significantly.

## 4. **Ensure Code Checkout Before Any Steps**
- The `checkout` step is **required before accessing the repository**.
- Added:
  ```yaml
  - name: Checkout Code
    uses: actions/checkout@v3
  ```
  Without this, subsequent steps would fail due to missing code files.

## 5. **Integrate Security Checks with Snyk**
- The workflow includes a **security scan** using [Snyk](https://snyk.io/) to detect vulnerabilities in dependencies.
- Implemented Snyk with:
  ```yaml
  - name: Run Snyk to check for vulnerabilities
    uses: snyk/actions/python-3.10@master
    with:
      command: code test
    env:
      SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
  ```
- This ensures that security vulnerabilities are identified early in the development cycle.

## 6. **Define Job Dependencies for Better Workflow Execution**
- The `build-and-push-docker` job **depends on successful completion** of:
  - `build-and-run-tests`
  - `security`
- Implemented with:
  ```yaml
  needs: 
    - build-and-run-tests
    - security
  ```
- This guarantees that the Docker image is built **only after** tests pass and security checks succeed.

By following these best practices, the CI workflow is now **faster, more efficient, and easier to maintain**.