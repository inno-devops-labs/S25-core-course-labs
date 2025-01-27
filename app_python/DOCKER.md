# Dockerfile Best Practices

## 1. **Use Official Base Images**
Using official lightweight base image ensures reliability, security, and performance.

```dockerfile
FROM python:3.12-slim
```

## 2. **Use multistage builds** 
```dockerfile
FROM python:3.12-slim as builder
```

## 3. **Leverage caching** 
```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
```

## 4. **Clean up after dependencies installation** 
```dockerfile
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*
```

## 5. **Use rootless user** 
```dockerfile
RUN useradd -m python_user && chown -R python_user:python_user /app
USER python_user
```

## 5. **Copy only necessary files** 
Compose Using .dockerignore properly





