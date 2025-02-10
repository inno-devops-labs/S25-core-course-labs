# Docker Best Practices

## Security

- The application **does not run as root**, ensuring better security.
- A dedicated **non-root user** (`appuser`) is created to execute the app.

## Efficiency

- **Using a minimal base image (`python:3.10-slim`)** to keep the image lightweight.
- **Avoiding unnecessary layers**: Commands are ordered logically to leverage Docker layer caching.
- **Using `.dockerignore`** to exclude unnecessary files (cache).

## Maintainability

- The `CMD` statement starts the FastAPI application using **Uvicorn**, keeping it lightweight.
- Dependencies are installed using `pip --no-cache-dir` to **avoid unnecessary bloat**.
- The FastAPI app files are **copied with ownership (`COPY --chown`)** to prevent permission issues.

---
