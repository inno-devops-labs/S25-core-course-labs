# Docker Best Practices

This application follows the best Docker practices:
1. Only `requirements.txt ` the file is copied first to reduce build time and image size
2. Using `--no-cache-dir' reduces the final image size
3. The `python:3-alpine` base image
