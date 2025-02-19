# Best Practices in Python Application CI

- __Trigger Conditions__: Runs on pull requests to `master` and specific file/folders changes.
- __Consistent Environment__: Uses `ubuntu-22.04` and sets a working directory.
- __Python Version__: Specifies Python version (`3.12`) and installs dependencies from multiple files.
- __Code Quality__: Lints code with `flake8` and `black`.
- __Testing__: Runs tests using `pytest`.
- __Security__: Scans for vulnerabilities with Snyk.
- __Job Order__: Runs testing first, then builds the Docker image if tests pass.
- __Docker__: Builds and pushes Docker images with proper setup and login actions.
- __Caching__: Speeds up builds using Docker and pip caching.
- __Secrets__: Keeps sensitive data safe with GitHub Secrets.
