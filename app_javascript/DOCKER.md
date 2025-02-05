# Docker Best Practices

## Best Practices Implemented

### 1. **Rootless Container**

- A non-root user (`appuser`) and group (`appgroup`) are created using `addgroup -S` and `adduser -S` to ensure the container does not run as the root user.
     The `USER appuser` instruction is used to restrict permissions, enhancing security.

---

### 2. **Precise Base Image**

- The base image `node:18.18.0-alpine3.18` was selected for its:
  - **Specific version**: Ensures predictable and reproducible builds.
    - **Lightweight nature**: Alpine minimizes image size compared to standard Node.js images.
    - **Security**: Reduces the attack surface by including only the necessary dependencies.

---

### 3. **Layer Sanity**

- Instructions are logically grouped to minimize the number of layers while keeping readability,
      (`npm install` is isolated for caching benefits, `COPY` operations are structured to reduce unnecessary rebuilds).
  - The layers are ordered to optimize Docker's caching mechanism, speeding up rebuilds.

---

### 4. **Copy Specific Files**

- Only the required application files (`index.html`, `style.css`, `script.js`) are copied into the container, avoiding unnecessary files and improving build efficiency.

## Running with Docker

   ```bash
    docker build -t app_js .
    docker run -p 8080:8080 app_js
   ```

Alternatively, you can pull the Docker image from my [Dockerhub repository](https://hub.docker.com/r/vladis7love/app_js) using the following commands:

   ```bash
   docker login
   docker pull vladis7love/app_js:latest
   docker run -p 8080:8080 vladis7love/app_js
   ```

Now, open your browser and go to <http://localhost:8080> to view the countdown timer application.
