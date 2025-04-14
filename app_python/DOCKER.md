# Docker image building

I've built a Docker image for Python application and successfully pushed it to Docker Hub.
The image can be seen [here](https://hub.docker.com/repository/docker/m0t9docker/pyapp/general).

## Best Practices applied

### Dockerfile linting

`hadolint` linter was used to readability and style in application Dockerfile.

### Minimal base image

I've used Python `alpine`-based image with minimal size to enhance building speed,
decrease final image size as well as number of vulnerabilities.

### Pinned base image version

I've pinned Python Alpine base image to `3.10` version.
This allows me always use this Python version.
Image will be safe in case of any bugs in newer Python releases.

### Non-root user

In Dockerfile I've created a usergroup with user with limited permissions
(in comparison with `root`) to decrease security risks.

### Optimized layering

The operations in the Dockerfile are sorted in ascending order of update rate
 (e.g., `requirements.txt` is less frequently updating file than `main.py` with source code).

 This allows effective reuse of the cache from the previous layers.

### Dockerignore

`.dockerignore` file allows ignoring files from the build context, increasing
efficiency of image build process.

## Distroless image

I've also built a Distroless image for the Python application.
The build process is described in `README.md`.

The resulting Distroless image size is almost 20MB heavier than original one.
I suppose this is because I was using slim Python image for dependencies downloading.
It was hard to craft the container based on Python alpine image (that is used in original one)
that easily started my FastAPI application.

Distroless based `pyapp` image on Docker hub can be seen [here](https://hub.docker.com/repository/docker/m0t9docker/pyapp_distro/general).

![Comparison of images sizes](image-size-comparison.png "Image sizes comparison")

May be this approach is not efficient for language without compiled binary.
