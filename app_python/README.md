# Moscow Time Web App

## Overview
This is a simple Python web application using **Flask** that displays the **current time in Moscow**. The time updates each time the page is refreshed.

## Installation Guide

### Prerequisites
- Python 3 installed
- `pip` installed

### Steps to Run Locally
1. Clone this repository:
   ```bash
    https://github.com/SuleimanKarimEddin/S25-core-course-labs/tree/master
    cd S25-core-course-labs
    git checkout lab1
    cd app_python
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python app.py 
    docker build -t suleimankrimeddin/app_python:latest .
   ```

# Docker Best Practices

## Best Practices Implemented

1. **Rootless Container**: The application runs as a non-root user (`appuser`).
2. **Minimal Base Image**: Used `python:3.11-alpine3.18` for security and efficiency.
3. **Layer Optimization**:
   - Only copied required files (`COPY requirements.txt ./` first, then `COPY app.py ./`).
   - Used `--no-cache-dir` to reduce image size.
4. **.dockerignore Usage**: Prevents unnecessary files from being included in the image.
5. **Exposed Only Required Ports**: Used `EXPOSE 5000` to keep attack surface minimal.
6. **Environment Variables & Security**:
   - No hardcoded credentials inside the image.
   - Uses Alpine to minimize vulnerabilities.

## **Testing and Deployment**
- Built and tested the image locally before pushing to Docker Hub.
- Ensured proper functionality by running the container and accessing the web app.
- docker pull suleimankrimeddin/app_python:v1.0
- docker run -p 5000:5000 suleimankrimeddin/app_python:v1.0

- docker pull suleimankrimeddin/app_python:distroless-v1.0
- docker run -p 5000:5000 suleimankrimeddin/app_python:distroless-v1.0

## **🔍 Image Size Comparison**
   - Image Version	Size
   - Regular Image	~100MB
   - Multi-Stage Image	~80MB
   - Distroless Image	~50MB


