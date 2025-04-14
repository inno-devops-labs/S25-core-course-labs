# Continuous Integration Best Practices

This document outlines the CI/CD practices implemented in this project.

## Workflow Features

1. **Caching**: 
   - Pip package caching to speed up dependency installation
   - Cache key based on requirements.txt hash

2. **Security Scanning**:
   - Snyk integration for vulnerability scanning
   - Medium severity threshold for security issues
   - Automatic monitoring of dependencies

3. **Testing**:
   - Linting with flake8
   - Unit testing with pytest
   - Code coverage reporting

4. **Docker Integration**:
   - Automatic Docker image building on main branch push
   - Image tagging with both latest and commit SHA

## Best Practices

- Always run tests on both push and pull request events
- Use working-directory to isolate app_python operations
- Separate test and build jobs with dependency (needs)
- Use environment variables for configuration
- Implement severity thresholds for security scans 