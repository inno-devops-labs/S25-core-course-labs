# Docker Best Practices Applied

1. **Non-root User**:
    - Created a non-root user (`appuser`) to enhance container security.
    - Prevents privilege escalation attacks.

2. **Optimized Layers**:
    - Installed dependencies in a single layer with `--no-cache-dir` to minimize image size.
    - Used `COPY` to add only necessary files to the container.

3. **Minimal Base Image**:
    - Used `python:3.9-alpine3.15` for a small, secure base image with Python 3.9.

4. **Environment Variables**:
    - Set `PYTHONDONTWRITEBYTECODE=1` to prevent Python from writing `.pyc` files.
    - Set `PYTHONUNBUFFERED=1` to ensure consistent logging.

5. **Expose Ports**:
    - Clearly exposed the port (`5000`) used by the application.

6. **.dockerignore**:
    - Used `.dockerignore` to exclude unnecessary files from the build context, improving build speed and efficiency.
