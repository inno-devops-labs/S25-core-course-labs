# Best Practices Implemented

# Use a Specific Base Image

- Base image: `python:3.10-slim-bullseye`.
- Using a specific version ensures consistency and avoids breaking changes from updates.

# Rootless Container

Created a non-root user (`appuser`) and assigned it as the user to run the application:
  ```dockerfile
  RUN groupadd -r appgroup && useradd --no-log-init -r -g appgroup appuser
  USER appuser
  ```

Layer sanity maintained by copying only required files and installing dependencies in separate layers:

```
  COPY requirements.txt .
  RUN pip install --no-cache-dir -r requirements.txt
  COPY app.py .
```


Added a `.dockerignore` file to exclude unnecessary files such as `__pycache__`, `.env`, and logs.

Exposed port `5000` using:

 ```dockerfile
     EXPOSE 5000
```

# Security and Minimal Image
   - Used the `slim` variant of Python to minimize the image size and reduce the attack surface.

---

# Advantages of These Practices
- Running as a non-root user enhances container security.
- Using a slim base image and ignoring unnecessary files reduces image size.
- Separating `COPY` and `RUN` commands allows Docker to cache layers effectively.
- Using a specific base image version ensures consistent builds.
