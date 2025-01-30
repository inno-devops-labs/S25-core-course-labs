# Docker Documentation

This document explains the **Docker best practices** employed within the Dockerfile.

## Best Practices

1. **Rootless Container**  
   - A new user created (`appuser`) to ensure the container does **not** run as `root`.

2. **Specific Base Image**  
   - Precise version of python is used (`python:3.9-slim`) instead of `python:latest` to ensure consistency.  

3. **Layer Minimization**  
   - Dependencies installed separately (`pip install -r requirements.txt`) before copying the application files. This way, if dependencies don’t change, Docker can cache that layer.

4. **Copy Only Necessary Files**  
   - Using `COPY requirements.txt .` and `COPY app.py .`, we avoid copying extra files into the image.

5. **.dockerignore Usage**  
   - A clean `.dockerignore` file to exclude environment files to reduce the image size.
