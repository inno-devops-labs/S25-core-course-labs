# Docker Configuration

## Docker Hub Repository

The Docker image for this application is available on Docker Hub:
[eleanorpi/moscow-time-app](https://hub.docker.com/repository/docker/eleanorpi/moscow-time-app/general)

## Docker Best Practices Implemented

1. **Multi-Stage Build**
   - Separate build stage for dependencies
   - Final stage with only necessary artifacts
   - Reduced final image size by excluding build tools

2. **Security Measures**
   - Non-root user (appuser) with minimal privileges
   - Custom security group (appgroup)
   - Proper file ownership with --chown
   - No sensitive data in image layers
   - Minimal base image (Alpine Linux)

3. **Build Optimization**
   - Layer caching with requirements.txt
   - .dockerignore for minimal context
   - Virtual build dependencies (.build-deps)
   - No-cache-dir for pip to reduce size
   - Proper ordering of layers (least to most frequently changed)

4. **Runtime Configuration**
   - Environment variables for Python and Flask
   - PYTHONDONTWRITEBYTECODE to prevent .pyc files
   - PYTHONUNBUFFERED for proper logging
   - Explicit port exposure (5000)
   - Container health check implementation

5. **File Management**
   - Proper WORKDIR usage
   - Selective file copying
   - Correct file permissions
   - Efficient layer ordering
   - Proper path configuration

6. **Base Image Selection**
   - Official Python Alpine image
   - Specific version pinning (3.11-alpine)
   - Minimal footprint
   - Regular security updates

## Building and Running

1. Build the image locally:

   ```bash
   docker build -t eleanorpi/moscow-time-app .
   ```

2. Pull from Docker Hub:

   ```bash
   docker pull eleanorpi/moscow-time-app
   ```

3. Run the container:

   ```bash
   docker run -d -p 5000:5000 --name moscow-time eleanorpi/moscow-time-app
   ```

4. Check container health:

   ```bash
   docker inspect --format='{{json .State.Health}}' moscow-time
   ```

5. Access the application:

   ```bash
   http://localhost:5000
   ```

## Image Size and Security

- Final image size is optimized through multi-stage build
- No unnecessary build tools in final image
- Non-root user for security
- Regular security updates via base image
- Health checks for monitoring
