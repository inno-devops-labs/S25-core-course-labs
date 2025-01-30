# Docker Best Practices for Region Time API

This document outlines the best practices implemented in our Docker setup to ensure security, efficiency, and maintainability.

## Non-root User

### Security Enhancement

Running containers as non-root users is a critical security practice. By default, Docker runs processes as root inside the container, which poses significant risks if the container is compromised.

In the Dockerfile, we create a non-root user named `appuser`:

```
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser
```
By switching to this non-root user before running the application, we mitigate potential damage from vulnerabilities.

By switching to this non-root user before running the application, we mitigate potential damage from vulnerabilities.

## Layer Optimization

### Efficient Use of Layers

Docker images are composed of multiple layers. Each command in the Dockerfile creates a new layer. Optimizing these layers can significantly improve build times and reduce image sizes.

#### Layer Caching

Copying `requirements.txt` first and install dependencies separately from copying the application code. This allows Docker to cache the dependency installation layer, speeding up subsequent builds when only the application code changes:

```
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY ./main.py /app/
```

## Precise Base Image Version

### Consistency and Stability

Using a precise version of the base image ensures consistency and avoids unexpected changes due to updates in the base image.

In the Dockerfile, we specify the exact version of the base image:

```
FROM python:3.9-alpine3.15
```

## Use of .dockerignore

### Improved Build Efficiency

The `.dockerignore` file excludes unnecessary files and directories from being included in the Docker image, reducing the size and improving build times.

## Rootless Container

### Principle of Least Privilege

By ensuring the application runs as a non-root user, we follow the principle of least privilege, enhancing security. This means the application has only the minimum level of access required to perform its functions, minimizing the risk of unauthorized access and damage.
