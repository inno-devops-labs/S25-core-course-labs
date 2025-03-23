# time_service_python

![Workflow Status](https://github.com/nai1ka/S25-core-course-labs/actions/workflows/app_python.yml/badge.svg)

A simple Python Web application to show current time in Moscow.

## Prerequisites

- [Python](https://www.python.org/downloads/)
- [FastApi](https://fastapi.tiangolo.com/)

## Install

Clone the repository:

```sh
git clone https://github.com/nai1ka/S25-core-course-labs
cd S25-core-course-labs/app_python
```

Create and activate virtual environment:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```sh
pip install -r requirements.txt
```

Run the app:

```sh
python app/main.py
```

The server will be available at [http://localhost:8000](http://localhost:8000)

## Docker

### Building

To build the image, run:

```sh
docker build -t nai1ka/time-service:latest .
```

You can use any tag you want instead of `nai1ka/time-service:latest`.

### Pulling

To pull the image from the Docker Hub, run:

```sh
docker pull nai1ka/time-service:latest
```

### Running

To run the container, run:

```sh
docker run -p 8000:8000 nai1ka/time-service:latest
```

Don't forget to replace `nai1ka/time-service:latest` with the tag you are using.

## Distroless Image Version

You can also build a distroless image:

```sh
# Build the image
docker build -t time-service-distroless -f distroless.Dockerfile .
# Run the container
docker run -p 8000:8000 time-service-distroless
```

## Unit Tests

The project includes Unit tests. They are located in the `tests` directory and used to automatically test the app.\
To run them manually, execute the following command inside the `app_python` directory:

```sh
pytest tests
```

Note: you may require to install dependencies for testing:

```sh
pip install -r requirements-test.txt
```

## CI workflow

The repository has a GitHub Actions workflow that runs the linter, unit tests and security check on every push to the repository.

### Steps

1. Building, linting and testing\
    In this step, the following actions are performed:
    - Installing the dependencies
    - Linting the code using flake8
    - Running the unit tests using pytest
2. Security check using Snyk
3. Building the distroless Docker image and pushing it to the Docker Hub
    - This step is triggered only when all of the previous steps are successful

Notes:

- The workflow is defined in `.github/workflows/app_python.yml`
- The workflow is triggered only when changes occur in the `app_python` directory or `.github/workflows/app_python.yml` file.

## Counting Visits

This application is able to count total number on visits on any page. To acces this data you may use the `\visits` endpoint. The number is stored in the `visits.txt` file.
Also, `docker-compose.yml` inside of `monitoring` folder mounts it to a volume, so the data will not be lost after the container is stopped.

## Structure

Directory structure (dotfiles are omitted):

```sh
.
├── CI.md
├── DOCKER.md
├── Dockerfile
├── PYTHON.md
├── README.md
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── index.py
│   └── utils
│       ├── __init__.py
│       ├── config.py
│       └── time_helper.py
├── distroless.Dockerfile
├── pytest.ini
├── requirements-test.txt
├── requirements.txt
├── templates
│   └── index.html
└── tests
    ├── __init__.py
    └── test_time.py
```
