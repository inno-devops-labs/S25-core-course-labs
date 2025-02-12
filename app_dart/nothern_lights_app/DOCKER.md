# Docker Best Practices for Flutter App

## 1. Rootless container
The container runs with a non-root user (`flutter`) by creating this user and switching to this user in the final image.

## 2. Layer sanity
The Dockerfile utilizes Docker's cache mechanism efficiently by first copying the `pubspec.yaml` and `pubspec.lock` files, allowing Docker to cache dependencies.

## 3. COPY
Instead of copying all files at once, we copy only the necessary files at the beginning (`pubspec.yaml`, `pubspec.lock`), allowing us to take advantage of Docker's layer caching for dependency installation.

## 4. Multi-stage build
A multi-stage build applied to separate the build process from the runtime environment. This ensures that the final image is smaller and does not contain unnecessary development dependencies. The Flutter build stage is discarded in favor of a minimal `nginx` server that serves the built web assets.
  
  