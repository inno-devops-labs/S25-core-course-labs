# DOCKER.md

## Docker Best Practices Implemented


### 1. **No Root User (Security)**
Security is a critical aspect of containerized applications. Running the container as the root user poses significant security risks. To mitigate this, we:
- Create a non-root user (`person`) inside the container.
- Set the correct ownership and permissions for the application directory.
- Switch to the non-root user before running the application.


### 2. **Minimal and Efficient Base Image**
We use the `python:3.12-alpine` base image, which is significantly smaller than Debian-based alternatives. This reduces the attack surface and speeds up deployment and image transfer.


### 3. **Optimized Dependency Installation**
To improve Docker build efficiency and caching, we:
- Copy `requirements.txt` first before copying the entire application code. This allows Docker to cache the dependency installation step unless `requirements.txt` changes.
- Use `--no-cache-dir` when installing Python dependencies to prevent unnecessary storage usage.


### 4. **Setting Environment Variables**
We set `PYTHONUNBUFFERED=1` to ensure that Python output is immediately flushed, which is important for logging inside containers.


### 5. **Explicit Work Directory**
We define `/app` as the working directory and ensure all operations occur inside it, improving maintainability and clarity.


### 6. **Explicit Port Exposure**
The application listens on port 8080, so we explicitly expose it in the Dockerfile for better networking clarity.


### 7. **Consistent Application Start Command**
Using `CMD` ensures the application starts reliably with the correct command. This approach allows the default command to be overridden if needed.


