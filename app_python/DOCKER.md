# Docker Best Practices

## Best Practices Implemented

1. **Use a Specific Base Image Version**:
   - The base image `python:alpine` is used.

2. **Non-Root User**:
   - A non-root user (`appuser`) and group (`appgroup`) are created to run the application, enhancing security.

3. **Minimize Layers**:
   - Files are copied in a single layer, and dependencies are installed in one `RUN` command to reduce the number of layers.

4. **Use `.dockerignore`**:
   - Unnecessary files are excluded from the Docker build context using `.dockerignore`.

5. **Environment Variables**:
   - `PYTHONUNBUFFERED=1` is set to ensure Python outputs are sent directly to the terminal.

6. **COPY Only Necessary Files**:
   - Only the required files (`requirements.txt`, `app.py`, `templates/`, and `static/`) are copied into the image.

7. **No Cache for Dependencies**:
   - The `--no-cache-dir` flag is used with `pip install` to avoid caching and reduce image size.

8. **Explicit Port Exposure**:
   - The application port (`8000`) is explicitly exposed for clarity.

9. **Use of Alpine Image**:
   - The Alpine-based image is lightweight, reducing the final image size.

## How to Build and Run the Docker Image

1. **Docker setup**:

```bash
docker build -t jlfkajlkifj/python-web-app:latest .
docker run -d -p 8000:8000 jlfkajlkifj/python-web-app:latest
docker push jlfkajlkifj/python-web-app:latest
docker pull jlfkajlkifj/python-web-app:latest
docker run -d -p 8000:8000 jlfkajlkifj/python-web-app:latest
```

