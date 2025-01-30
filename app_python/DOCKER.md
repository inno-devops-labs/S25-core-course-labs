# Docker Documentation

## Link
https://hub.docker.com/repository/docker/netpo4ki/python-web/general

`netpo4ki/python-web:latest`

## Dockerfile Best Practices

1. **Multi-Stage Builds**: Used to reduce the final image size by separating the build and runtime environments.
2. **Non-Root User**: The application runs as a non-root user (`appuser`) for security.
3. **Layer Caching**: Dependencies are installed in a separate layer to leverage caching.
4. **Minimal Base Image**: `python:3.10-alpine` is used to reduce the image size.
5. **Environment Variables**: `PATH` is updated to include user-installed binaries.