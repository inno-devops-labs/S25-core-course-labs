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

<img width="1214" alt="Docker Scout" src="https://github.com/user-attachments/assets/f1ec3eac-4cb9-428e-be46-b63ca3f44464" />
