# Docker image report

## Best practices

- Debian-based image is better for installing dependencies because [Alpine uses musl and it might need a compiler to build a .whl](https://pythonspeed.com/articles/alpine-docker-python/). Ready-made packages are available in the Alpine package manager but using it hurts the portability.
- Versioned images are better for security and reproducibility.
- App file copied after requirements to avoid reinstalling dependencies on every layer change.
- Non-root user is used to avoid potential security issues.
- Official image is used
- Buildx cache (buildx required) is used for pip to speed up the installation even if the previous layers have been changed
- Array notation for cmd over string cmd for not spawning a shell and for maintainability

## Distroless image

- Distroless image is used to reduce the size of the image and to avoid potential security issues.
- Additionally, the rootless tag was used to avoid potential privelege escalation issues.
- It lacks a shell and some basic system tools (like `ls`, `cat`, etc.), so it's not suitable for debugging.
- This image has a Python version that comes with the Debian image that it was derived from (Python 3.11) in my case, so I had to change the image in the dependencies stage to use the compatible Python version.
- With some trial and error I found out how to copy the dependencies from the `python:3.11-slim-bullseye` image to the `gcr.io/distroless/python3-debian12:nonroot` image.
  - The `COPY --from=build-env /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages` was the example but did not work.
  - Copying venv didn't work either because it was symlinking to /usr/local/lib which was not present in the distroless image.
  - The solution was to copy the site-packages and define the `PYTHONPATH` environment variable to point to it.
- The image size is 80% smaller than the previous one.

```
fallenchromium/moscow-timezone-app       latest        d5bb751c7626   7 minutes ago       184MB
fallenchromium/moscow-timezone-app       distroless    3228c6c1c73d   About an hour ago   101MB
```
