# Docker Best Practices Implemented

This document outlines the Docker best practices employed in the creation of the Dockerfile for this application.

* **Non-root User:** The container runs as a non-root user (`appuser:appgroup`) for enhanced security. This prevents potential privilege escalation attacks.
* **Reduced Image Size:**  The `python:3.9-alpine3.17` base image is used, which is a minimal and lightweight distribution, resulting in a smaller final image size.  `apk add --no-cache` avoids caching package downloads.
* **Layer Caching:** The `COPY requirements.txt .` instruction is placed before the `RUN pip install` instruction. This allows Docker to cache the dependency installation layer, speeding up subsequent builds if only the application code changes.
* **.dockerignore File:** A `.dockerignore` file is used to exclude unnecessary files and directories from the image, further reducing image size and build time.
* **Specific COPY Instructions:**  Only essential files (`requirements.txt` and `app.py`) are copied into the image, avoiding unnecessary bloat.
* **Explicit Version Pinning:** `python:3.9-alpine3.17` specifies a precise base image version to ensure reproducible builds.
