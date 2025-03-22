# Moscow Time Web Application

[![CI for app_python](https://github.com/cuprum-acid/devops-labs/actions/workflows/app_python.yml/badge.svg?branch=lab3)](https://github.com/cuprum-acid/devops-labs/actions/workflows/app_python.yml)

## Overview

This is a web app that shows current date and time in Moscow. It is written in Python with Bottle framework.

## Requirements

* Python 3.12

## Installation

Clone this repository:

```bash
git clone https://github.com/cuprum-acid/devops-labs.git -b lab1
```

Open directory:

```bash
cd devops-labs/app_python
```

Install virtual environment and dependencies:

```bash
python -m venv venv
```

```bash
source venv/bin/activate # Linux/Mac
```

```bash
venv\Scripts\activate # Windows
```

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python app.py
```

Now it is available on `localhost:8080` in browser. Or you can run in terminal:

```bash
curl localhost:8080
```

## Run tests

If you want to run automatic tests, then you need to install additional packages:

```bash
pip install pytest==8.3.4
```

```bash
pip install requests==2.32.3
```

They were not included in `requirements.txt` because they are not required to run application

After that run:

```bash
pytest test_app.py
```

## Docker

### Build

```bash
cd devops-labs/app_python
```

```bash
docker build -t ebob/moscow-time:v1.0 .
```

### Pull and Run

```bash
docker pull ebob/moscow-time:v1.0
```

```bash
docker run -d --name msk -p 8080:8080 ebob/moscow-time:v1.0
```

Now it is available on `localhost:8080`

## Distroless Docker Image

### Build

```bash
docker build -t ebob/moscow-time:v1.0-distroless -f distroless.Dockerfile .
```

### Pull and Run

```bash
docker pull ebob/moscow-time:v1.0-distroless
```

```bash
docker run -d --name msk-distroless -p 8081:8080 ebob/moscow-time:v1.0-distroless
```

Now it is available on `localhost:8081`

## Continuous Integration

This repository contains a CI pipeline configuration for the python application. The CI pipeline is managed with `GitHub Actions` and includes multiple jobs to ensure the code quality, functionality, security, and successful deployment of the application.

The pipeline consists of these main jobs:

1. Lint and Format: Ensures the code follows linting and formatting standards.
2. Test: Runs tests to verify the correctness of the application.
3. Security Scan: Checks for security vulnerabilities in the codebase using `Snyk` tool.
4. Docker Build and Push: Builds and pushes a Docker image to the DockerHub and ghcr.
