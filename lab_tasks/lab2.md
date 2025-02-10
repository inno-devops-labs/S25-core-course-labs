# Lab 2: Containerization - Docker

## Overview

In this lab assignment, you will learn to containerize applications using Docker, while focusing on best practices. Additionally, you will explore Docker multi-stage builds. Follow the tasks below to complete the lab assignment.

## Task 1: Dockerize Your Application

**6 Points:**

1. Create a `Dockerfile`:
   - Inside the `app_python` folder, craft a `Dockerfile` for your application.
   - Research and implement Docker best practices. Utilize a Dockerfile linter for quality assurance.

2. Build and Test Docker Image:
   - Build a Docker image using your Dockerfile.
   - Thoroughly test the image to ensure it functions correctly.

3. Push Image to Docker Hub:
   - If you lack a public Docker Hub account, create one.
   - Push your Docker image to your public Docker Hub account.

4. Run and Verify Docker Image:
   - Retrieve the Docker image from your Docker Hub account.
   - Execute the image and validate its functionality.

## Task 2: Docker Best Practices

**4 Points:**

1. Enhance your docker image by implementing [Docker Best Practices](https://docs.docker.com/build/building/best-practices/).
   - No root user inside, or you will get no points at all.

2. Write `DOCKER.md`:
   - Inside the `app_python` folder, create a `DOCKER.md` file.
   - Elaborate on the best practices you employed within your Dockerfile.
   - Implementing and listing numerous Docker best practices will earn you more points.

3. Enhance the README.md:
   - Update the `README.md` file in the `app_python` folder.
   - Include a dedicated `Docker` section, explaining your containerized application and providing clear instructions for execution.
     - How to build?
     - How to pull?
     - How to run?

### List of Requirements

- Rootless container.
- Use COPY, but only specific files.
- Layer sanity.
- Use `.dockerignore`.
- Use a precise version of your base image and language, example `python:3-alpine3.15`.

## Bonus Task: Multi-Stage Builds Exploration

**2.5 Points:**

1. Dockerize Previous App:
   - Craft a `Dockerfile` for the application from the prior lab.
   - Place this Dockerfile within the corresponding `app_*` folder.

2. Follow Main Task Guidelines:
   - Apply the same steps and suggestions as in the primary Dockerization task.

3. Study Docker Multi-Stage Builds:
   - Familiarize yourself with Docker multi-stage builds.
   - Consider implementing multi-stage builds, only if they enhance your project's structure and efficiency.

4. Study Distroless Images:
   - Explore how to use Distroless images by reviewing the official documentation: [GoogleContainerTools/distroless](https://github.com/GoogleContainerTools/distroless).
   - Create new `distroless.Dockerfile` files for your Python app and your second app.
   - Use the `nonroot` tag for both images to ensure they run with non-root privileges.
   - Verify that the applications work correctly with the Distroless images.
   - Compare the sizes of your previous Docker images with the new Distroless-based images.
   - In the `DOCKER.md` file, describe the differences between the Distroless images and your previous images. Explain why these differences exist (e.g., smaller size, reduced attack surface, etc.).
   - Include a screenshot of your final results (e.g., image sizes).
   - Add a new section to the `README.md` file titled "Distroless Image Version".

### Guidelines

- Utilize appropriate Markdown formatting and structure for all documentation.
- Organize files within the lab folder with suitable naming conventions.
- Create pull requests (PRs) as needed: from your fork to the main branch of this repository, and from your fork's branch to your fork's master branch.

> Note: Utilize Docker to containerize your application, adhering to best practices. Explore Docker multi-stage builds for a deeper understanding, and document your process using Markdown.
