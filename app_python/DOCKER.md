# Best practices

## 1. Specific image with specific version: `FROM python:3.10-alpine3.18 AS base`.

Alpine image reduces image size and pinned version helps to avoid issues after image update.

## 2. Copying only needed files

Copy only the files required for the build to reduce the attack surface.

## 3. Formatting file with `hadolint`

Lint and format Dockerfile using `hadolint` to ensure best practices.

## 4. Dockerignore file

Use a `.dockerignore` file to exclude unnecessary files from the build context.

## 5. Rootless container

Run containers as a non-root user to enhance security.