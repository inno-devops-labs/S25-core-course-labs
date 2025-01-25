# Docker Best Practices Implemented

## Right base image

I used `python:3.12.8-alpine3.21` as the base image.
It is a lightweight image that contains only the necessary packages.
So, the final image is smaller.

## Usage of `.dockerignore`

I used a `.dockerignore` file to exclude unnecessary files and directories
from the build context, improving the build performance.

## Creation of ephemeral container

Container needs no configuration to run. It is ready to run as soon as it is created.

## Installation of only necessary packages

The requirements.txt file contains only the necessary packages.

## Right order of instructions

The instructions are ordered in such a way that
the layers that change the least are placed at the top.
This way, the cache can be used more effectively.

## Pin base image version

I pinned the version of the base image to the following specific version:

```
python:3.12.8-alpine3.21@sha256:ba13ef990f6e5d13014e9e8d04c02a8fdb0fe53d6dccf6e19147f316e6cc3a84
```

This way, the base image will not change unexpectedly.

## Usage of non-root user

I created a non-root user to run the application.

## Disabling of Python cache

I disabled the Python cache to reduce the size of the final image.

## Writing maintainer label

I wrote the maintainer label in the Dockerfile.

## Dockerfile linting

I linted the Dockerfile using the [hadolint](https://hadolint.github.io/hadolint/).
