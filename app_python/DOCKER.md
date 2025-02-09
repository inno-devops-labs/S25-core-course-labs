# Docker best practices

## **Use of an Official Base Image**

I used lightweight Alpine-based official Python image `python:3.13.1-alpine3.21`, which significantly reduces the image size with pinned version tag to ensure consistency across builds and avoids unexpected issues due to updates in the base image.

## **Non-Root User**

I create user with limited permissions and use it in the container. This mitigates the risk of privilege escalation in case of an exploit.

## **Optimized build process with layer caching**

This layer will only be rebuilt if `requirements.txt` changes, leveraging Docker’s layer caching and reducing build times.

## **.dockerignore**

I keep the `.dockerignore` file clean and avoid using the `COPY . .` in the Dockerfile, to make sure that only the necessary files will be added to the image.

## **Use Haskell Dockerfile Linter**

[Hadolint](https://github.com/hadolint/hadolint) is a smarter Dockerfile linter that helps to build best practice Docker images.

## **Docker Scout**

I analyze image with Docker Scout to find out possible vulnerabilities and fix them.

<img width="1212" alt="Docker Scout" src="https://github.com/user-attachments/assets/672b5cc9-7dba-43e0-87fc-43e98c66a688" />

## **DockerHub**

Image is available on [DockerHub](https://hub.docker.com/repository/docker/ebob/moscow-time/tags/v1.0/sha256-963767cb63ad8759727d0507f84fa4891bffe760742a9509bd899a49a7873757)

## **Distroless Image**

Additionaly, I build distroless image. I didn't create an additional user because I used a container with a `nonroot` tag. Distroless image appeared to be 20 MB larger than the original one. I think this is because we don't compile the python program into a binary file, so reducing the size is not an advantage. But the distroless container is a very good solution in terms of security: it does not contain shell and other utilities that reduce attack surface.

Here is image size comparison:

![image](https://github.com/user-attachments/assets/37cbc610-a7a2-4da1-bcab-34a81515347b)


I upload it on [DockerHub](https://hub.docker.com/repository/docker/ebob/moscow-time/tags/v1.0-distroless/sha256-cee4db447ea129aca4c6a05e045e3de5758d01343a68345abbdd93b6affae59d) too
