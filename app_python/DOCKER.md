# Docker best practices

## 1. Using a specific trusted lightweight base image

For this project, I chose the `python:3.12.8-alpine3.21` base image. Using a specific version ensures consistency.

## 2. Copying only specific files

I copied only the necessary files (`app.py`, `requirements.txt`, and the `templates` folder) into the container. This approach minimizes the container's attack surface by eliminating unnecessary files.

## 3. Rootless and UID-independent container

Following Docker security best practices, I created a rootless user named `python_usr` and configured the container to run under that user.

## 4. Dockerignore

I implemented the `.dockerignore` file to exclude files that should not be part of the image build, such as local configuration files or secrets.

## 5. Miscellaneous improvements

- **Prefer COPY instead of ADD**: I used `COPY` to explicitly copy files instead of `ADD` since `COPY` is more predictable and conforms to best security practices.
- **Explicit EXPOSE**: I used the `EXPOSE 8080` directive to explicitly document the intended use of the container on the network.
- **No-Cache Pip Install**: To reduce the image size and improve security, I used the `--no-cache-dir` option in `pip install`.
