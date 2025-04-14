# app_python

[![app-python](https://github.com/2IMT/S25-core-course-labs/actions/workflows/app-python.yml/badge.svg)](https://github.com/2IMT/S25-core-course-labs/actions/workflows/app-python.yml)

This web application displays current time in Moscow

## Running

- Install dependencies

```console
pip install -r requirements.txt
```

- Run the server

```console
uvicorn main:app
```

- The server's address will be `http://127.0.0.1:8000`

## Docker

### Building The Image

```console
docker build -t 2imt/app_python:1.2 .
```

### Pulling The Image

```console
docker pull 2imt/app_python:1.2
```

### Running The Image

```console
docker run --rm -p 8000:8000 2imt/app_python:1.2
```

## Unit Tests

### Dependencies

`pytest`

### Running Tests

```console
pytest .
```

## CI Workflow

- **Dependencies**: Installs the required Python dependencies.
- **Linting**: Runs `flake8` to check the code style and potential issues.
- **Testing**: Runs tests using `pytest` to ensure the project is functioning correctly.
- **Docker**: Builds and pushes a Docker image to Docker Hub.
- **Security**: Checks for vulnerabilities using Snyk.
