# Docker Best Practices

## Rootless Container

The container runs as a non-root user (`myuser`) for improved security.

## Layer Optimization

Layers are minimized by combining `COPY` and `RUN` commands, improving build performance.

## Use of `.dockerignore`

The `.dockerignore` file excludes unnecessary files (e.g., `.git`, `venv/`, `*.log`, `*.pyc`, `__pycache__`) to reduce image size.

## Specific Base Image Version

The `python:3.9-slim` image is used to ensure consistency and reduce image size.