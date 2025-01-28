# Docker Best Practices

## Best Practices Implemented

### 1. **Using a Minimal Base Image**

- I use `python:3.9-slim` instead of `python:3.9` to minimize the image size and reduce security vulnerabilities.
  ```dockerfile
  FROM python:3.9-slim
  ```

### 2. **Setting a Working Directory**

- Using `WORKDIR /app` ensures all subsequent commands run within the `/app` directory, improving maintainability.
  ```dockerfile
  WORKDIR /app
  ```

### 3. **Copying Only Necessary Files**

- Instead of copying everything, I copy only the required files to minimize image size.
  ```dockerfile
  COPY requirements.txt ./
  COPY web_app.py ./
  ```

### 4. **Using a .dockerignore File**

- A `.dockerignore` file is included to exclude unnecessary files from the build context:
  ```plaintext
  .venv/
  *.pyc
  __pycache__/
  *.env
  .git/
  ```
- This reduces image size and improves build performance.

### 5. **Installing Dependencies Efficiently**

- Using `--no-cache-dir` prevents pip from storing cache, reducing image bloat.
  ```dockerfile
  RUN pip install --no-cache-dir -r requirements.txt
  ```

### 6. **Exposing Only Necessary Ports**

- The application runs on port `5000`, so I explicitly expose it.
  ```dockerfile
  EXPOSE 5000
  ```

### 7. **Running the Application with CMD**

- Using `CMD` instead of `ENTRYPOINT` makes it easier to override the default command during runtime if needed.
  ```dockerfile
  CMD ["python", "web_app.py"]
  ```

### 8. **Avoiding Running as Root User**

- Currently, the container runs as root, which is not a best practice.
- To enhance security, I created a non-root user and run the application as that user:
  ```dockerfile
  RUN useradd -ms /bin/bash appuser
  USER appuser
  ```
- This prevents privilege escalation in case of security vulnerabilities.

