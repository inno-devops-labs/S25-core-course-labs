# Docker image building

I've built a Docker image for Go application and successfully pushed it to Docker Hub.
The image can be seen [here](https://hub.docker.com/repository/docker/m0t9docker/goapp/general).

## Best Practices applied

### Dockerfile linting

`hadolint` linter was used to readability and style in application Dockerfile.

### Minimal base image

I've used Golang `alpine`-based image with minimal size to enhance building speed,
decrease final image size as well as number of vulnerabilities.

### Pinned base image version

I've pinned Golang Alpine base image to `1.23.5` version.
This allows me (for now) to use only latest stable version and not start using `1.24` when it will be released.

### Non-root user

In Dockerfile for the final image I've created a usergroup with user with
limited permissions (in comparison with `root`) to decrease security risks in the final image.

### Multi-stage build

With application on Go language I've crafted Dockerfile for multi-stage build.
Initially, builder image is created just to compile Go source files to resulting binary.
Resulting one is just an Alpine image with static content and binary file to be run.

### Optimized layering

The operations in the Dockerfile are sorted in ascending order of update rate.
For instance, files in `cmd` directory won't be updated as frequently as in `internal` one.
This allows effective reuse of the cache from the previous layers.

### Dockerignore

`.dockerignore` file allows ignoring files from the build context, increasing
efficiency of image build process.

## Distroless image

I've also built a Distroless image for the Go application.
The build process is described in `README.md`.

The resulting Distroless image size is almost 3 times less than original one.
This is because Distroless base image does not include shells, package managers and other OS features.
Some of them (e.g., shell) can be enabled with `debug` tag.

Distroless based `goapp` image on Docker hub can be seen [here](https://hub.docker.com/repository/docker/m0t9docker/goapp_distro/general).

![Comparison of images sizes](image-size-comparison.png "Image sizes comparison")

Due to the nature of compiled Go language, I needed only binary file and static ones in final image.
I didn't update code anyhow.
