# Docker Best Practices

1. **Use a Minimal Base Image:**

    The python:3.9-alpine3.15 base image is lightweight and secure, reducing the attack surface and image size.

2. **Run as a Non-Root User:**

    The application runs as a non-root user (appuser) inside the container to improve security.

3. **Optimize Docker Layers:**

    Dependencies are installed in a separate layer to leverage Docker's caching mechanism and speed up builds.

4. **Expose Only Necessary Ports:**

    Exposed only port 8000 (the port used by the FastAPI application). Not `network` mode.

5. **Use .dockerignore:**

    Unnecessary files are excluded from the Docker build context using a .dockerignore file, reducing the build context size.

6. **Set Environment Variables:**

    `PYTHONUNBUFFERED=1` is set to ensure Python outputs are sent directly to the terminal (useful for logging that may occure in next versions).

7. **Use COPY Instead of ADD:**

    The COPY instruction is used to copy only necessary files into the image, avoiding unintended side effects.

8. **Expose Only Necessary Ports:**

    Only port 8000 (used by FastAPI) is exposed in the Dockerfile.

9. **Push to Docker Hub:**

    Pushed the Docker image to Docker Hub for easy sharing and deployment.
