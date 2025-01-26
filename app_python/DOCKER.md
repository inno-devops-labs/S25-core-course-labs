# Overview

## Best Practices Implemented

- The application runs under a non-root user
- Using `python:3.9-alpine` for a specific and lightweight base image
- Only the required files are copied to the image
- `.dockerignore` usage
- Organized instructions to minimize layers

## Docker Commands

- `docker build -t rwkals/app_python:latest .`
- `docker run -p 5000:5000 rwkals/app_python:latest`

## Distroless Image

- **Base image**. The Distroless runtime image `gcr.io/distroless/python3:nonroot` is used
- **Non-root user**. The `nonroot` tag ensures the application runs with non-root privileges
- **Smaller and more secure**.
  - The Distroless image removes unnecessary tools and utilities
  - Focuses on a minimal runtime environment

[sizes comparison](size_comparison.png)

### Why not significant difference in size?

The Distroless image is slightly smaller, but the difference is less significant for python because of optimized `alpine` base image.
