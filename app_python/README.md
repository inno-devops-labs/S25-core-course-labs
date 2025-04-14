# Moscow Time WebApp

## Overview
Moscow Time WebApp is a simple web application that provides the current time in Moscow. The application serves the Moscow time via a REST API endpoint.

## Features
- Provides the current Moscow time in JSON format.
- Lightweight and easy to deploy.
- Dockerized for seamless container-based deployment.

## API Documentation

### Endpoint: `GET /`

**Response:**
```json
{
    "moscow_time": "2025-02-06 12:34:56"
}
```
- `moscow_time`: The current time in Moscow (UTC+3) formatted as `YYYY-MM-DD HH:MM:SS`.

## Running the Application

### Locally
```bash
python app_python/app.py
```
By default, the application starts on port `8000`. You can change the port by passing it as an argument:
```bash
python app_python/app.py 8080
```

### Using Docker
#### Build the Docker Image
```bash
docker build -t moscow-time-webapp app_python/
```

#### Run the Container
```bash
docker run -p 8000:8000 moscow-time-webapp
```

## Unit Tests
Unit tests are implemented using `pytest`. The test suite checks:
- The server starts and responds correctly.
- The response contains the `moscow_time` field.
- The `moscow_time` value is accurate within a small time margin.

To run the tests:
```bash
pytest app_python/tests/
```

## Continuous Integration (CI)
The project includes a GitHub Actions CI workflow that automates building, testing, and linting.

### CI Workflow Steps:
1. **Install Dependencies**: Sets up Python and installs required dependencies.
2. **Run Linter**: Uses `ruff` to ensure code quality.
3. **Run Tests**: Executes the test suite using `pytest`.
4. **Docker Build & Push**: Builds and optionally pushes the Docker image.
5. **Snyk Vulnerability Checks**: Ensures security compliance by scanning dependencies.

### CI Status Badge
![CI Status](https://github.com/dantetemplar/fork-S25-core-course-labs/actions/workflows/ci.yaml/badge.svg)

## License
This project is licensed under the MIT License.

## Author
**Ruslan Bel'kov**  
Email: [r.belkov@innopolis.university](mailto:r.belkov@innopolis.university)

