# Docker Implementation Guide

## Best Practices Implemented

### 1. **Non-Root User**  
   The container runs under a dedicated non-root user (`myuser`) to minimize security risks.  
   ```dockerfile
   RUN adduser -D myuser && mkdir -p /app && chown myuser:myuser /app
   USER myuser
   ```

### 2. **Optimized Base Image**  
   Uses `python:3.9-alpine3.15` for its small size, security updates, and compatibility.
   ```dockerfile
   FROM python:3.9-alpine3.15
   ```

### 3. **Layer Caching**  
   Dependencies are installed before copying application code to leverage Docker build cache.
   ```dockerfile
   COPY --chown=myuser:myuser requirements.txt .
   RUN pip install --user --no-cache-dir -r requirements.txt
   ```

### 4. **Production Configuration**  
   Debug mode is explicitly disabled for security.
   ```dockerfile
   ENV FLASK_ENV=production
   ```

### 5. **Minimal Build Context**  
   `.dockerignore` excludes development files to reduce image size:
   ```
   venv/
   __pycache__/
   *.pyc
   .git/
   ```

### 6. **Port Management**  
   Explicitly exposes port 5000 and runs the Flask app.
   ```dockerfile
   EXPOSE 5000
   CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
   ```

## Workflow Commands  

### **Build the Image**  
```bash
docker build -t yehiasobeh/moscow-time-app:latest .
```

### **Push to Docker Hub**  
```bash
docker login
docker push yehiasobeh/moscow-time-app:latest
```

### **Pull and Run**  
```bash
docker pull yehiasobeh/moscow-time-app:latest
docker run -p 5000:5000 yehiasobeh/moscow-time-app
```

## Security Practices  
🛡️ **Non-root execution:** Mitigates container breakout risks.  
🛡️ **No cached dependencies:** `--no-cache-dir` flag reduces image bloat.  
🛡️ **Alpine Linux:** Minimal base image with security updates.  

## Troubleshooting  

- **Permission Issues:** Ensure the working directory (`/app`) is owned by `myuser`.  
- **Dependency Conflicts:** Use explicit versions in `requirements.txt`.  
- **Port Conflicts:** Check if port `5000` is free before running the container.  

---


