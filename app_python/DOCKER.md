## Docker Best Practices Used

1. **Rootless Container**:
   - Created a non-root user (`appuser`).
   - Changed ownership of files and switched to this user.

2. **COPY Instead of ADD**:
   - Used `COPY` command for including only necessary files.
   - Added a `.dockerignore` file to exclude unnecessary files.

3. **Layer Sanity**:
   - Combined related commands to reduce the number of layers.
   - Used `--no-cache-dir` with `pip install` to avoid temporary caches.

4. **Precise Base Image**:
   - Selected a lightweight and specific base image (`python:3.9-alpine3.17`).

5. **Minimal Image Size**:
   - Leveraged Alpine Linux for a smaller image size.

## Additional Notes
- The Dockerfile adheres to Docker best practices for security, performance, and maintainability.