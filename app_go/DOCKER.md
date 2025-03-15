# Go Web Application

## ✅ Best Practices

### Using linter

I use `hadolint` linter to ensure that `Dockerfile` adheres to best practices and to identify possible problems early.

### Minimal base image

I use a lightweight image that is based on Alpine Linux and I specify the exact versions of Go and Alpine. This reduces the image size and the potential attack surface.

### Using working directory

I set the `WORKDIR`, which improves code readability and prevents some bugs with incorrect paths from appearing.

### Installing only required dependencies

By using `go.mod` and `go.sum` files I install only those packages that are required.

### Copying only necessary files

By using `.dockerignore` and copying only specific files, I reduce the image size and the potential attack surface.

### Using nonroot user

I create and use a nonroot user to run the application, reducing security risks.

### Layer sanity

File copying and dependency installation steps are ordered to utilize Docker layer caching.

### Multi-stage building

I implement a multi-stage build process to separate the build environment from the runtime environment. This provides a smaller final image as it includes only binary and static files.

## 🐟 Distroless Version

### Size comparison

A distroless image turned out more than 2x smaller than a distro-based image (18.5 MB vs 40.9 MB, respectively).

This is because distroless version is a stripped down version of Debian. It contains a minimal environment to run binary files.

### Differences from distro-based version

- Smaller attack surface

    By removing shells, package managers, and other tools, we lower the amount of components in the container, therefore, reducing the attack surface.

- Image size

    The distroless version has a smaller image size, due to different components being removed.

- Worse debugging

    Due to different components being removed, the debugging capabilities are more worse than in distro-based version.

### Final result

![Image size comparison](media/sizes.png)
