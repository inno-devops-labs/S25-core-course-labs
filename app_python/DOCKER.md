## Docker Best Practices Applied

### Non-root user

- To improve container security, a non-root user (appuser) was created.
- Prevents attacks that escalate privilege.

### Environmental variables

- To stop Python from writing **_.pyc_** files, set **_PYTHONDONTWRITEBYTECODE=1_**.
- In order to guarantee constant logging, set **_PYTHONUNBUFFERED=1_**.

### Optimized layers of data

- To reduce picture size, dependencies were installed in a single layer using **_--no-cache-dir_**.

- Only relevant files were added to the container using **_COPY_**.

### Minimal Base Image

- Python 3.9 was used to create a tiny, safe base image using **_python:3.9-alpine3.15_**.

### .dockerignore file

- To increase build speed and efficiency, superfluous files were removed from the build context using **_.dockerignore_**.
