# Python Moscow time application

![workflow](https://github.com/m0t9/S25-core-course-labs/actions/workflows/app_python.yml/badge.svg)

## Overview

This web application returns Moscow time on the `/` page.

## Local installation and running

```bash
# Installing the repo itself
git clone https://github.com/m0t9/S25-core-course-labs -b lab1

# Setup virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
cd S25-core-course-labs/app_python

# Running
uvicorn main:app --reload

# Testing
curl http://127.0.0.1:8000
```

## Docker

### Build

```bash
cd S25-core-course-labs/app_python
docker build -t pyapp .
```

### Pull & Run

```bash
# Pulling the image
docker pull m0t9docker/pyapp:latest

# Running the container
docker run -d -p 8000:8000 m0t9docker/pyapp:latest

# Testing
curl http://127.0.0.1:8000
```

### Distroless Image Version

#### Build

```bash
cd S25-core-course-labs/app_python
docker build -f distroless.Dockerfile -t pyapp_distro .
```

#### Pull & Run

```bash
# Pulling the image
docker pull m0t9docker/pyapp_distro:latest

# Running the container
docker run -d -p 8000:8000 m0t9docker/pyapp_distro:latest

# Testing
curl http://127.0.0.1:8000
```

## Testing

```bash
pytest test_main.py
```
