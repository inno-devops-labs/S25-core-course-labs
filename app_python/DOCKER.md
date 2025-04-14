# Docker Best Practices in Django Project

## Best Practices Applied

### 1. **Minimal & secure base image**
- Used **`python:3.11-alpine3.18`**, a lightweight Alpine Linux image, reducing attack surface and size.

### 2. **Rootless execution**
- Created a **non-root user (`appuser`)** to prevent privilege escalation.

### 3. **Optimization**
- Used **COPY only for required files** (`requirements.txt`, `manage.py`, `time_app/`).
- Installed Python dependencies in a **single `RUN` statement** to reduce layers.

### 4. **Caching**
- **Pip install happens before copying the app files**, leveraging Docker cache for dependencies.

### 5. **Exclusion of unnecessary files**
- Used `.dockerignore` to prevent unnecessary files from being added to the image.


## Distroless Dockerfile vs. Dockerfile
The distroless image will typically be smaller than the standard image because it includes only the app's runtime environment and its dependencies, without unnecessary libraries or OS files.
![
](image.png)


