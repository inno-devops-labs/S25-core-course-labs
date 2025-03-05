## Best Practices

1. **Rootless Container**:
   - The application runs as a non-root user (`myuser`) to enhance security

2. **Layer Sanity**:
   - Dependencies are installed in a separate layer to optimize caching. However, the number of layers is reduced, to minimize size of container.
   - Only necessary files (`requirements.txt`, `app.py`, and `templates/index.html`) are specified in .dockerignore and copied into the image

3. **Precise Base Image**:
   - The base image `python:3.9-alpine3.15` is used for a lightweight and specific environment

4. **`.dockerignore`**:
   - Unnecessary files are excluded from the Docker build context using `.dockerignore`.
