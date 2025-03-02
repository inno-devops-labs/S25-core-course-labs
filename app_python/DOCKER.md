# Docker Best Practices

## Introduction
This file describes the Docker best practices implemented in the `app_python` containerization process. Following these best practices ensures security, performance, and maintainability.

## Best Practices

### 1. **Rootless Container**
- The application does not run as the root user.
- A dedicated user `appuser` is created to enhance security.

```dockerfile
RUN useradd -m appuser
USER appuser
```

### 2. Use a Minimal and Specific Base Image

- I used `python:3.9-slim` instead of a generic `python:latest` to reduce attack surface and image size.

```dockerfile
FROM python:3.9-slim
```

### 3. Efficient Layer Management

- The `COPY` command is used in a structured manner to optimize caching.
- Dependencies are installed before copying the entire source code to avoid unnecessary rebuilds.

```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
```

### 4. Use .dockerignore

- A `.dockerignore` file is included to prevent unnecessary files from being copied, reducing image size and build time.

```text
__pycache__/
*.pyc
*.pyo
.env
.git
```

### 5. Expose Only Required Ports

- Only the necessary port `(5000)` is exposed to reduce attack surface.

```dockerfile
EXPOSE 5000
```

### 6. Define a Clear Entry Point

- The application is started using the `CMD` instruction to allow easy overriding.

```dockerfile
CMD ["python", "app.py"]
```

### 7. Use a Non-Blocking Command

- The `CMD` command runs in the foreground to keep the container active without unnecessary background processes.



## Conclusion

Following these best practices results in a secure, lightweight, and maintainable Docker container. Additional improvements can include multi-stage builds and the use of Distroless images for further optimization.
