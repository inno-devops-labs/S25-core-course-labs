# DOCKER.md

## Docker Best Practices Implemented

1. **No Roots Here**
   - The Dockerfile sets up a `nonrootuser` to avoid running as root.

2. **Lightweight Base**
   - The `python:3.10-slim-bullseye` is used for optimization and security.

3. **Layer Sanity**
   - Layers are optimized:
     - Installing dependencies (`pip install`) is separated to allow caching.
     - Code is copied after dependencies to avoid rebuilding if code was changed.

4. **Environment Variables**
   - Added `PYTHONDONTWRITEBYTECODE=1` and `PYTHONUNBUFFERED=1` for improved performance.

5. **Using COPY**
   - Only specific files (`app.py` and `requirements.txt`) are copied to avoid overhead.

6. **Dockerignore File**
   - Excludes unnecessary files like `__pycache__`, `.env`, `.git`, and `.DS_Store`.

## Additional Notes
- Using `--no-cache-dir` with `pip install` prevents caching and reduces image size.
- The container exposes only the required port (5000).
