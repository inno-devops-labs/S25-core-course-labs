# Docker Best Practices Implemented

## Right base image

I used `golang:1.23.5-alpine3.21` as the base image.
It is a lightweight image that contains only the necessary packages.
So, the final image is smaller.

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
```

This way, the base image will not change unexpectedly.

## Usage of non-root user

I created a non-root user to run the application.

## Writing maintainer label

I wrote the maintainer label in the Dockerfile.

## Dockerfile linting

I linted the Dockerfile using the [hadolint](https://hadolint.github.io/hadolint/).
