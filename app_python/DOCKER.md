# DOCKER.md

## Docker Best Practices

### Rootless Container
- Created a non-root user `appuser` to run the application.

### COPY Specific Files
- Used `COPY` to include only the necessary files for the application.

### Layer Sanity
- Organized the Dockerfile to minimize the number of layers and ensure efficient caching.

### .dockerignore
- Included a `.dockerignore` file to exclude unnecessary files from the Docker build context.

### Precise Base Image
- Used a specific version of the base image: `python:3.9-slim`.

## Steps to Build, Push, and Run the Docker Image

### Build the Docker Image
```sh
docker build -t your_dockerhub_username/app_python:latest .