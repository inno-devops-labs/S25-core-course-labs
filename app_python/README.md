# Python Web Application

## Overview
This is a simple web application that displays the current time in Moscow. It is built using Flask, a lightweight Python web framework.

### Features
- Displays the current Moscow time.
- Refresh the page to see the updated time.
- Lightweight and fast.

## Requirements
- Python 3.8+
- Flask
- pytz

## Installation and Running Locally

### 1. Clone the repository:
```bash
git clone https://github.com/ramilevna/S25-core-course-labs.git
```

### 2. Navigate to the application directory:
```bash
cd app_python
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the application:
```bash
python app.py
```

### 5. Open the application in your browser:
```
http://127.0.0.1:8080/
```

## Running with Docker

### 1. Build the Docker image:
```bash
docker build -t ramilevna/app_python:latest .
```

### 2. Run the container:
```bash
docker run --rm -p 8080:8080 ramilevna/app_python:latest
```

### 3. Pull and run from Docker Hub:
```bash
docker pull ramilevna/app_python:v1.0
docker run --rm -p 8080:8080 ramilevna/app_python:v1.0
```

## Running with Distroless Image

To enhance security and efficiency, this application supports Distroless images.

### **Distroless Base Images Used:**
- **Python App**: `gcr.io/distroless/python3-debian12:nonroot`
- **JavaScript App**: `gcr.io/distroless/nodejs18-debian12:nonroot`

### **Key Benefits of Distroless:**
- Smaller image size
- No shell access (reduces attack surface)
- Optimized performance

### **Running the Distroless Version:**

### 1. Build the Distroless Image:
```bash
docker build -t app_python:distroless -f distroless.Dockerfile .
```

### 2. Run the Distroless Container:
```bash
docker run --rm -p 8080:8080 app_python:distroless
```

## Running Unit Tests

This project includes unit tests to ensure application reliability. The tests use `pytest` and are located in the `tests/` directory.

### Run the tests:
```sh
PYTHONPATH=. pytest tests/
```

# Python Application CI/CD Pipeline

![CI Status](https://github.com/ramilevna/S25-core-course-labs/actions/workflows/python-ci.yml/badge.svg)