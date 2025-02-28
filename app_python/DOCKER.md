# Dockerfile: Best Practices

## Base Image Selection
Using a slim Python image (`python:3.9.7-slim`) is a good practice as it minimizes the image size.

## Non-Root User
A non-root user (`appuser`) is created and used, fulfilling the no-root-user requirement.

## Leverage Build Cache
Dependencies (`requirements.txt`) are copied and installed before the application code. This ensures the Docker build cache is leveraged if only the app code changes.

## Working Directory
`WORKDIR /app` is used to ensure the application runs in a consistent directory.

## Minimized Layers
Commands are grouped logically into layers for optimal use of caching.

## Avoiding Unnecessary Packages
The slim base image and `pip install --no-cache-dir` avoid bloat.

## Expose Ports and CMD
`EXPOSE 8000` and a clear `CMD` are used for running the application.
