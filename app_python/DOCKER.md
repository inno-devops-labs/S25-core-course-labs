# Docker Best Practices

## Non-Root User
- A non-root user (`appuser`) is created and used to run the application to enhance security.

## Specific File Copying
- Only specific files (`requirements.txt`, `app.py`, and `templates` directory) are copied to the Docker image to minimize the image size and improve security.

## Layer Sanity
- Dependencies are installed in a separate layer to leverage Docker's caching mechanism.

## Precise Base Image
- A precise version of the base image (`python:3.9-alpine3.15`) is used to ensure consistency and reproducibility.

## .dockerignore
- A `.dockerignore` file is used to exclude unnecessary files and directories from the Docker build context, reducing the image size and improving build performance.
