# Docker Best Practices

This document outlines the Docker best practices implemented in the `app_react` project. It explains the rationale behind each practice and how it is applied in the Dockerfile.

1. **Multi-Stage Builds**:
   - The Dockerfile uses a multi-stage build to separate the build, dependency installation, and runtime environments. This minimizes the final image size and enhances security by excluding unnecessary development dependencies from the production image.

2. **Non-Root User**:
   - A non-root user (`app`) is created and used to run the application, enhancing security by avoiding root privileges.

3. **Layer Sanity**:
   - Only necessary files (e.g., `src/`, `public/`, `package.json`, and configuration files) are copied into the image. This reduces the number of layers and keeps the image size small.

4. **Environment Variables**:
   - Environment variables like `PNPM_HOME` and `PATH` are set to optimize the behavior of `pnpm` and ensure the proper execution of commands in the containerized environment.

5. **Precise Base Image**:
   - A specific version of the base image (`node:23-alpine3.21`) with a SHA256 hash is used to ensure reproducibility and security. This avoids potential vulnerabilities or unexpected changes associated with using the `latest` tag.

6. **Caching Dependencies**:
   - The `--mount=type=cache,id=pnpm,target=/pnpm/store` flag is used during dependency installation to cache `pnpm` dependencies, speeding up subsequent builds.

7. **Linting and Formatting**:
   - Linting and formatting commands (`pnpm run lint`, `pnpm run format`, etc.) are executed as part of the build process to ensure code quality and consistency.

8. **`.dockerignore` File**:
   - A comprehensive `.dockerignore` file excludes unnecessary files and directories (e.g., `.git`, `node_modules`, `.env`, and build artifacts like `dist/`). This reduces the build context size and improves build performance.

9. **Explicit Port Exposure**:
   - Port `4173` is explicitly exposed to document the application's network requirements and simplify container orchestration.

10. **Prefer COPY Over ADD**:
    - The `COPY` instruction is used instead of `ADD` to transfer files into the image. `COPY` is preferred as it is more transparent and predictable, avoiding unexpected behavior associated with `ADD`.

11. **Prefer ENTRYPOINT and CMD**:
    - The `ENTRYPOINT` instruction is used to define the main command for the container (`pnpm run preview`). This makes the container behave like an executable, while `CMD` allows for easy overriding of arguments (e.g., host and port).

12. **Pin Base Image Versions**:
    - The base image version is explicitly pinned (`node:23-alpine3.21`) and includes a SHA256 hash for additional security and reproducibility. This ensures that the same base image is used consistently, avoiding vulnerabilities or breaking changes from updates.

13. **Minimal Final Image**:
    - Only the necessary build artifacts (e.g., `dist/`, `node_modules/`, and configuration files) are included in the final image. This reduces the attack surface and optimizes the image size.
