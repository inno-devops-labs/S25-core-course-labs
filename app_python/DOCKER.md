# Docker Containerization of Flask Moscow Time App

## Best Practices Implemented

### 1. Precise Base Image with Digest
Used a **minimal and specific base image** with pinned version and digest:

```Dockerfile
FROM python:3.13.1-alpine3.21@sha256:<digest>
```

This ensures immutability and reproducibility.

---

### 2. Multi-Stage Builds
Used multi-stage builds to separate dependency installation from the runtime environment, reducing final image size and surface area:

```Dockerfile
# Stage 1: builder (installs deps into venv)
# Stage 2: final (copies in just the venv and app)
```

---

### 3. Layer Caching & Sanity
Used pip cache mount to reduce rebuild time:

```Dockerfile
RUN --mount=type=cache,target=/root/.cache/pip pip install ...
```

Only specific files are copied in each stage, minimizing invalidation of layers.

---

### 4. Virtual Environment Usage
Installed dependencies into a virtual environment, and set environment variables to prioritize it:

```Dockerfile
ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"
```

---

### 5. Non-root Execution 
Created and used a non-root user `app`, following the principle of least privilege:

```Dockerfile
RUN adduser -u 1001 -G app -D app
USER app
```


---

### 6. Copy Specific Files Only
Avoided using `COPY . .` and instead only copied in what’s needed:

```Dockerfile
COPY --chown=app:app app.py ./app.py
COPY --chown=app:app templates ./templates
```

This ensures better layer control and smaller image size.

---

### 7. ENTRYPOINT for Flask
Used `ENTRYPOINT` with Flask run command, ensuring clean container start:

```Dockerfile
ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=5000"]
```

---

### 8. Container Port Exposed
Only port 5000 is exposed:

```Dockerfile
EXPOSE 5000
```

---

### 9. .dockerignore Implemented
A `.dockerignore` file was added to reduce build context size and ensure a cleaner image.
This helps prevent unnecessary files from being sent to the Docker daemon and keeps image layers clean and small.

---

## Build, Run & Push Steps

### Build the Docker Image

```bash
docker build -t alimansour000/moscow-time-app:latest .
```

### Run the Container

```bash
docker run -p 5000:5000 alimansour000/moscow-time-app:latest
```

### Push to Docker Hub

```bash
docker push alimansour000/moscow-time-app:latest
```

---

## Summary

This Docker setup implements security (non-root), small size (Alpine, multi-stage), reproducibility (pinned image digest), and hygiene (specific file copying, .dockerignore).