# Best practices

1. Using minimalistic image:
    - Use `python:3.13-slim` as base image.
2. Use `.dockerignore` to exclude files from build.
3. Often rebuilding image:
    - Use `docker build --no-cache -t <name> .` to build image.
    - Use `pip install --no-cache-dir --upgrade pip` to upgrade pip.
    - Use `pip install --no-cache-dir -r requirements.txt` to install dependencies.
4. Ephemeral container:
    - It has only zone setting file. Otherthings do not require to tune sattings.
5. Avoiding using unnecessary packages:
    -I install only packages, which was obtained by usind `pip freeze` command during the clean building.
6. Caching (layer saving)
    - I use immutable layers in the beginning. Mutable layers are closer to the end.
7. Decouple applications:
    - It is atomic container with one application.
8. Pin base image versions:
    - Use base image's hash on `FROM` stage.
