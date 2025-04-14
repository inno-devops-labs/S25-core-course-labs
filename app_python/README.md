# Moscow Time Web Application

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![FastAPI](https://img.shields.io/badge/Framework-FastAPI-green)  

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
