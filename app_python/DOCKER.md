
---


# Docker Best Practices that Applied here:

1. **Non-Root User**  
   Created a dedicated user `appuser` to avoid running as root.

2. **Multi-Stage Build**  
   Separated build and runtime stages to reduce final image size.

3. **Layer Optimization**  
   Cached dependencies separately and copied only necessary files.

4. **Precise Base Image**  
   Used `python:3.9-slim` for a minimal and secure base.

5. **.dockerignore**  
   Excluded development files like `venv` and `.git`.

6. **Explicit Versioning**  
   Pinned Python and dependency versions for reproducibility.

7. **Minimal Permissions**  
   Used `chown` to restrict file ownership to `appuser`.