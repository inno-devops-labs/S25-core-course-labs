# Docker Best Practices for app_javascript

## 1. Non-root User

Running applications in Docker containers as a non-root user improves security by reducing the potential attack surface. In this Dockerfile, I've created a non-root user (`appuser`) and set it as the user that runs the Node.js app. This ensures that even if an attacker exploits the app, they won’t have full root access to the container.

```Dockerfile
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser
```

## 2. Efficient Layering

Docker images are built in layers, and each instruction in the Dockerfile creates a new layer. By copying the `package.json` and `package-lock.json` files first, it takes advantage of Docker's layer caching. This means that if these files don’t change, Docker will skip the `npm install` step and use the cached layer, speeding up the build process.

```Dockerfile
COPY package*.json ./
RUN npm install --production
```

## 3. Multi-Stage Builds

In the Dockerfile, I use a multi-stage build to separate the build environment from the final production image. In the first stage (`build`), I install dependencies and copy the application files. The second stage is based on a minimal `node:16-alpine` image and only copies over the necessary artifacts (i.e., the app files and installed dependencies) from the build stage. This reduces the size of the final image and eliminates unnecessary build tools.

```Dockerfile
FROM node:16-alpine as build
FROM node:16-alpine
COPY --from=build /app /app
```

## 4. Specific Version of Node Image

To ensure consistency and avoid unexpected updates, I use a specific version of the Node.js base image (`node:16-alpine`). This guarantees that the app will always run in the same environment, regardless of when the image is built.

```Dockerfile
FROM node:16-alpine
```

## 5. Use of `.dockerignore`

The `.dockerignore` file is used to exclude files that are not necessary for the application to run, such as `node_modules`, `.git` directory, and local development files like `.vscode`. This reduces the size of the image and keeps it clean from unnecessary files.

## **Distroless Image Version**

### **Differences Between Distroless and Previous Images**

1. **Size**:
   - **Distroless Image**: ~113 MB.
   - **Previous Node.js Image**: ~120 MB.
   - **Reason**: Distroless images contain only the app and runtime, without development tools, reducing the overall size.

2. **Security**:
   - **Distroless Image**: Fewer components, reducing the attack surface.
   - **Previous Node.js Image**: Includes shell and package managers, which increase potential vulnerabilities.

3. **Performance**:
   - **Distroless Image**: Slightly faster startup and lower memory usage.
   - **Previous Node.js Image**: Larger and includes more utilities, which can affect performance.

### **Why These Differences Exist**

- **Smaller Size**: Distroless images are optimized for production with only the essentials.
- **Reduced Attack Surface**: Fewer components to exploit.
- **Production-Readiness**: Only the necessary parts for running the app are included.

![Images compare](/app_javascript/images_compare.jpg)
