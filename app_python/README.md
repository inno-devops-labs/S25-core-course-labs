# Moscow Time Web Application

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![FastAPI](https://img.shields.io/badge/Framework-FastAPI-green)
![CI/CD Workflow](https://github.com/yeaphm/S25-core-course-labs/actions/workflows/python_app_ci.yml/badge.svg)

## Overview

A simple web application that displays the current time in **Moscow (MSK)** using Python and FastAPI.  

---

## Features  

- Real-time Moscow time (UTC+3) using `pytz`.  
- PEP8-compliant code with clean structure.  
- Interactive API documentation (Swagger UI and ReDoc).  

---

## Prerequisites  

- **Python 3.8 or later** must be installed on your system.  
  - Download Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
  - Verify installation:  

    ```bash
    python --version  # Should return "Python 3.x.x"
    ```

---

## Local Installation  

1. **Clone the repository**:  

   ```bash
   git clone https://github.com/yeaphm/S25-core-course-labs.git
   cd app_python
   ```

2. **Set up a virtual environment**:  

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:  

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:  

   ```bash
   uvicorn app:app --host 0.0.0.0 --port 5000
   ```

5. **Access the app**:  
   Open `http://localhost:5000` in your browser.  

6. **Explore API docs**:  
   Visit `http://localhost:5000/docs` for interactive API documentation.  

---

## Dependencies  

- FastAPI (web framework)  
- Uvicorn (ASGI server)  
- pytz (timezone handling)  

See [`requirements.txt`](./requirements.txt) for details.

## Docker Instructions

[Dockerhub](https://hub.docker.com/r/efimpuzhalov/moscow-time-python-app)

### Build the Image

```bash
docker build -t dockerhub-username/moscow-time-app:latest .
```

### Pull from Docker Hub

You can use mine image:

```bash
docker pull efimpuzhalov/moscow-time-app:latest
```

### Run the Container

```bash
docker run -p 5000:5000 efimpuzhalov/moscow-time-app:latest
```

### Verify

Access the app at `http://localhost:5000`.

**Key Features**:  

- 🛡️ Runs as non-root user (`appuser`).  
- 🐳 Optimized layers for faster builds.  
- 🔒 Security-hardened with `.dockerignore`.

## Distroless Image Version

[Dockerhub](https://hub.docker.com/r/efimpuzhalov/moscow-time-python-app-distroless)

### Usage

```bash
# Build Distroless version
docker build -f distroless.Dockerfile -t moscow-time-distroless .

# Run container
docker run -p 5000:5000 moscow-time-distroless

# Or use pre-built image
docker run -p 5000:5000 efimpuzhalov/moscow-time-python-app-distroless:latest
```

### Distroless Features

- 🔒 **Non-Root Execution**: Runs as UID 1000 by default
- 🛡️ **Security First**: No shells (bash/sh) or package managers
- 📦 **Dependency Control**: Only explicitly installed Python packages

## Unit Tests

Unit tests are implemented to ensure the correctness and reliability of the application's functionality. They validate that the `/` endpoint returns the accurate current time in Moscow (UTC+3).

### Running Tests

To execute the unit tests, follow these steps:

1. **Ensure Dependencies Are Installed**:

   ```bash
   pip install -r requirements.txt -r requirements-dev.txt
   ```

2. **Run the Tests**:

   ```bash
   pytest test_app.py
   ```

### Test Details

- **Framework** : pytest
- **Test File** : test_app.py
- **Description** :
  - Simulates a GET request to the `/` endpoint using `fastapi.testclient.TestClient`.
  - Compares the returned time with the current Moscow time generated using `pytz`.
  - Allows for a ±5-second tolerance to account for potential execution delays.
- **Assertions** :
   Verifies the HTTP status code is `200` (OK).
   Ensures the returned time matches the expected Moscow time within the allowed tolerance.

### Best Practices Applied

- **Isolation** : Tests are independent and do not rely on external services or shared state.
- **Validation** : Assertions are used to verify both the structure and content of the API response.
- **Timezone Handling** : Accurate timezone handling is ensured using `pytz`.

## **CI Pipeline Overview**

This repository includes a **GitHub Actions CI** pipeline to ensure high-quality code, security, and automated deployment.

### **🔄 CI Workflow Triggers**

The workflow runs on **pull requests** affecting:

- The `app_python/` directory.
- The `.github/workflows/app_python.yml` file.

### **🛠️ CI Workflow Steps**

#### **1️⃣ Build, Lint, and Test**

- Installs dependencies using `pip`.
- Runs `flake8` for linting (max line length: 88).
- Executes `pytest` to validate functionality.

#### **2️⃣ Security Check**

- Uses **Snyk** to scan dependencies for security vulnerabilities.

#### **3️⃣ Docker Build & Push**

- Builds and pushes **two images**:
  - **Alpine-based image** (`latest` tag).
  - **Distroless-based image** (`distroless` tag).
- Pushes images to Docker Hub under `${{ secrets.DOCKER_USERNAME }}`.
