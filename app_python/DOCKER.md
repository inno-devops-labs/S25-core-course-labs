# Docker Best Practices for Python Web Application

## Overview
This document details the Docker best practices used in containerizing the Python web application.

## Best Practices Implemented

### 1. **Minimal and Specific Base Image**
- Chose `python:3.10-alpine3.15` for a lightweight, secure base image.

### 2. **Running as Non-Root User**
- Added a new user `appuser` to prevent privilege escalation:
  ```dockerfile
  RUN addgroup -S appgroup && adduser -S appuser -G appgroup
  USER appuser

### 3. **Using .dockerignore**
- Excluded unnecessary files like __pycache__/, .git/, and .env to speed up builds.

### 4. **Efficient Layering**
- Installed dependencies separately to leverage Docker’s caching mechanism:
```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
```

### 5. **Environment Variables for Security**
- Disabled Python buffering and unnecessary pip features for a cleaner image:
```dockerfile
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1
```
### 6. **Exposing Only Necessary Ports**
- Restricted to only port `5000` for security:
```dockerfile
EXPOSE 5000
```