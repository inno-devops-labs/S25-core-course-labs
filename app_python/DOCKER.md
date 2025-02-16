# Why is this Dockerfile so amazing?

1. Non-root user - if I did everything correctly, the user is completely non-root, following **principle of least priveledge**.
2. File ownership with parts like `--chown=appuser:appuser` that ensures proper ownership.
3. Minimal and specific base image in `python:3.11-alpine3.18`, no `latest` tag.
4. Isolated dependencies
5. Layer ordering
6. Environment Configuration

## Distroless

Basically distroless version is a container stripped to it's bare minimum - no shell like `sh` or package manager like `apk`, 
and utilizes safety practices like running nonroot user by default. Through this minimalism it makes the surface of attack on 
the application almost non-existant and the image size itself smaller, but also way harder to work around it's features :).

For example this time app is **52.8MB** on distroless vs **77.3MB** on a regular image.

See `distroless.png` in static files for screenshot of the proof.
