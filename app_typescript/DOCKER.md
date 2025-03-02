# Best practices

## 1. Specific image with specific version: `FROM node:22-alpine3.18 AS base`.

Alpine image reduces image size and pinned version helps to avoid issues after image update.

## 2. Copying only needed files

Copy only the files required for the build to reduce the attack surface.

## 3. Formatting file with `hadolint`

Lint and format Dockerfile using `hadolint` to ensure best practices.

## 4. Dockerignore file

Use a `.dockerignore` file to exclude unnecessary files from the build context.

## 5. Rootless container

Run containers as a non-root user to enhance security.

# Comparison with Distroless image

## 1. Size

![Images size comparison](sizes.png)

As we can see, distroless container is almost twice smaller.

## 2. Base image
* Previous: Used `node:22-alpine3.18` as the base image. This is an Alpine-based image,
known for its small size but includes a package manager and shell.

* Distroless: Uses a `distroless/nodejs20-debian11:nonroot` image for the runtime. 
Distroless images are minimal and include only the runtime environment required for the application,
with no shell or package manager.

## 3. Security

* Previous: A non-root user is manually created (`app_typescript_user`), 
but the Alpine base image may still include unused packages and tools, which could introduce vulnerabilities.

* Distroless: The `nonroot` tag enforces the use of a non-root user
and avoids additional unnecessary tools, further reducing the attack surface.

## 4. Build Process

* Previous: Combined the build and runtime stages in a single image, leading to a larger final image.

* Distroless: Introduces a multi-stage build process:

  * A `build-env` stage for building the application.
  * A `deps-env` stage for preparing production dependencies.
  * A final `run-env` stage that only includes the built application and runtime dependencies.

## 5. Entry Point

* Previous: Executes `npm run preview`, relying on `npm` being available in the runtime image.

* Distroless: Directly runs the Vite CLI (`vite preview`) via the Node.js runtime, bypassing the need for `npm`.