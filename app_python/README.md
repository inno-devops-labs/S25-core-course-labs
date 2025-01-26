# Python Sample Application

## Overview

This is a simple python web application that shows current Moscow time.

## Installation and running

- Clone this repository and go to the project directory:

```bash
git clone https://github.com/mihdenis85/S25-core-course-labs.git -b lab1
cd S25-core-course-labs/app_python
```

- Install virtual environment and all dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- Run the application (via `gunicorn`) and test:

```bash
python -m gunicorn --bind 0.0.0.0:8080 app:app
curl localhost:8080
```

## Docker

### Build

```bash
cd S25-core-course-labs/app_python
docker build --tag docker_username/app_python:v1.0 .
```

Instead of docker username, use your own one.

### Pull and Run

```bash
docker pull mihdenis85/app_python:v1.0
docker run -p 8080:8080 mihdenis85/app_python:v1.0
```
