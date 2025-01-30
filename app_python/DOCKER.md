# Docker Best Practices Implemented

## Running as a Non-Root User
- The application runs under **appuser** instead of the root user.
- This enhances security and prevents privilege escalation.

## Minimal and Precise Base Image
- `python:3.11.6-alpine3.18` is used instead of a generic Python image.
- Alpine-based images are much smaller, improving efficiency.

## Using `.dockerignore`
- Unnecessary files like `__pycache__/`, `.env`, and `venv/` are **excluded** from the image to reduce build size.

## Dependency Management
- Dependencies are installed using `pip install --no-cache-dir`, preventing unnecessary cache bloat.

## Optimized Layering
- `requirements.txt` is copied and dependencies are installed **before** copying the rest of the application.
- This ensures Docker’s layer caching optimizes rebuild times.

## Using a Dedicated Work Directory
- The working directory is set to `/app` for better organization.

## Copying Only Necessary Files
- Instead of `COPY . .`, only **required files** are copied (`requirements.txt`, `app.py`).
- This minimizes unnecessary rebuilds.

## Exposing Only Necessary Ports
- `EXPOSE 5000` explicitly signals the port Flask runs on.

## Setting Proper Ownership and Permissions
- The app directory is assigned to `appuser` with `chown`, preventing permission issues.

## Using CMD Instead of ENTRYPOINT
- `CMD ["python", "main.py"]` ensures flexibility for overriding the default command.
