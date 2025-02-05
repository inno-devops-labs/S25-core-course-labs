# Docker Best Practices for moscow-time-app

## Best Practices Implemented
### Use a Minimal Base Image
-Using python:3-alpine3.15 instead of python:3 to reduce image size and attack surface.
-Alpine-based images are significantly smaller and contain fewer vulnerabilities.

### Run as a Non-Root User
Running applications as root inside containers is a security risk.
A dedicated user appuser is created to avoid running as root.

#### Check if the container runs as a non-root user:

docker run --rm -it utkanosss/moscow-time-app whoami
If it prints appuser, it's correctly configured.

### Use COPY Instead of ADD
COPY is used instead of ADD to avoid unnecessary complexity.
ADD can extract archives, which may lead to unintended side effects.

### Optimize Layer Caching
Installing dependencies before copying application files allows Docker to cache dependencies.

### Use a .dockerignore File
Prevents unnecessary files from being added to the image, reducing build size.

### Expose Only Necessary Ports
The app runs on port 5000, so we explicitly expose it.

## Summary
- Minimal image size
- Non-root user for security
- Efficient caching for faster builds
- .dockerignore to exclude unnecessary files
- Multi-stage builds for optimization

