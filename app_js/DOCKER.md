# Docker

**Docker Hub (default)**: click the [link](https://hub.docker.com/r/nickolaus899/js-cities-dist)
**Docker Hub (distroless)**: click this [link](https://hub.docker.com/r/nickolaus899/js-distroless)


### Slim
The *slim* version was taken to decrease
the size of the image: `node:16-slim`

### Best practices:
* **Minimalistic image**: use of `python:3.10-slim` to decrease size
of the image
* **Usage of only necessary files**: `COPY` is applied only
to the files needed for the application & `.dockerignore`
is set
* **Distroless imagess**: for decreasing size of an image
* **Security**: running everything as a non-root user (for both
default and distroless cases)


### Distroless
Decreased size from 179MB to 113MB.

### Multi-stage building
Multi-stage building was considered as not suitable for the 
default case. However, I have implemented it for the 
distroless docker. There are two separated stages