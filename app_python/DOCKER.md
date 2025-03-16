
# Best Practices

1. **Non-Root User**: The Dockerfile creates and switches to a non-root user (`appuser`) to enhance security.
2. **Specific Base Image Version**: The base image `python:3.10-alpine3.15` is used for reproducibility.
3. **Minimal File Copying**: Only necessary files (`requirements.txt`, `app.py`, and `templates/`) are copied into the image.
4. **Layer Optimization**: Dependencies are installed in a single `RUN` command to reduce the number of layers.
5. **No Cache for Pip**: The `--no-cache-dir` flag is used to reduce the image size.
6. **Explicit Port Exposure**: The `EXPOSE 5000` directive makes it clear which port the application uses.
7. **Use of `.dockerignore`**: Unnecessary files are excluded from the build context using a `.dockerignore` file.
8. **Rootless Container**: The container runs as a non-root user for improved security.
