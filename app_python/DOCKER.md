# Python Web Application

## ✅ Best Practices

### Using linter

I use `hadolint` linter to ensure that `Dockerfile` adheres to best practices and to identify possible problems early.

### Minimal base image

I use a lightweight image that is based on Alpine Linux and I specify the exact versions of Python and Alpine. This reduces the image size and the potential attack surface.

### Using working directory

I set the `WORKDIR`, which improves code readability and prevents some bugs with incorrect paths from appearing.

### Installing only required dependencies

By using `requirements.txt` file with `--no-cache-dir` flag I install only those packages that are required and do not save unnecessary caches.

### Copying only necessary files

By using `.dockerignore` and copying only specific files, I reduce the image size and the potential attack surface.

### Using nonroot user

I create and use a nonroot user to run the application, reducing security risks.

### Layer sanity

File copying and requirements installation steps are ordered to utilize Docker layer caching.
