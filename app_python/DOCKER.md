# Docker Best Practices Documentation

## Best Practices Employed

1. **Rootless Container**:
   - Created a non-root user to enhance security, ensuring the application doesn’t run as the root user.

2. **Specific Base Image**:
   - Used a slim and specific Python base image: `python:3.11-slim`. This ensures a smaller attack surface and smaller image size.

3. **Layer Sanity**:
   - Grouped instructions that change frequently (like `COPY` and `RUN pip install`) together to optimize Docker layer caching.

4. **.dockerignore**:
   - Added a `.dockerignore` file to exclude unnecessary files (e.g., `.git`, `__pycache__`) from the build context, reducing the image size.

5. **Minimal Dependencies**:
   - Used `--no-cache-dir` during `pip install` to avoid caching unnecessary files.

6. **Specific Port Exposure**:
   - Exposed only port `8080`, the one used by the Flask application.

7. **Application Directory**:
   - Used `WORKDIR /app` to keep the application organized and avoid running processes from the root directory.

8. **Small Image Layers**:
   - Only the necessary files (`app.py` and `requirements.txt`) were copied to the container.
