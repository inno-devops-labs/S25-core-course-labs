# Moscow Time Web-Application

[![Python Application CI](https://github.com/azamatbayramov/S25-core-course-labs/actions/workflows/app_python.yml/badge.svg)](https://github.com/azamatbayramov/S25-core-course-labs/actions/workflows/app_python.yml)

## About

This is a simple web application on Python that displays the current time in Moscow.

## How to Use

### Manual

1. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

2. Run the application using the one of the following commands:

```bash
python main.py
```

```bash
uvicorn --host 0.0.0.0 --port 8001 main:app
```

3. Open your web browser and navigate to `http://0.0.0.0:8001/` to view the current time in Moscow.

### Regular Docker Image

1. Build or pull the Docker image.

- Build the Docker image using the following command:

```bash
docker build -t azamatbayramov/s25-devops-py .
```

- Pull the Docker image from Docker Hub using the following command:

```bash
docker pull azamatbayramov/s25-devops-py
```

2. Run the Docker container using the following command:

```bash
docker run -p 8001:8001 azamatbayramov/s25-devops-py
```

3. Open your web browser and navigate to `http://0.0.0.0:8001/` to view the current time in Moscow.

### Distroless Docker Image

1. Build or pull the Docker image.

- Build the Docker image using the following command:

```bash
docker build -t azamatbayramov/s25-devops-py-dl -f distroless.Dockerfile .
```

- Pull the Docker image from Docker Hub using the following command:

```bash
docker pull azamatbayramov/s25-devops-py-dl
```

2. Run the Docker container using the following command:

```bash
docker run -p 8001:8001 azamatbayramov/s25-devops-py-dl
```

3. Open your web browser and navigate to `http://0.0.0.0:8001/` to view the current time in Moscow.

## Unit Tests

1. Install the required dependencies using the following command:

```bash
pip install -r requirements-test.txt
```

2. Run the unit tests using the following command:

```bash
pytest test_main.py
```

## CI Workflow

The CI workflow for this application is defined in the `.github/workflows/app_python.yml` file.

It consists of the following steps:

- **Build and Test**:
    - Sets up the Python environment.
    - Installs dependencies.
    - Lints the code using `flake8` and `black`.
    - Runs the unit tests using `pytest`.
    - Scans for vulnerabilities using Snyk.
- **Build and Push**:
    - Sets up Docker Buildx.
    - Logs in to Docker Hub.
    - Builds and pushes the Docker image using the `distroless.Dockerfile`.

## Endpoints

- `/` - Displays the current time in Moscow as an HTML response using `/api/time` endpoint.
- `/api/time` - Returns the current time in Moscow as a JSON response.
- `/docs` - Interactive OpenAPI documentation.
