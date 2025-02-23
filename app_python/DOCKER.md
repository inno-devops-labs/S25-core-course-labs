# Docker Best Practices

## Enhancing the Docker Image

### Security Improvements
- **Non-root user**: The container runs as a non-root user (`myuser`), improving security.
- **Minimal base image**: Using `python:3.12-slim` reduces unnecessary components and potential vulnerabilities.

### Performance Enhancements
- **Multi-stage builds**: Dependencies are installed in a separate `builder` stage, reducing the final image size.
- **No cache for dependencies**: Using `--no-cache-dir` prevents storing unnecessary package installation files.
- **Use .dockerignore** to exclude unnecessary files

I also used hadolint Dockerfile for quality assurance.