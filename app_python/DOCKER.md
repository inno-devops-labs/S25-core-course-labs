# Docker image report

## Best practices

- Debian-based image is better for installing dependencies because [Alpine uses musl and it might need a compiler to build a .whl](https://pythonspeed.com/articles/alpine-docker-python/). Ready-made packages are available in the Alpine package manager but using it hurts the portability.
- Versioned images are better for security and reproducibility.
- App file copied after requirements to avoid reinstalling dependencies on every layer change.
- Non-root user is used to avoid potential security issues.
- Official image is used
- Buildx cache (buildx required) is used for pip to speed up the installation even if the previous layers have been changed
- Array notation for cmd over string cmd for not spawning a shell and for maintainability
