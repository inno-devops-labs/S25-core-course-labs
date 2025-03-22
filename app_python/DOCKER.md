# Docker Best Practices

## Best Practices Implemented
1. **Rootless Container**: The application runs as a non-root user (`appuser`).
2. **Specific File Copying**: Only necessary files (`requirements.txt` and `app.py`) are copied into the image.
3. **Layer Sanity**: Each command in the Dockerfile creates a new layer, optimizing the image size.
4. **.dockerignore**: Unnecessary files are excluded from the Docker context, reducing build time and image size.
5. **Precise Base Image**: The base image is specified as `python:3.10-slim` to ensure consistency.

