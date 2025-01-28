# DOCKER.md

## Docker Best Practices Used

In this task, the following Docker best practices were implemented to ensure that the containerized application is efficient, secure, and follows industry standards.

### 1. **Rootless Container**

- A non-root user is created to run the application inside the container. This minimizes security risks associated with running containers as the root user.
  - The following commands were used to create and switch to a non-root user:

     ```dockerfile
     RUN adduser -D appuser
     USER appuser
     ```

### 2. **Optimized Image Layers**

- By combining related `RUN` instructions into a single command, unnecessary layers were avoided. This helps reduce the size of the Docker image and optimizes the build process.
  - For example:

     ```dockerfile
     RUN pip install --no-cache-dir -r requirements.txt
     ```

### 3. **Use of `.dockerignore`**

- A `.dockerignore` file was used to exclude unnecessary files (like `.git`, `.env`, temporary files, etc.) from being copied into the Docker image. This reduces the image size and keeps it clean.

### 4. **Precise Base Image Versioning**

- To ensure a stable and reproducible build, a specific version of the base image (`python:3-alpine3.15`) was used instead of the latest version. This helps in minimizing the final image size.

     ```dockerfile
     FROM python:3-alpine3.15
     ```

### 5. **Application Binding to 0.0.0.0**

- The Python application was configured to listen on all network interfaces (`0.0.0.0`) so that it can be accessed from outside the Docker container. The application was not bound to `127.0.0.1` (localhost).

     ```python
     app.run(host='0.0.0.0', port=5000)
     ```

### 7. **Efficiency with `COPY` Directive**

- Only the necessary files (such as `requirements.txt` and application code) were copied into the Docker image, avoiding unnecessary bloat.
  - The Dockerfile ensures that we copy the files with the correct order:

     ```dockerfile
     COPY requirements.txt .
     COPY . .
     ```

## **Distroless Image Version**

### **Differences Between Distroless and Previous Images**

1. **Size**:
   - **Distroless Image**: ~72 MB.
   - **Previous Python Image**: ~68 MB.
   - **Reason**: Distroless images contain only the application and essential runtime dependencies, without unnecessary tools. But I copied python3.*/site-packages and set the PYTHONPATH environment variable for my flask app to work. Thats why I copy it and "make my distroless image bigger", than I could. I tried different versions of distroless.Dockerfile and only the one like the one I submitted worked.

2. **Security**:
   - **Distroless Image**: Contains only runtime dependencies, no shell or package manager, reducing the attack surface.
   - **Previous Python Image**: Includes a shell and package manager, which increase potential security risks.

![Images compare](/app_python/images_compare.jpg)
