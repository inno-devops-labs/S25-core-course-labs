# Docker Best Practices

This document outlines the Docker best practices implemented in this project.

## Best Practices

1. **Non-Root User**:
   - The container runs as a non-root user (`appuser`) for improved security.

2. **Minimal Base Image**:
   - The `python:3.9-slim` base image is used to reduce the image size.

3. **Layer Optimization**:
   - Commands are combined in the `Dockerfile` to minimize the number of layers.
   - The `--no-cache-dir` flag is used with `pip install` to avoid caching and reduce image size.

4. **Precise Versioning**:
   - Specific versions are used for the base image (`python:3.9-slim`) and dependencies.

5. **.dockerignore File**:
   - Unnecessary files are excluded using a `.dockerignore` file.

6. **COPY Only Necessary Files**:
   - Only the `requirements.txt` and `app.py` files are copied into the image to keep it lightweight.

## Docker Commands

- **Build the Docker Image**:
  ```bash
  docker build -t vika123vika/app-python:latest .
