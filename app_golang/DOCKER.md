# Dockerization of Golang Application

This document explains how the Golang application serving random programming quotes was containerized using Docker. It follows best practices to ensure a secure, lightweight, and efficient Docker image.

---


## 🚀 Docker Best Practices

### 1. **Using a Lightweight Base Image**
- Chose base image, which is a minimal, secure, and lightweight version of Python. It reduces the overall image size and attack surface.

### 2. **Rootless Containers**
- Created a non-root user (`appuser`) inside the container using:
  ```dockerfile
  RUN addgroup -S appgroup && adduser -S appuser -G appgroup
  USER appuser

### 3. **Working Directory**
- Using a working directory ensures that all operations within the container are organized in a specific folder. This enhances clarity and maintainability.

    ```dockerfile
    WORKDIR /app


### 4. **Excluding Unnecessary Files**
- Added a .dockerignore file to exclude irrelevant files like __pycache__, .vscode, and logs:
    ```dockerfile
    __pycache__/
    *.pyc
    *.pyo
    *.log
    venv/
    .vscode/

## 📦 How to Build the Docker Image

To build the Docker image locally, use the following command:

```bash
docker build -t azazaki/app_golang:1.0 .
```


## 📥 How to Pull the Docker Image
To pull the Docker image from Docker Hub, use the following command:
```bash
docker pull azazaki/golang:1.0

```

## 🚀 How to Run the Docker Image
Run the container locally with the following command:
```bash
docker run -p 8080:8080 azazaki/app_golang:1.0
```
Once the container is running, open your browser and navigate to:
```
http://localhost:8080
```

## 🔍 Differences Between Distroless and Previous Images

| Feature              | Traditional Image (Alpine)    | Distroless Image (`gcr.io/distroless/static:nonroot`) |
|----------------------|-----------------------------|-------------------------------------------------------|
| **Base Image**       | `alpine:3.18`               | `distroless/static:nonroot`                           |
| **Image Size**       | ~15MB                        | ~5MB                                                  |
| **Shell Availability** | Yes (`/bin/sh`)             | No shell available (`no /bin/sh`)                     |
| **Package Manager**  | Yes (`apk` available)       | No package manager                                    |
| **Security**         | Moderate                    | Highly secure (minimal attack surface)               |
| **Rootless by Default** | No (needs manual setup)    | Yes (runs as `nonroot` by default)                    |
| **Use Case**         | General-purpose, debugging  | Production-ready, lightweight, optimized runtime     |

### **Why the Differences Exist**
- **Smaller Image Size**: Distroless images **exclude unnecessary components** (shell, package manager, and debugging tools), reducing the image size.
- **Reduced Attack Surface**: By **removing shells and package managers**, Distroless makes it **harder for attackers** to exploit the container.
- **Rootless by Default**: Distroless **enforces security best practices** by running as a non-root user out of the box.
- **No Shell Access**: Unlike Alpine, **Distroless does not provide `/bin/sh`**, requiring the application to be fully self-contained.

### **When to Use Distroless**
- **Ideal for production deployments** where security and minimal size are priorities.
- **Not suitable for debugging** because it lacks a shell and package manager.

🚀 **Conclusion:**  
Using **Distroless** improves security, reduces image size, and removes unnecessary system utilities, making it the **best choice for production-ready Golang applications.**
