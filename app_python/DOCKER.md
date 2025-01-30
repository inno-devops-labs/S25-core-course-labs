# **Best Practices**

## 1. Rootless Container
- Usage of non-root user (`dew1769`)
- This improves security and prevents privilege escalation

## 2. Minimal Base Image
- Used `python:3.11-slim` for a stability and to minimize troubles

## 3. Optimized Layers
- Used `COPY --chown=dew1769:dew1769 requirements.txt /app/` to install dependencies first
- As a result we do not need to rebuild the image when app code changes

## 4. Usage of `.dockerignore`
- Prevents unnecessary files (`venv/`, `__pycache__/`, `.git`) from being copied

## 5. Efficient `pip install`
- Used `--no-cache-dir` to reduce the image size

## 6. Expose Ports
- `EXPOSE 5000` to define default port for our application