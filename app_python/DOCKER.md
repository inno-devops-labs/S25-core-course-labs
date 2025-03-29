# 📦 Docker Best Practices for Moscow Time Web App

## 🔍 Best Practices Implemented

1️⃣ **Use a Minimal Base Image**
   - Using `python:3.10-alpine` instead of full Python images reduces size and attack surface.

2️⃣ **No Root User (Security)**
   - Created `appuser` as a non-root user to enhance security.

3️⃣ **Optimized Layer Caching**
   - Copy `requirements.txt` first before copying app files to optimize Docker build caching.

4️⃣ **Using a Virtual Environment**
   - Dependencies are installed in `venv/` instead of the global system.

5️⃣ **No Unnecessary Dependencies**
   - Used `--no-cache-dir` to reduce image bloat.

6️⃣ **Exposing Only Required Ports**
   - `EXPOSE 5000` ensures only necessary ports are open.

7️⃣ **CMD Uses Full Path**
   - Using `/app_python/venv/bin/python` explicitly ensures the app runs with the virtual environment.

## 📜 Summary
This ensures the Docker image is **lightweight, secure, and optimized** for performance.
