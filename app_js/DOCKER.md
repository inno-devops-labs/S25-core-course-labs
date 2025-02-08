# Docker Best Practices

## Introduction
This file describes the Docker best practices implemented in the `app_js` containerization process. Following these best practices ensures security, performance, and maintainability.

## Best Practices

### 1. **Rootless Container**
- The application does not run as the root user.
- A dedicated user `appuser` is created to enhance security.

```dockerfile
RUN useradd -m appuser
USER appuser
```

### 2. Use a Minimal and Specific Base Image
- I used `node:20-alpine` for the build stage and `gcr.io/distroless/nodejs20:nonroot` for the runtime stage

```dockerfile
FROM node:20-alpine AS builder

FROM gcr.io/distroless/nodejs20:nonroot
```

### 3. Efficient Layer Management
- The `COPY` command is used in a structured manner to optimize caching.
- Dependencies are installed before copying the entire source code to avoid unnecessary rebuilds.

```dockerfile
COPY package*.json ./  # Install dependencies first to optimize caching
RUN npm ci --omit=dev   # Install only production dependencies
COPY . .               # Copy the application code
```

### 4. Expose Only Required Ports
- Only the necessary port `(3000)` is exposed to reduce the attack surface.

```dockerfile
EXPOSE 3000
```

### 5. Define a Clear Entry Point
- The application is started using the `CMD` instruction to allow easy overriding.

