## Introduction

Hey there! For this lab assignment, I containerized the **Moscow Time** web application using Docker while following
best practices. Instead of using a standard `python` image, I opted for a **non-root** base image to improve security.
Additionally, I created an efficient `.dockerignore` file to exclude everything except the necessary files.

## Why Docker?

- **Portability**: The container runs the same way on any machine with Docker installed.
- **Security**: Running as a non-root user reduces attack surface.
- **Efficiency**: Using a minimal, precise base image improves performance.
- **Reproducibility**: Ensures the same environment across different deployments.

## Docker Best Practices Implemented

1. **Non-Root Base Image**
    - Used `python:3.13-alpine` with a **predefined non-root user**.
    - No manual user creation needed—ensuring a **secure container**.

2. **Minimal `.dockerignore`**
    - Ignored **everything** except `app.py`, `Dockerfile`, `README.md`, and `DOCKER.md`.
    - Prevented unnecessary files from being copied into the container.

3. **Efficient Docker Layers**
    - Used `COPY . /app/` since `.dockerignore` already filters unnecessary files.
    - Installed dependencies (no deps yet actually, but in the future...) **before copying source code** to leverage **layer caching**.

4. **Lightweight Base Image**
    - Used `python:3.13-alpine` instead of `python:latest` to **reduce size**.

## Building and Running the Docker Container

### 1. Build the Image

```sh
docker build -t moscow-time-webapp .
```

### 2. Run the Container

```sh
docker run -d -p 8000:8000 --name moscow-time moscow-time-webapp
```

### 3. Test the Application

```sh
curl http://localhost:8000
```

Expected response:

```json
{
  "moscow_time": "2025-01-30 14:15:00"
}
```

## Pushing to Docker Hub

### 1. Log in to Docker Hub

```sh
docker login
```

### 2. Tag the Image

```sh
docker tag moscow-time-webapp dantetemplar/moscow-time-webapp:latest
```

### 3. Push the Image

```sh
docker push dantetemplar/moscow-time-webapp:latest
```

### 4. Pull the Image from Docker Hub

```sh
docker pull dantetemplar/moscow-time-webapp:latest
```

### 5. Run the Pulled Image

```sh
docker run -d -p 8000:8000 dantetemplar/moscow-time-webapp:latest
```

## Conclusion

This Dockerized **Moscow Time WebApp** follows security best practices by using a non-root base image and 
excluding unnecessary files. The result is a small, efficient, and secure container!

> **Tip**: Always prefer **minimal, non-root images** and use a **strict `.dockerignore`** to optimize your Docker
> builds. 🚀
> Yet it can be improved using docker compose, may be I will switch to it on next lab.
