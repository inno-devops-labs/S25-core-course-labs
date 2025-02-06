# Docker

**Docker Hub (default)**: click the [link](https://hub.docker.com/r/nickolaus899/python-msk-time)
**Docker Hub (distroless)**: click this [link](https://hub.docker.com/r/nickolaus899/py-distroless)

### Base image
`python:3.10-slim` was taken as a lighweight (slim) version
of Python 3.10 for this small project - *slim* keeps
the size of image small.



### Best practices
* **Minimalistic image**: use of `python:3.10-slim` to decrease size
of the image
* **Usage of only necessary files**: `COPY` is applied only
to the files needed for the application & `.dockerignore`
is set
* **Clean up**: the `--no-cache-dir` prevents
increase of image size because of cache files 
* **Security**: running everything as a non-root user (*appuser*)
* **Distroless image**: for decreasing size
* **Multi-stage for distroless image**: building and running


### Distroless
Size decreased from 139MB to 57.7MB.
