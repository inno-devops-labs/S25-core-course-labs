# Docker Best Practices 

1. using specific files in COPY instruction: to minimize the image size and avoid unnecessary rebuilds, I am copying only files required to start the application (`templates` folder, `app.py`, and `requirements.txt`) instead of whole directory (`COPY . .`).
1. non-root user: application is running under the `worker` user.
1. using .dockerignore: by using a .dockerignore file, I prevent unnecessary files from being sent to the Docker daemon, this helps to speed up the build process and reduce the cache size.
1. precise base image version: due to specific version (python:3-alpine3.15) of the base image, builds become reproducible
