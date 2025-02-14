# Best practices

1. Using minimalistic image:
2. Use `.dockerignore` to exclude files from build.
3. Often rebuilding image:
4. Ephemeral container:
    - It has only zone setting file. Otherthings do not require to tune sattings.
5. Avoiding using unnecessary packages:
6. Caching (layer saving)
    - I use immutable layers in the beginning. Mutable layers are closer to the end.
7. Decouple applications:
    - It is atomic container with one application.
8. Pin base image versions:
    - Use base image's hash on `FROM` stage.
