# Docker Implementation Best Practices

## Docker Hub

The Docker image is available on Docker Hub:
- Repository: [sergeipolin/moscow-time](https://hub.docker.com/r/sergeipolin/moscow-time)

## Security Best Practices

1. **Non-root User**
   - Created a dedicated non-root user `appuser`
   - Application runs with limited privileges
   - Prevents potential security vulnerabilities

2. **Multi-stage Build**
   - Uses a builder stage for compilation and dependencies
   - Final image contains only necessary runtime components
   - Significantly reduces attack surface

## Image Optimization

1. **Base Image Selection**
   - Uses `python:3.11-slim-bullseye` for minimal footprint
   - Slim variant reduces image size while maintaining functionality
   - Specific version pinning for reproducibility

2. **Layer Optimization**
   - Requirements installed separately to leverage Docker cache
   - Only necessary files copied to final image
   - Proper ordering of layers for cache efficiency

3. **File Selection**
   - Implemented `.dockerignore` to exclude unnecessary files
   - Only production-required files are copied
   - Reduces build context size and final image size

## Runtime Configuration

1. **Environment Variables**
   - `PYTHONDONTWRITEBYTECODE=1`: Prevents Python from writing bytecode
   - `PYTHONUNBUFFERED=1`: Ensures Python output is sent straight to terminal
   - Proper PATH configuration for the non-root user

2. **Port Configuration**
   - Explicit port exposure (8000)
   - Clear documentation of network requirements

## Build and Runtime Optimization

1. **Dependency Management**
   - Dependencies installed with `--no-cache-dir` to reduce image size
   - Requirements file copied first to leverage build cache
   - System packages cleaned up after installation

2. **File System Organization**
   - Clear WORKDIR structure
   - Proper ownership and permissions
   - Organized file copying strategy

## Development Considerations

1. **Maintainability**
   - Clear, documented Dockerfile
   - Separation of build and runtime stages
   - Consistent naming conventions

2. **Reproducibility**
   - Specific version pinning
   - Deterministic build process
   - Documented build and run procedures 