# Docker Documentation (app_js)

This document explains how we containerized the Node.js application for the **Bonus Task**, focusing on multi-stage builds and Distroless images.

---

## Docker Best Practices

1. **Rootless Container**  
   - We create a non-root user (`myuser`) in our standard Dockerfile.
   - For Distroless, we use the `nonroot` variant from GoogleContainerTools.

2. **Precise Base Images**  
   - For the standard build, we use `node:18.16.0-alpine3.15`.
   - For the Distroless build, we use `gcr.io/distroless/nodejs18:nonroot`.

3. **Layer Efficiency**  
   - We copy only necessary files in the correct order.
   - We install dependencies in one stage, then copy them to the final image (multi-stage).

4. **.dockerignore**  
   - We exclude files like `node_modules`, `.git`, etc. to reduce build context and final image size.

5. **COPY Only Specific Files**  
   - We explicitly copy `package.json` and `server.js` instead of copying the entire folder.

6. **No Root**  
   - In the standard Dockerfile, we switch to a `myuser` user.
   - In the Distroless version, `:nonroot` ensures the container does not run as root.

---

## Multi-Stage Builds and Distroless

We implemented a multi-stage build in the `distroless.Dockerfile`:
1. **Stage 1** uses the Alpine-based Node image to install dependencies.
2. **Stage 2** uses the Distroless Node.js image (`nodejs18:nonroot`).

## Image Size Comparison

| Image |  Approx Size |
|:-|-------------:|
| js-app:latest |       ~80 MB |
| js-app:distroless |    ~50-60 MB |

