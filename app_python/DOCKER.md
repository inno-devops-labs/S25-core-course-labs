## Docker Best Practices Implemented

### 1. **Using a Precise Base Image**
- The Dockerfile uses `python:3.9-alpine` instead of a general `python` tag to ensure **stability and smaller image size**.

### 2. **Rootless Container**
- The application runs as a **non-root user** to improve security.

### 3. **Efficient Layering**
- Only necessary files are copied using `COPY` instead of `ADD`.
- The `.dockerignore` file ensures unnecessary files (e.g., `venv`, `__pycache__`) are **not included** in the image.

### 4. **Minimal Dependencies**
- The `requirements.txt` is used to **install only required dependencies**, keeping the image lightweight.

### 5. **Exposing Required Ports**
- The Flask application runs on **port 5000**, which is explicitly exposed in the Dockerfile.

### 6. **CMD Usage**
- `CMD` is used instead of `ENTRYPOINT` for flexibility when overriding the default command.