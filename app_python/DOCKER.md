# Docker Best Practices for app_python

This document outlines the best practices employed within our Dockerfile for the `app_python` application. Following these practices ensures that our containerized application is efficient, secure, and easy to maintain.

## 1. Use a Minimal Base Image

I use the `python:3.10-slim` base image which is smaller compared to the full `python:3.10` image. This reduces the attack surface and improves build times.

```Dockerfile
FROM python:3.10-slim
```
### 2. Create a Non-Root User
Running applications as a non-root user enhances security by limiting potential damage from vulnerabilities. I create a user named builder.
```Dockerfile
RUN useradd --create-home builder
WORKDIR /home/builder
USER builder
```

### 3. Specify WORKDIR
Using WORKDIR sets the working directory inside the container, making subsequent commands relative to this path and ensuring consistency.
```Dockerfile
WORKDIR /home/builder
```

### 4. Copy Requirements First
Copying requirements.txt first allows Docker to leverage layer caching effectively. If only the code changes but not the dependencies, Docker will reuse the cached layer.
```Dockerfile
COPY requirements.txt .
```

### 5. Install Dependencies with No Cache
Using --no-cache-dir during pip install avoids storing unnecessary files in the Docker image, reducing its size.
```Dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

### 6. Copy Application Code
Copy the application code after installing dependencies to ensure any changes to the code do not invalidate the dependency installation layer.
```Dockerfile
COPY main.py .
COPY ./templates ./templates
```

### 7. Expose Necessary Ports
Explicitly expose the port used by the application (8000) so it’s clear what ports need to be accessible externally.
```Dockerfile
EXPOSE 8000
```

### 8. Use CMD Correctly
The CMD instruction specifies the default command to run when the container starts. I use an array format to avoid shell interpretation issues.
```Dockerfile
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```