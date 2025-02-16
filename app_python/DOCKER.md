# Best Practices in the Dockerfile

## 1. Use a minimal and specific base image

- **`FROM python:3.9-alpine3.15`**: Alpine-based images are lightweight and secure.

## 2. Set a working directory

- **`WORKDIR /app`**: Organizes files and avoids path issues.

## 3. Use a non-root user for security  

- **`RUN addgroup -S appgroup && adduser -S appuser -G appgroup`**  
- **`USER appuser`**: Prevents security risks.

## 4. Optimize dependency installation  

- **`COPY requirements.txt requirements.txt`**: Enables Docker layer caching.  
- **`RUN pip install --no-cache-dir -r requirements.txt`**: Reduces image size.

## 5. Copy application files separately

- **`COPY src/ src/`**

## 6. Adjust ownership of files  

- **`RUN chown -R appuser:appgroup /app`**: Prevents permission issues.

## 7. Expose required ports  

- **`EXPOSE 5000`**: Documents the service port.

## 8. Define an entry point  

- **`CMD ["python", "main.py"]`**: Specifies the default command.  
