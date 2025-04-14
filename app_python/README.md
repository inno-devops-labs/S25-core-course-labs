## Overview
A simple web application that displays the current time in Moscow.

## Installation
Installing of dependencies:
`pip install -r requirements.txt`

## Start
`python app.py`;
Checkout `http://localhost:5000`

## Docker Instructions:

## How to build an image?
`docker build -t myapp:latest .`

## How to launch the container?
`docker run --rm -p 5000:5000 myapp`

## How to send an image to Docker Hub?
`docker tag myapp username/myapp:latest`
`docker push username/myapp:latest`

## How to launch a container from Docker Hub?
`docker pull username/myapp:latest`
`docker run --rm -p 5000:5000 username/myapp:latest`

## Unit Tests:

**Running tests**
To run all tests:
- `python -m unittest discover app_python/tests`


## Python CI/CD
Automatically performs:
- Install dependencies.
- Linter `flake8`.
- Unit tests `unittest`.
- Build and publish Docker image to Docker Hub.

## Python CI Status
![Python CI](https://github.com/AlexeyKureykin/S25-core-course-labs/actions/workflows/ci-python.yml/badge.svg)
