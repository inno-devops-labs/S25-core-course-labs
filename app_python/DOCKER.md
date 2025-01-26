# Docker Documentation (app_python)

## Docker Best Practices Implemented

1. **Rootless Container**  
   - We create a non-root user (`myuser`) in the Dockerfile.  
   - We use the `nonroot` variant of the Distroless image for even more security.

2. **Precise Base Image**  
   - `python:3.9.18-alpine3.15` ensures a known, consistent environment.

3. **Layer Efficiency**  
   - We copy `requirements.txt` and install dependencies before copying the main code.  
   - This allows Docker to cache layers and speeds up rebuilds.

4. **.dockerignore**  
   - We ignore unnecessary files like `.git`, `venv/`, etc. to reduce image size and improve build times.

5. **COPY Only Specific Files**  
   - Instead of copying the entire project, we explicitly copy `requirements.txt` and then the application code.

6. **No Root Privileges**  
   - We run as a non-root user (`myuser` or the Distroless `nonroot` user).

## Multi-Stage Builds and Distroless

- In `distroless.Dockerfile`, we use a **two-stage build**:
  1. Build all dependencies using a standard Python base.
  2. Copy the results into a **Distroless** final image.  
- **Distroless** images are smaller and more secure by removing shell and package managers.

## Image Size Comparison

| Image Type            | Approx Size | Reason for Difference                      |
|-----------------------|------------:|--------------------------------------------|
| Alpine-based Image    | ~30-40 MB   | Contains minimal OS components             |
| Distroless Image      | ~20-25 MB   | Smaller, no shell/package manager, reduced surface |

