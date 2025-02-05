# Docker Best Practices

This document describes the best practices applied in the Dockerfile for application containerization.

## Best practices

1. **Using an unprivileged user** 
 To minimize security risks the application is run as the `appuser` user, not as root.

2. **Using `.dockerignore`** 
 Unnecessary files are ignored to reduce the size of the build context.

3. **Using `--no-cache-dir` when installing dependencies** 
 This reduces the size of the final image.

4. **Copying only necessary files** 
 The image is copied only `requirements.txt` and `main.py` to minimize its size.