# Docker Documentation for Python Web App

## 1. Docker Best Practices Implemented
1. **Pinned Base Image**: Using `python:3.10.13-alpine3.16` ensures consistent builds.
2. **Non-Root User**: Created `python_user` to avoid running as root in the container.
3. **Minimal Installation**:
   - Used `--no-cache-dir` to reduce leftover artifacts.
   - Only copied `requirements.txt` and `main.py` to keep the final image small.
4. **.dockerignore**: Excludes unneeded files/folders like `venv`, `.git`, etc.
5. **Layer Usage**:
   - Pinned packages are installed in one layer.
   - Code is copied in another layer.
   - This means changes in code won't always invalidate the dependencies layer.

## 2. Dockerfile Linting
- Recommended to use [Hadolint](https://github.com/hadolint/hadolint) or similar linting tools to catch potential Dockerfile issues.

## 3. Image Verification
- **Local Run**:
  ```bash
  docker build -t sedoxxx/python-webapp:latest .
  docker run -d -p 5000:5000 sedoxxx/python-webapp:latest
