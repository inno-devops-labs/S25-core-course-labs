# Docker Best Practices

## Best Practices Implemented

1. **Rootless Container**:
   - Added a non-root `appuser` to run the application.
This practice enhances security by minimizing potential risks associated with
running processes as the root user.
2. **Precise Base Image**:
   - Used `python:3.9-slim` for a smaller image size.
3. **Layer Optimization**:
   - Combined related commands into fewer `RUN` statements to minimize the
   number of layers created, which reduces the image size and speeds up the build process.
   - Used `--no-cache-dir` for dependency installation. This reduces the final image size
   by excluding unnecessary cache files.
4. **.dockerignore**:
   - Excluded unnecessary files to reduce the image size.

## How to Build and Run

   ```bash
    docker build -t app_python .
    docker run -p 5000:5000 app_python
   ```

Alternatively, you can pull the Docker image from my [Dockerhub repository](https://hub.docker.com/r/vladis7love/app_python) using the following commands:

   ```bash
   docker login
   docker pull vladis7love/app_python:latest
   docker run -p 5000:5000 vladis7love/app_python
   ```
