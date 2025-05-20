# README.md

## Overview
This is a simple web application developed using FastAPI to display the current time in Moscow.

## Local Installation
1. Clone the repository.
2. Navigate to the `app_python` folder.
3. Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
4. Run the application:
```bash
uvicorn app:app --reload
```
5. Open your browser and go to http://127.0.0.1:8000/.

## Requirements:
* MSK Time timezone setup
* 2 PRs created
* README includes Overview
* Nice Markdown decoration
* Local installation details included
* Rootless container
* Use COPY but only specific files
* Layer sanity
* Use .dockerignore
* Use a precise version of your base image and language, example python:3-alpine3.15

## Docker Section
# Why Docker?
Docker provides a consistent environment for development, testing, and production. By containerizing the application, we ensure that it runs the same way regardless of the underlying system.

## How to Build the Docker Image
1. Ensure you are in the app_python directory.
2. Build the Docker image using the following command:
```bash
docker build -t fastapi-app-python .
```
## How to Pull the Docker Image from Docker Hub
If you have pushed the image to Docker Hub, you can pull it using:
```bash
docker pull grisharybolovlev/fastapi-app-python
```

## How to Run the Docker Container
1. Run the Docker container using the built or pulled image:
```bash
docker run -p 8000:8000 grisharybolovlev/fastapi-app-python
```
2. Open your browser and go to http://localhost:8000/.

## Docker Best Practices Employed
* Avoid Running as Root User : The Dockerfile creates a non-root user (appuser) and switches to it using the USER instruction. This enhances security by preventing the application from running with elevated privileges.
* Use a Precise Version of Base Image : We specified a precise version of the base image (python:3.9-alpine3.15). This ensures consistency across builds and avoids potential issues due to unexpected changes in the base image.
* Layer Optimization :
Install Dependencies First : We copied requirements.txt first and installed dependencies before copying the rest of the application code. This allows Docker to cache the dependency installation layer, reducing build time when only the application code changes.
Use Multi-stage Builds if Necessary : For more complex applications, multi-stage builds can further optimize the final image size.
* Use .dockerignore : We created a .dockerignore file to exclude unnecessary files and directories from being copied into the Docker image. This reduces the image size and improves build speed.
* Use COPY Instead of ADD : We used the COPY instruction instead of ADD. While both can copy files, COPY is more explicit and does not have the additional functionality of extracting archives, which aligns better with best practices for clarity and simplicity.
* Environment Variables : We set environment variables to control various aspects of the application behavior and build process:
PYTHONUNBUFFERED: Ensures logs are printed directly to stdout/stderr.
PYTHONDONTWRITEBYTECODE: Prevents Python from writing .pyc files.
PIP_NO_CACHE_DIR: Disables caching of downloaded packages.
PIP_DISABLE_PIP_VERSION_CHECK: Disables the pip version check.
* Minimal Base Image : We chose the alpine version of the Python image (python:3.9-alpine3.15) to minimize the image size while still providing the necessary tools and libraries.
* Clean Up After Installation : We cleaned up unnecessary files after installing dependencies using apk del to reduce the final image size.
* Expose Ports Explicitly : We explicitly exposed port 8000 using the EXPOSE instruction. This makes it clear which ports the container listens on and helps with documentation and troubleshooting.
* CMD Instruction : We used the CMD instruction to specify the default command to run the application. This allows users to override the command if needed without modifying the Dockerfile.