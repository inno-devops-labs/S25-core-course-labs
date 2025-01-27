# app_rust

## Docker Best Practices

1. **Multi-Stage Build**
   Used a multi-stage build to compile the application in the first stage and use a minimal runtime image for the final container

2. **Rootless Container**
   Created a non-root user (`appuser`) to run the application securely.

3. **Precise Base Images**
   - Builder: `rust:1.84-slim-bullseye`
   - Runtime: `debian:bullseye-slim`

4. **Minimized Image Size**
   Used only the compiled binary in the final image.

5. **Layer Optimization**
   - Grouped related commands in the build stage.
   - Used `.dockerignore` to reduce the build context.

6. **Explicit Port Exposure**
