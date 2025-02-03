
# Practices

- hadolint was used to lint the Dockerfiles
- .dockerignore file
- multistage build, one for downloading, one for execution

# Distroless vs Common | Comparison

| Image                 | Size      |
|-----------------------|-----------|
|  python:3-alpine3.15  |   105MB   |
| Distroless Image      |  94.3 MB  |

The difference between these two is that distroless has the most minimal set of libraries and binaries onboard. It contains nothing but stuff necessary to run the application.

This greatly reduces the size of image and reduces surface of attack, as there is less things to compromise.
