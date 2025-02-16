# Docker Best Practices

## Best Practices Implemented
1. **Rootless Container**: The application runs as a non-root user.
2. **Specific File Copying**: Only necessary files are copied into the image.
3. **Layer Sanity**: Each command in the Dockerfile creates a new layer, optimizing the image size.
4. **.dockerignore**: Unnecessary files are excluded from the Docker context, reducing build time and image size.
5. **Precise Base Image**: The base image is specified as `node:18-alpine` to ensure consistency.
6. **Multi-Stage Builds**: The Dockerfile uses multi-stage builds to separate the build environment from the production environment, reducing the final image size. 