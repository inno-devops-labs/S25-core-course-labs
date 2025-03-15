# Docker Best Practices

## Best Practices Used in Dockerfile

1. **Rootless Containers**:
   * Added a non-root user `appuser` to enhance container security.

2. **Layer Optimization**:
   * Leveraged Docker's caching mechanism by copying `requirements.txt` first and installing dependencies before copying other files.

3. **Precise Base Image**:
   * Used a specific version of the base image (`python:3.10-slim-bullseye`) for reproducibility and smaller size.

4. **Selective COPY**:
   * Only necessary files are included in the image to keep it clean and minimal.

5. **Environment Variables**:
   * Set `PYTHONDONTWRITEBYTECODE` and `PYTHONUNBUFFERED` to optimize Python behavior in containers.

6. **.dockerignore**:
   * Excluded unnecessary files from the build context to reduce image size.

## Additional Notes

* This Dockerfile adheres to Docker best practices and has been tested for functionality and efficiency.
* Images are pushed to a public Docker Hub account for easy retrieval.
