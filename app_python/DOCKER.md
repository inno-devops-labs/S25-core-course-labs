## Implemented Best practices

1. **Use a precise version of the base image and language**: Used a specific Python version `python:3.10-slim` with a minimal footprint to reduce attack surface and image size.
2. **Create a non-root user and get them permissions**: Added a dedicated user `user` and assigned ownership of necessary directories for security.
3. **Layer Sanity**: Organized instructions logically to minimize the number of layers, making the image more efficient and manageable.
4. **Copy only necessary files**: Only necessary files are copied initially to avoid unnecessary rebuilds.
5. **Use .dockerignore**: Excludes unnecessary files to reduce build context size.
6. **Optimize dependency installation**: Used `--no-cache-dir` with `pip install` to prevent caching unnecessary files, reducing image size.