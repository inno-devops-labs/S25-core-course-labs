# Docker best practices:

1. Safety (using COPY (which is safer as it handles only local files, so it is more predictable) command instead of ADD)
2. Layer are minimized, so the size of the whole docker image is smaller.
3. Cached packets are removed.
4. A file .dockerignore is added which removes excessive files from the build.
5. Dockerfile is simplified by setting app as a WORKDIR.
