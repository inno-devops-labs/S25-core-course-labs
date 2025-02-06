# Continuous Integration (CI) for Python Project

## Introduction

This document outlines the best practices for setting up continuous integration (CI) workflows for a Python project
using GitHub Actions. It includes details about setting up linting, testing, building, and pushing a Docker image for
deployment.

## CI Workflow Overview

The CI workflow consists of two main jobs:

1. **Build**: This job installs dependencies, runs linters, and executes tests.
2. **Docker**: This job builds a Docker image of the Python application.

## Best Practices Applied

1. **Use of python -m pip**

To ensure consistency and avoid potential issues with system-installed Python, we use python -m pip for upgrading pip
and installing dependencies.

2. **Automating testing with pytest**

Automating tests as part of the CI process ensures that any changes are validated before being deployed. We use pytest
to run the tests, which helps identify any issues early.

3. **Efficient Docker Image build**

We use a multi-stage Docker build to minimize the size of the final Docker image. This separates the build environment
from the runtime environment, ensuring only the necessary files are included in the final image.

4. **Version pinning in requirements.txt**

Pinning package versions in the requirements.txt file ensures that the application uses consistent versions of
dependencies across all environments.

5. **Flake8 for code quality**

We incorporate flake8 as a linter to check for style violations and maintain code quality. This step ensures that code
follows the PEP 8 style guide, improving readability and consistency.
