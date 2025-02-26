# Moscow time web application

[![Python CI](https://github.com/MikitaDrazdou/S25-core-course-labs/actions/workflows/python-ci.yml/badge.svg?branch=lab3)](https://github.com/MikitaDrazdou/S25-core-course-labs/actions/workflows/python-ci.yml)

## Overview

A simple web application built with FastAPI that displays the current time in Moscow. The application updates the time on each page refresh, providing real-time Moscow time information.

## Features

- RESTful API endpoint
- Returns current Moscow time
- Timezone handling using pytz
- Comprehensive test suite

## Prerequisites

- Python 3.8+
- Docker (optional, for containerization)

## Local installation

1. Clone the repository

```bash
git clone <repository-url>
cd app_python
```

2. Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
python app.py
```

5. Access the application
Open your browser and navigate to: <http://127.0.0.1:8000>

The page will display the current Moscow time in the format: YYYY-MM-DD HH:MM:SS

## Docker

### Building the image

```bash
docker build -t your-dockerhub-username/moscow-time-api:latest .
```

### Pulling the image

```bash
docker pull your-dockerhub-username/moscow-time-api:latest
```

### Running the container

```bash
docker run -d -p 8000:8000 your-dockerhub-username/moscow-time-api:latest
```

The API will be available at <http://localhost:8000>

### API endpoints

- `GET /`: Returns the current time in Moscow

### Features

- Lightweight Alpine-based image
- Runs as non-root user for security
- Optimized for minimal image size
- Follows Docker best practices

## Unit tests

The application includes a comprehensive test suite built with pytest. The tests cover:

- API endpoint functionality
- Time format validation
- Timezone accuracy

### Running tests

Make sure you're in the app_python directory and have activated your virtual environment:

```bash
# Activate virtual environment if not already activated
source .venv/bin/activate  # On Unix/macOS
.venv\Scripts\activate     # On Windows

# Install test dependencies if not already installed
pip install -r requirements.txt

# Run tests in different ways:

# 1. Run all tests
pytest

# 2. Run tests with verbose output
pytest -v

# 3. Run tests with coverage report
pytest --cov=app

# 4. Run tests with coverage and generate HTML report
pytest --cov=app --cov-report=html

# 5. Run a specific test file
pytest test_app.py

# 6. Run a specific test function
pytest test_app.py::test_read_main
```

The tests will verify:

- API endpoint responses
- Time format correctness
- Moscow timezone accuracy

For detailed information about the tests and testing practices, see [PYTHON.md](PYTHON.md).

## Continuous integration

This project uses GitHub Actions for continuous integration. The CI pipeline includes:

### Automated workflows

1. **Testing**
   - Runs all unit tests
   - Performs code linting with flake8
   - Generates code coverage reports
   - Uses pip caching for faster builds

2. **Docker**
   - Builds Docker image
   - Pushes to Docker Hub
   - Implements layer caching for build optimization

3. **Security**
   - Runs Snyk security scanning
   - Checks for vulnerabilities in dependencies
   - Enforces security best practices

### CI configuration

The CI workflow is triggered on:

- Push to repository (affecting Python app files)
- Pull request creation/updates (affecting Python app files)

For detailed information about CI implementation and best practices, see [CI.md](CI.md).

### Required Secrets

To enable CI functionality, the following secrets need to be configured in GitHub:

- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: Your Docker Hub access token
- `SNYK_TOKEN`: Your Snyk API token

## Docker support

For Docker-related instructions and best practices, please refer to [DOCKER.md](DOCKER.md).

## API documentation

### Endpoints

#### GET /

Returns the current time in Moscow timezone.

Response format:

```json
{
    "current_time": "YYYY-MM-DD HH:MM:SS"
}
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License.
