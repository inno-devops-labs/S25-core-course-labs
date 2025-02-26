## Docker best practices applied

### Non-root user

- To improve container security, a non-root user (appuser) was created.
- Prevents attacks that escalate privilege.

### Environmental variables

- To stop Python from writing `.pyc` files, set `PYTHONDONTWRITEBYTECODE=1`.
- In order to guarantee constant logging, set `PYTHONUNBUFFERED=1`*.

### Optimized layers of data

- To reduce picture size, dependencies were installed in a single layer using `--no-cache-dir`.

- Only relevant files were added to the container using `COPY`.

### Minimal base image

- Python 3.9 was used to create a tiny, safe base image using `python:3.9-alpine3.15`.

### `.dockerignore` file

- To increase build speed and efficiency, superfluous files were removed from the build context using `.dockerignore`.
