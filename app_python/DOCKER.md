# Used Docker Best Practices

## Security

Used a non-root user instead of running as root.

## Right choice of image

Picked a smaller base image: python:3.10-alpine instead of python:latest.

## Optimization of image size

Used --no-cache with pip to keep the image smaller.

## Optimized COPY

Added only requirements.txt first to use caching.

## Exclude with .dockerignore

Added .dockerignore to skip unnecessary files in the build.
