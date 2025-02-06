# Docker Best Practices

## Rootless Container

- A **non-root user (`appuser`)** runs the application to **enhance security**.
- Prevents privilege escalation risks.

## Using COPY for Specific Files

- Instead of `COPY . .`, **only necessary files** are copied:
  - `requirements.txt` (dependencies first for caching).
  - `time_app.py` and `templates/` (after dependencies are installed).

## Optimized Layering (Layer Sanity)

- **Installing dependencies first** enables Docker’s caching mechanism.
- **Avoids redundant `chown` operations** by setting ownership **during file copy**.

## Minimal & Secure Base Image

- Using `python:3.11-alpine3.18`:
  - **Alpine-based** images are **smaller (~15MB)** and **more secure** than full Debian-based images.

## `.dockerignore`

- **Prevents unnecessary files** from being copied into the Docker image.
- Keeps the image **clean, lightweight, and efficient**.
