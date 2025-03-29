[![CI for Python app](https://github.com/vtecovsky/S25-core-course-labs/actions/workflows/ci-python.yaml/badge.svg?branch=lab-3)](https://github.com/vtecovsky/S25-core-course-labs/actions/workflows/ci-python.yaml)

# Overview

This Python web application displays the current time in Moscow using FastAPI.

## Features

- Displays the current time in Moscow in the format `YYYY-MM-DD HH:MM:SS`
- Handles time zones using the `pytz` library
- Built with FastAPI

## Endpoints

### `GET /msc_time`

Returns the current time in Moscow.

**Response:**

```json
{
  "current_time": "2025-01-25 12:34:56"
}
```


### `GET /visits`

Returns total number of visits.

**Response:**

```json
{
  "visits": "11"
}
```

## Unit Tests

1. **Unit Testing**:  
   - Implemented tests for the `/msc_time` endpoint using FastAPI's `TestClient`.
   - Verified response formats and ensured time accuracy within a defined tolerance.

2. **Automated Testing**:  
   - Used `pytest` for running the test suite

## Local Installation

Follow the steps below to set up the application locally on your machine.

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/vtecovsky/S25-core-course-labs
cd app_python
```

### 2. Setup a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Running

```bash
python -m src.app
```

## Running in Docker container

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/vtecovsky/S25-core-course-labs
cd app_python
```

### Build

```bash
docker build -t vtecovsky/app_python:latest .
```

### Pull

Start by cloning the repository to your local machine:

```bash
docker pull vtecovsky/app_python:latest
```

### Run

Start by cloning the repository to your local machine:

```bash
docker run --rm -p 8000:8000 vtecovsky/app_python:latest
```

# **CI Workflow** 🚀  

My **Continuous Integration (CI) pipeline** is designed to ensure code quality, reliability, and smooth deployment. The workflow is triggered whenever changes are made to the `app_python/` directory.  

## **Pipeline Overview**  
The CI process consists of three key jobs:  

### 🔍 **1. Linting**
- Uses **Ruff** to enforce coding standards and detect potential issues.  

### 🧪 **2. Testing**
- Runs **pytest** to validate the correctness of the endpoint.  
- Ensures all tests pass before proceeding to the next stage.  

### 📦 **3. Build & Push**  
This step prepares and deploys the application using Docker:  
1. **Login** – Authenticates with Docker Hub.  
2. **Build** – Creates a Docker image of the application.  
3. **Push** – Uploads the built image to the container registry.  
