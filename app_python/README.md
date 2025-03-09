# Overview

[![Python package](https://github.com/RwKaLs/S25-core-course-labs/actions/workflows/python-ci.yml/badge.svg?branch=lab3)](https://github.com/RwKaLs/S25-core-course-labs/actions/workflows/python-ci.yml)

This web application displays the current time in Moscow and updates it every second. It uses Flask web framework and follows the best Python web practices.

The application is able to return number of visits of the main app page on `/visits` endpoint.

## Tools

`Flask`: Chosen for its lightweight, ideal for small web applications like Moscow-time showing.

`pytz`: Properly handles timezone.

## Installation and run

1. Clone repo
2. Navigate to `app_python` directory
3. Install dependencies `pip install -r requirements.txt`
4. Run using `python app.py`
5. Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and observe correct Moscow time

## Docker

This application is containerized with Alpine image because of its lightweight.

Dockerhub: [link](https://hub.docker.com/repository/docker/rwkals/app_python)

### Building

From folder with Dockerfile:

```shell
docker build -t rwkals/app_python:latest .
```

### Pulling

```shell
docker pull rwkals/app_python:latest
```

### Running

```shell
docker run -p 5000:5000 rwkals/app_python:latest
```

## Distroless Image

A distroless image, smaller and more secure. Details in [link](DOCKER.md)

Dockerhub: [link](https://hub.docker.com/repository/docker/rwkals/app_python_distroless)

### Distroless Building

From folder with distroless.Dockerfile:

```shell
docker build -t rwkals/app_python_distroless:latest -f distroless.Dockerfile .
```

### Distroless Pulling

```shell
docker pull rwkals/app_python_distroless:latest
```

### Distroless Running

```shell
docker run -p 5000:5000 rwkals/app_python_distroless:latest
```

## Unit tests implementation

Unit tests are implemented for the Flask app to verify its functionality.
They check the main routes and ensure the application responds as expected.

Tests execution:

```shell
python -m unittest tests/test_app.py
```

More details are in [PYTHON.md](PYTHON.md)

## Continuous Integration Workflow

The project uses Github Actions for continuous integration.
CI workflow includes python dependencies installation, linting the code using `flake8`,
and running unit tests with `unittest`.
Moreover, it integrates docker steps: logging into Docker Hub, building and pushing the image.
