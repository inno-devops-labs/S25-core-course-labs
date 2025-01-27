# app_python

## Best practices used

1. **Specific Base Image Version**

   Using `python:3.11.6-slim-bullseye` ensures reproducibility

2. **Environment Variables**

   - `PYTHONUNBUFFERED=1`: Ensures logs are output in real-time
   - `PYTHONDONTWRITEBYTECODE=1`: Prevents Python from creating `.pyc` files

3. **Rootless Container**

   - Created a system user `appuser` and group `appgroup`
   - Using the non-root user for all operations, enhancing security

4. **Minimized File Copying**

   - Used `COPY` for specific files instead of the entire directory
   - Ensured proper ownership of copied files with the `--chown` option

5. **Layer Optimization**

   - Related commands are grouped in a single `RUN` instructions where possible
   - Installed Python dependencies in a single step

6. **Using `.dockerignore`**

7. **Explicit Port Exposure**
