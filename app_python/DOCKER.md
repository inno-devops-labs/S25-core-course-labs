# Dockerfile Best Practices Explained

This document highlights the best practices followed in the `Dockerfile` for the `app_python` project, which builds a container image for a Python Flask application. The Dockerfile was crafted following [Docker's best practices](https://docs.docker.com/build/building/best-practices/), with additional insights from the Hadolint linter for validation.

## 1. Choosing the Right Base Image
    ```
    FROM python:3-alpine3.15
    ```
We chose python:3-alpine3.15 as the base image. This image is based on Alpine Linux, a lightweight distribution that minimizes the overall size of the container image. Alpine images are a great choice for production environments, reducing attack surface and improving security.

## 2. Efficient Layering
We ensure that each instruction in the Dockerfile adds only necessary changes to the image layers. This reduces the overall size and complexity of the final image. Layers are cached in Docker, so this organization makes sure that steps are efficiently executed.

## 3. Bind Mount Instead of Copy
    ```
    RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
        pip install --no-cache-dir --requirement /tmp/requirements.txt
    ```
Bind mounts are more efficient than ```COPY``` for including files from the build context in the container, as bind-mounted files are only added temporarily for a single RUN instruction, and don't persist in the final image.

## 4. Minimal Copy Instructions
Instead of using a single ```COPY . .``` command, we copy only the necessary files individually. This ensures that only the files needed for the application are included in the image, preventing unnecessary files from being added to the image.

## 5. Avoiding Unnecessary Installation of Recommends
    ```
    RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
        pip install --no-cache-dir --requirement /tmp/requirements.txt
    ```
We avoid installing recommended packages with ```--no-install-recommends```, which helps reduce the image size by not including extra dependencies that are not essential for the application to run.

## 6. Exposing the Correct Port
    ```
    EXPOSE 8000
    ```
We use the ```EXPOSE``` directive to specify that the application will listen on port 8000, which matches the configuration in the main Flask app code. 

## 7. Clean Up Temporary Files
We make sure to clean up after installing dependencies by using the ```--no-cache-dir``` option for pip and removing any unnecessary files.

## 8. Hadolint for Dockerfile Linting

We used Hadolint to organize and clean up the Dockerfile by identifying inefficiencies and enforcing best practices. It ensured proper layer management, optimized commands, and minimized unnecessary dependencies, resulting in a leaner and more maintainable Dockerfile.

# The Difference Between The Distroless Image and The Previous Image

## The Previous Image
A Python base image was used and the whole Dockerfile consisted of one stage where it was needed to install some extra packages and then run the app.

## The Distroless Image
The Dockerfile consisted of 2 stages, where in the first stage a Python base image was used to install the packages into a target folder, while the second stage a distroless Python image waas used and it copied the installed packages from the previous stage which helped to decrease the size of the final docker image. Moreover, a nonroot distroless Python base image was used (v1.0.1).

![Distroless image -> 59MB - Previous image -> 69 MB](assets/comparison.jpg)