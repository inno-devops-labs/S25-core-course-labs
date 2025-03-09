# Docker Best Practices Implementation

1. **Alpine Base Image** - Uses minimal `python:3.11-alpine3.18`.
2. **Multi-Stage Build** - Separates build and runtime stages. Reduces final image size by separating build/runtime.
3. Copies requirements first for caching.
4. **.dockerignore File** - Excludes unnecessary files.
5. **Package Management** - Uses `--no-cache-dir` with pip.
6. **Timezone Support** - Installs `tzdata` package explicitly
7. **Non-Root User** - Enhances security by avoiding privileged operations.