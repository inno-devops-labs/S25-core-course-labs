# Python Web Application: Moscow Time

[![CI Workflow](https://github.com/dprostiruk/S25-core-course-labs/actions/workflows/ci.yml/badge.svg?branch=lab3)](https://github.com/dprostiruk/S25-core-course-labs/actions/workflows/ci.yml)

## Introduction

This is a simple web application built with Python and Flask to display the current time in Moscow. The time updates whenever the page is refreshed.

### Instructions

1. Clone this repository:

```bash
https://github.com/dprostiruk/S25-core-course-labs.git
```

2. Navigate to the `app_python` folder:

```bash
cd app_python
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

5. Open a browser and visit:

`http://127.0.0.1:5000/`

> *Note*: Ensure your system's timezone settings are correct to display the accurate Moscow time.

## Unit Tests

Unit tests have been implemented using the `unittest` framework to ensure the reliability of the application. The following tests are included:

- **Response Status Test**: Verifies that accessing the `/` route returns a `200 OK` status.
- **Content Test**: Ensures that the response contains the expected text (`Current Time in Moscow:`).

To run the tests, execute:

```bash
python -m unittest discover app_python
```

These tests are also integrated into the CI workflow to maintain application stability.

## CI Workflow

A GitHub Actions workflow is set up for continuous integration, which includes:
- **Linting**: Ensures code follows PEP 8 using `flake8`.
- **Testing**: Runs unit tests automatically.
- **Docker Integration**: Builds and pushes a Docker image to Docker Hub.

## Docker commands
### Build the Docker Image

```bash
docker build -t shelma13/app_python .
```

### Run the container locally

```bash
docker run -p 5000:5000 shelma13/app_python
```

### Push Image to Docker Hub

```bash
docker tag shelma13/app_python shelma13/app_python:latest
docker push shelma13/app_python:latest
```

### Pull and Run from Docker Hub

```bash
docker pull shelma13/app_python:latest
docker run -p 5000:5000 shelma13/app_python:latest
```

### Requirements

- Python 3
- Flask
- pytz

### Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [Flask Framework](https://flask.palletsprojects.com/)
- [Timezones in Python](https://docs.python.org/3/library/datetime.html#time-zones)
