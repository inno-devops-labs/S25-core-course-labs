# Docker Best Practices Implemented

## Multi-stage build with right base images

I used a multi-stage build to compile the Go application.
First stage is used to build the application and
the second stage is used to run the application.
First stage uses `golang:1.23.5-alpine3.21` as the base image.
Second stage uses `alpine:3.21.2` as the base image.
Alpine images are used to keep the image size small.

## Usage of `.dockerignore`

I used a `.dockerignore` file to exclude unnecessary files and directories
from the build context, improving the build performance.

## Creation of ephemeral container

Container needs no configuration to run. It is ready to run as soon as it is created.

## Installation of only necessary packages

Application uses only the standard library of Go, so no additional packages are installed.

## Right order of instructions

The instructions are ordered in such a way that
the layers that change the least are placed at the top.
This way, the cache can be used more effectively.

## Pin base image version

I pinned the version of the base image to the following specific version:

```
golang:1.23.5-alpine3.21@sha256:47d337594bd9e667d35514b241569f95fb6d95727c24b19468813d596d5ae596
alpine:3.21.2@sha256:56fa17d2a7e7f168a043a2712e63aed1f8543aeafdcee47c58dcffe38ed51099
```

This way, the base image will not change unexpectedly.

## Usage of non-root user

I created a non-root user to run the application.

## Writing maintainer label

I wrote the maintainer label in the Dockerfile.

## Dockerfile linting

I linted the Dockerfile using the [hadolint](https://hadolint.github.io/hadolint/).
