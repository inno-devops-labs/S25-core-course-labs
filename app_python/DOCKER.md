# Docker best practices

## 1. Usage of a lightweight base image

The most common one is Alpine base image with a tag number, for example in my case
it is `python:3.12-alpine3.18`.

## 2. Copying of specific files only

This reduces the attack surface.

## 3. Rootless container

This reduces the attack surface as well.

## 4. Linting and .dockerignore

I added `dockerfilelint` pre-commit hook and `dockerignore` file.
