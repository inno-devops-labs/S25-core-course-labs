     # Docker Best Practices

     ## Best Practices Implemented
     - **Non-root User**: The application runs as a non-root user to enhance security.
     - **Layer Sanity**: Each command in the Dockerfile creates a new layer, ensuring efficient caching.
     - **Specific File Copying**: Only necessary files are copied into the image.
     - **Precise Base Image Version**: Using python:3.10-alpine ensures consistency and security.
     - **No Cache for Dependencies**: Using --no-cache-dir minimizes image size by not caching pip packages.

     ## Additional Notes
     Following these best practices helps in maintaining smaller, more secure, and efficient Docker images.
     
