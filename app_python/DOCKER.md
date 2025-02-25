# Docker Implementation Guide

## Overview
This document outlines the Docker implementation for the Moscow Time Display application, highlighting the best practices employed to ensure security, efficiency, and maintainability.

## Best Practices Implemented

### 1. Security Best Practices
- **Non-root User**
  - Created dedicated non-root user `appuser` with specific UID/GID (1001)
  - Restricted shell access using `/sbin/nologin`
  - All processes run with limited privileges
  - Explicit file permissions (755) for application files

- **Multi-stage Build**
  - Separate builder stage for compilation and dependencies
  - Final stage contains only runtime components
  - Reduced attack surface and image size

- **Security Configurations**
  - No sensitive data in image layers
  - Proper file ownership and permissions
  - Proxy headers handling for security behind reverse proxies

### 2. Image Optimization
- **Base Image Selection**
  - `python:3.11-slim-bullseye` for minimal footprint
  - Specific version pinning for reproducibility
  - Slim variant to reduce attack surface

- **Layer Optimization**
  - Strategic layer ordering for optimal caching
  - Minimal number of layers
  - Combined RUN commands where appropriate
  - Cleaned package manager caches

- **File Management**
  - `.dockerignore` for excluding unnecessary files
  - Selective file copying with explicit ownership
  - Only production-required files included

### 3. Build Time Optimizations
- **Dependency Management**
  - Requirements installed with `--no-cache-dir` and `--no-compile`
  - Separate layer for pip installations
  - Cleaned apt caches after package installation

- **Build Arguments and Labels**
  - Build-time arguments for versioning
  - OCI standard labels for metadata
  - Source code reference and maintainer information

### 4. Runtime Optimizations
- **Environment Configuration**
  - `PYTHONDONTWRITEBYTECODE=1`: Prevents bytecode generation
  - `PYTHONUNBUFFERED=1`: Unbuffered output
  - `PYTHONPATH` and `PATH` properly configured
  - Timezone setting for application functionality

- **Health Monitoring**
  - Implemented HEALTHCHECK
  - Regular health status monitoring
  - Configurable check intervals and thresholds

### 5. Container Runtime Security
- **Process Isolation**
  - Non-root user execution
  - Limited file system access
  - Explicit port exposure

- **Resource Management**
  - Clear port specifications
  - Process running as non-privileged user
  - Proper signal handling

## Usage Instructions

### Building the Image
```bash
# Build with build-time arguments
docker build -t moscow-time \
  --build-arg BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ') \
  --build-arg VERSION=1.0 \
  .
```

### Running the Container
```bash
# Run with recommended settings
docker run -d \
  --name moscow-time \
  -p 8000:8000 \
  --security-opt no-new-privileges \
  --cap-drop ALL \
  moscow-time
```

### Health Check
The container includes a health check that runs every 30 seconds:
```bash
# View container health status
docker inspect --format='{{.State.Health.Status}}' moscow-time
```

## Security Considerations
1. The container runs as a non-root user (UID 1001)
2. Minimal base image to reduce attack surface
3. No unnecessary packages or tools installed
4. Proper file permissions and ownership
5. Security-related flags enabled for runtime

## Maintenance
- Regular base image updates recommended
- Monitor security advisories for dependencies
- Review logs for health check status
- Update build arguments for new versions
