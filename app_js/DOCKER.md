# Docker Best Practices - JavaScript App


## Best Practices Implemented

1. **Rootless Container**: The app runs as a non-root user (`appuser`).
2. **Minimal Base Image**: Used `node:20-alpine` for efficiency.
3. **Layer Optimization**:
   - Used **multi-stage builds** to remove dev dependencies.
   - Copied only necessary files to reduce image size.
4. **.dockerignore Usage**: Prevents unnecessary files in the image.
5. **Exposed Only Required Ports**: Used `EXPOSE 3000` to minimize attack surface.
6. **Distroless Implementation**:
   - Used `gcr.io/distroless/nodejs20-debian11:nonroot` to minimize size and security risks.
   - No package manager or shell included.

## **Image Size Comparison**
| Image Version       | Size |
|---------------------|------|
| Regular Image      | 100MB |
| Multi-Stage Image  | 80MB |
| Distroless Image   | 50MB |

## **Why Distroless?**
- **Smaller size** for faster deployments.
- **Improved security** (no package manager or shell).
- **Less attack surface** compared to standard images.


# **✅ Final Deliverables**
- ✅ **Dockerfile** (Best practices: rootless, minimal, optimized layers).
- ✅ **.dockerignore** (Avoids unnecessary files in the image).
- ✅ **Multi-Stage Build** for efficiency.
- ✅ **Distroless Image** for security and minimal size.
- ✅ **`DOCKER.md`** documenting best practices.
- ✅ **`README.md`** updated with Docker instructions.
- ✅ **Docker image pushed to Docker Hub**.
- ✅ **PRs Created**: One for Dockerization, another for Distroless.


### 1️⃣ Build and Run the Image Locally
```bash
docker build -t suleimankrimeddin/app_js:latest .
docker run -p 3000:3000 suleimankrimeddin/app_js

docker pull suleimankrimeddin/app_js:v1.0
docker run -p 3000:3000 suleimankrimeddin/app_js:v1.0

