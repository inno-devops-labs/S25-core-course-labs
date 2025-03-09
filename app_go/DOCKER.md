# Docker Best Practices

This document outlines the Docker best practices implemented in the `app_go` project. It explains the rationale behind each practice and how it is applied in the Dockerfile.

---

## 1. Multi-Stage Builds

- The Dockerfile uses a **multi-stage build** to separate the build environment from the runtime environment.
- This approach **reduces the final image size** by removing unnecessary dependencies required only during the build stage.
- The `builder` stage compiles the Go binary, while the `final` stage runs the application with minimal dependencies.

---

## 2. Non-Root User for Security

- A **non-root user (`app`)** is created and used to run the application, enhancing security by avoiding root privileges.
- The `RUN addgroup -g 1001 app && adduser -u 1001 -G app -D app` command ensures the application does not run as root.
- The `USER app` directive is used to enforce non-root execution.

---

## 3. Efficient Layering & File Copying

- Only essential files (`app.go`, `go.mod`, and `templates/`) are copied to minimize the image size.
- `COPY --chown=app:app` is used to maintain correct ownership of files and prevent permission issues.
- In the `final` stage, only the **compiled binary** and **templates** are copied, reducing unnecessary bloat.

---

## 4. Explicit Base Image Versioning

- The base image is pinned to a **specific version** (`golang:1.23-alpine3.21`) and a **SHA256 hash** for security and reproducibility.
- This prevents unexpected changes from upstream images that may introduce vulnerabilities or break dependencies.

---

## 5. Optimized Dependency Management

- `go mod download` is executed before the build step to cache dependencies and speed up builds.
- This ensures dependencies are fetched efficiently without redundant downloads in subsequent builds.

---

## 6. Minimal Final Image

- The final image **does not include unnecessary build tools**, reducing attack surfaces and keeping it lightweight.
- Instead of using `builder` as the final stage, a minimal `alpine:3.21` base image could be used to further reduce size.

---

## 7. Proper Signal Handling & Entrypoint

- `ENTRYPOINT ["./app"]` ensures the application starts correctly.
- This allows for **better signal handling**, ensuring proper shutdown when stopping the container (e.g., with `CTRL+C`).

---

## 8. Explicit Port Exposure

- `EXPOSE 3000` is included to document the network interface the application listens on.
- While it does not actually expose the port, it serves as metadata for users and tools like Docker Compose.

---

## 9. Using COPY Over ADD

- The `COPY` instruction is preferred over `ADD` since it is more predictable and does not unintentionally extract archives or fetch remote URLs.

---

## 10. Dockerignore for Optimized Context Size

- A `.dockerignore` file should be used to exclude unnecessary files (e.g., `.git`, `node_modules`, `*.log`) to improve build performance and reduce the image size.

---

Got it! Here’s an updated version that’s more in line with your existing structure:

---

Sure! Here's the updated version of the section with a placeholder for the image:

---

## 11. Distroless Image Comparison

We also experimented with **Distroless images**, which are minimal images containing only the application and its runtime dependencies, with no package manager or shell. The main differences between the Distroless images and the previous Docker images are as follows:

- **Smaller Image Size:**
  - Distroless images are much smaller because they only include the essential components needed to run the application. This significantly reduces the size of the image.
  - Example sizes:
    - `ali12hamdan/app_go-prod-1.0.0`: **347MB**

- **Reduced Attack Surface:**
  - By removing unnecessary packages like shell utilities and package managers, Distroless images have a smaller attack surface, making them more secure.

- **Performance Benefits:**
  - Smaller image sizes also translate to **faster builds** and **quicker deployments**, which can be a major advantage in environments with rapid scaling or frequent updates.

---
