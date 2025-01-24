# Overview

Let's begin with a step-by-step explanation of all the solutions I used to create a Dockerfile:

---

## Base Image Selection

- **Precise Image**: Use a specific image version to preserve the stability of the build and ensure that no changes can
  be made by third parties (image owners).
- **Slim Version**: Choose the slim version to reduce the size of the resulting image.

  ```dockerfile
  FROM python:3.12.0-slim AS base
  ```

## Security Enhancements

- **Non-Root User**: Create a non-root user to enhance security by preventing the use of the root user.

  ```dockerfile
  RUN useradd -m appuser
  USER appuser
  ```

## Directory Structure

- **Working Directory**: Setting up the working directory is a standard in image creation because it helps to maintain a
  clear file structure.

  ```dockerfile
  WORKDIR /app
  ```

## File Management

- **Selective File Copying**: Copy only the necessary files for the application to start and run properly.
- **Order of COPY Commands**: Arrange the `COPY` commands in descending order of volatility, from the most volatile
  files to the most stable, to catch build errors earlier.
- **Ownership**: Ensure the correct `appuser` ownership is applied to the application sources.

  ```dockerfile
  COPY --chown=appuser:appuser requirements.txt .
  COPY --chown=appuser:appuser app/.env* ./
  COPY --chown=appuser:appuser app ./app
  COPY --chown=appuser:appuser run.py .
  ```

## Dependency Management

- **Install Dependencies**: Run dependencies installation with no cache to avoid using external space.

  ```dockerfile
  RUN pip install --no-cache-dir -r requirements.txt
  ```

## Container Startup

- **ENTRYPOINT Command**: Use the `ENTRYPOINT` command because we have a single application and generally do not want
  users to override container startup logic.

  ```dockerfile
  ENTRYPOINT ["python", "run.py", ".env"]
  ```

## Optimization

- **.dockerignore Usage**: Additionally, include a `.dockerignore` file to exclude unnecessary files from the final
  image.

---

Additionally, I do not use multi-stage builds because for Python applications that are not compiled
this is unnecessary.
