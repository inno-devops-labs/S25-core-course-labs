# Docker Best Practices

## 1. Rootless Container
- A non-root user (`webuser`) is created and used.

## 2. Minimization
- `pip install --no-cache-dir` is used to install dependencies without caching.

## 3. Using a Precise Base Image
- `python:3.12-alpine3.18` is used to ensure stability.

## 4. Using `.dockerignore`
- Unnecessary files (`__pycache__/`, `.git/`, `venv/`, etc.) are excluded to reduce image size.

## 5. Optimized Copying
- `COPY` is used twice:
  - First, only `requirements.txt` is copied to cache dependency installation. This ensures that dependencies are reinstalled only when requirements.txt changes.
  - Then, only the necessary app files are copied to prevent unnecessary dependency reinstalls when code changes.

## 6. Layer Sanity
- Used `COPY --chown` to set file ownership during the copy process, eliminating the need for separate RUN chown commands and reducing layers.
- Merged related commands into single RUN statements to minimize the total number of layers.
- Ordered instructions for caching.

## 7. Health Checks
- Implemented a `HEALTHCHECK` directive to periodically verify that the application is running correctly.

## 8. Environment Variables
- Set environment variables to optimize Python's behavior within the container.