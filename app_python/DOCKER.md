# Docker Best Practices

1. **Rootless Container**

   - Created a non-root user (`appuser`) and switched to it with `USER` in the Dockerfile. This enhances security by preventing the application from running as `root`.

2. **Pinned Base Image**

   - Used `python:3.10-alpine3.15` to ensure a specific Alpine and Python version, improving consistency.

3. **Multi-Stage Build**

   - We separate build dependencies (Stage 1) from final runtime (Stage 2). This reduces the final image size and attack surface.

4. **Layer Caching**

   - Copied and installed `requirements.txt` separately so Docker can cache dependencies, leading to faster rebuilds.

5. **.dockerignore Usage**

   - Excludes files like `.git`, `__pycache__`, local `.env`, and documentation. Prevents unnecessary bloat.

6. **Minimal Base Image**

   - Alpine-based images are lighter than standard Debian/Ubuntu images.

7. **Use of COPY Instead of ADD**

   - `COPY` is more explicit and recommended unless you need `ADD`’s specific features (like auto-unpacking tar files or fetching remote URLs).

8. **No Root User**

   - We explicitly avoid running as `root` inside the container. A container run as root can pose security risks.

9. **Docker Linter**
   - (Optional) We used [Hadolint](https://github.com/hadolint/hadolint) or a similar Dockerfile linter to check for best practices.

Feel free to add more best practices you’ve applied or discovered.
