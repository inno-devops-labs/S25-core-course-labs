# Continuous Integration (CI) Documentation

## Best Practices
- **Caching**: Speeds up builds by reusing dependencies. For Python, we cache pip dependencies; for Node.js, we cache npm packages.
- **Linting**: Ensures code quality. We use `flake8` for Python and `ESLint` for Node.js.
- **Testing**: Python unit tests are executed with `pytest`, while Node.js tests run using `jest` (or `mocha` if configured).
- **Docker**: Automated build and push to the Docker registry are integrated for both applications.
- **Security**: Snyk vulnerability checks are included to identify and address security issues.
- **Status Badge**: Provides immediate visibility of workflow status in the repository's README.

## Workflow Overview

### Python CI Workflow
1. **Checkout** → **Set up Python** → **Cache pip dependencies** → **Install Python dependencies** → **Lint with flake8** → **Run pytest tests** → **Docker login, build, and push**.
2. This workflow triggers on push and pull request events specifically for changes in the `app_python/` directory.

### Node.js CI Workflow
1. **Checkout** → **Set up Node.js** → **Cache npm dependencies** → **Install Node.js dependencies** → **Lint with ESLint** → **Run tests using jest/mocha** → **Docker login, build, and push**.
2. This workflow triggers on push and pull request events specifically for changes in the `app_nodejs/` directory.

By incorporating these workflows, our CI pipeline ensures that both the Python and Node.js applications are built, tested, and deployed in a secure and efficient manner.
