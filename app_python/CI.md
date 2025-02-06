
# CI Workflow Best Practices

## Workflow Configuration
- **Triggering the Workflow**: The workflow is triggered on pull requests and push events to the `master` and `lab3` branches. This ensures that changes are tested before merging.
- **Path Restrictions**: The workflow runs only if changes are made to the specified paths, which reduces unnecessary runs.

## Caching Dependencies
- **Dependency Caching**:
  - Utilizes GitHub Actions' caching to store pip dependencies.
  - This significantly speeds up future installations by avoiding redundant downloads.

### Example Caching Configuration:
```yaml
- name: Cache pip dependencies
  uses: actions/cache@v3
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

## Code Quality Checks
Linting with Flake8:
Integrates flake8 to enforce coding standards and maintain code quality.
Ensures consistent style and error detection across the codebase.
### Example Linting Command:
```yaml
- name: Lint Code (flake8)
  run: |
    pip install flake8
    flake8 app_python/main.py app_python/ut/
```

## Running Tests
### Unit Testing:
Uses Python’s built-in unittest framework to automate testing of the application.
Ensures that functionality remains intact with continuous changes to the codebase.
### Example Test Execution:
```yaml
- name: Run Unit Tests
  run: |
    python -m unittest discover app_python/ut
```
## Docker Integration
- Building and Pushing Docker Images:
- Automates the process of building a Docker image and pushing it to Docker Hub after successful tests.
- Ensures that the latest version is always available in the container registry.
### Docker Build and Push Configuration:
```yaml
- name: Build and Push Docker Image
  uses: docker/build-push-action@v6
  with:
    context: ./app_python
    file: ./app_python/Dockerfile
    push: true
    tags: ${{ secrets.DOCKER_USERNAME }}/devopsapp:latest
```

## Security Checks
Snyk Integration:
Implements Snyk for vulnerability scanning of dependencies to identify and address potential security issues.
### Example Snyk Configuration:
```yaml
- name: Run Snyk Vulnerability Scan
  uses: snyk/actions/python@master
  env:
    SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
  with:
    args: --file=app_python/requirements.txt
```

