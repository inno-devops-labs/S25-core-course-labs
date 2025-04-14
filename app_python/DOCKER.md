# Containerization details

This document explains the security and optimization best practices used while dockerizing application.

List of best-practices applied:

1. Non-Root Execution
2. Python Environment Optimization
3. Dependency Management
4. Image Size Optimization
5. Log Management
6. Port Configuration
7. Build Efficiency

## Base Image Strategy

Out dockerfile uses minimal musl libc-based distribution (≈5MB base image). Explicit `3-alpine3.15` tag ensures deterministic builds. We use official Docker-maintained Python image with security updates.

## Non-Root Execution

We follow principle of Least Privilege - so no root privileges in runtime. This reduces internal attack surfaces and makes it harder for adversary to escape to host or exploit a kernel vulnerability.Also we use explicit user/group IDs prevent accidental privilege reassignment.

## Python Environment Optimization

We use several environment-related optimization for our application:

- `PYTHONUNBUFFERED`: Ensures immediate log output
- `PYTHONDONTWRITEBYTECODE`: Precrets .pyc file creation (reduces attack surface)

## Dependency Management

Temporary build dependencies removed post-install. The flag `--no-cache-dir` for pip avoids ~200MB cache bloat. Cleanup in same RUN instruction minimizes image layers

## Image Size Optimization

We applied several techniques to optimize image size:

1. Multi-Stage Build Patterns (implicit in Alpine)
2. Dependency Cleanup:

   ```dockerfile
   apk del .build-deps
   ```

3. Combined RUN instructions (also known as "Layer Squashing")
4. Running package manager without cache

Final image typically much lower (in this application currenlty container size is just 59MB) then 350MB+ for standard Python images

## Log Management

The logging is redirected to standart I/O channels, so it integrates with Docker logging drivers. It still preserves access/error streams.

## Port Configuration

To improve flexibility and allow overrides with `docker run -e PORT=8000`, the port to be run on was made as an environment variable.

## Build Efficiency

Changes to app code don't trigger dependency reinstalls, because of the order of layers we use.

