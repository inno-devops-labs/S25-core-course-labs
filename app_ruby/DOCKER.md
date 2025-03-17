# Docker best practices

## **Use of an Official Base Image**

I used lightweight Alpine-based official Ruby image `ruby:3.4.1-alpine3.21`, which significantly reduces the image size with pinned version tag to ensure consistency across builds and avoids unexpected issues due to updates in the base image.

## **Non-Root User**

I create user with limited permissions and use it in the container. This mitigates the risk of privilege escalation in case of an exploit.

## **Optimized build process with layer caching**

This layer will only be rebuilt if `Gemfile` changes, leveraging Docker’s layer caching and reducing build times.

## **.dockerignore**

I keep the `.dockerignore` file clean and avoid using the `COPY . .` in the Dockerfile, to make sure that only the necessary files will be added to the image.

## **Use Haskell Dockerfile Linter**

[Hadolint](https://github.com/hadolint/hadolint) is a smarter Dockerfile linter that helps to build best practice Docker images.

## **Docker Scout**

I analyze image with Docker Scout to find out possible vulnerabilities and fix them.

<img width="1204" alt="Docker Scout" src="https://github.com/user-attachments/assets/6749da86-f21f-447c-8ca4-3097c1add321" />

## **DockerHub**

Image is available on [DockerHub](https://hub.docker.com/repository/docker/ebob/omsk-time/tags/v1.0/sha256-0d436c0125cf7307f573fa7f7cf3b7ab2671ba3fe1455babeb08ee45f213ec11)

## **Distroless Image**

Additionaly, I build distroless image. I didn't create an additional user because I used a container with a `nonroot` tag. Distroless image appeared to be 70 MB larger than the original one. I think this is because we don't compile the ruby program into a binary file, so reducing the size is not an advantage. Also `alpine` base image did not work in distroless environment, so I used `slim` which is a little bit larger. But the distroless container is a very good solution in terms of security: it does not contain shell and other utilities that reduce attack surface.

Here is image size comparison:

<img width="1389" alt="Comparison Size" src="https://github.com/user-attachments/assets/a4e6ba3c-169b-4efa-b341-43759dd4a3d7" />

I upload it on [DockerHub](https://hub.docker.com/repository/docker/ebob/omsk-time/tags/v1.0-distroless/sha256-f7e2aba76f6b08839e08129c95aa371841a48f780116d12e9e8f66840b20c3f8) too
