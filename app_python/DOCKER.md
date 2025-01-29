# Docker Best Practices for Flask App

## 1. Rootless Container
We ensure that the container runs as **non-root user**: `flask_app_user`\
This is critical for security purposes, as running as the root user can expose the container to unnecessary risks

## 2. Layer sanity
To minimize image size and optimize build time, we combine related commands, such as **installing dependencies** and **copying files**, into fewer layers\
This allows Docker to cache layers **efficiently, reducing the time needed for future builds**

## 3. Selective Copy
We selectively copy only the files that are necessary for the application to run:
* `requirements.txt`
* `web.py`
* `templates/`
* `static/`

This reduces the final image size and prevents unnecessary files from being included in the Docker image

## 4. Precise Version of Base Image
We use a specific version of the Python base image (`python:3.9-alpine3.15`) to ensure that the image is consistent and not affected by any future breaking changes in newer versions of the base image

## 5. `.dockerignore`-file
We use a `.dockerignore` file to exclude unnecessary files from the Docker image, such as local python bytecode files, git-related files etc.

## 6. Env Variables
We set the `FLASK_APP` and `FLASK_ENV` env variables to ensure the application runs in production mode, **improving performance and security**
