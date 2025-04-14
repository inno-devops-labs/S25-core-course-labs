# Docker Documentation

## Link
https://hub.docker.com/repository/docker/netpo4ki/go-web/general

`netpo4ki/go-web:latest`

## Dockerfile Best Practices

1. **Multi-Stage Builds**: Separates the build and runtime environments to reduce the final image size.
2. **Non-Root User**: Runs the application as a non-root user for improved security.
3. **Minimal Base Image**: Uses a lightweight base image for the runtime stage.
4. **Distroless Image**: Uses a Distroless base image for the runtime stage to further reduce size and attack surface.