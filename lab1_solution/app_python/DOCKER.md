# Best practices

1. The use of `python:3.13.1-slim` minimizes the image size, which leads to faster downloads and improved security.

2. Setting environment variables like `PYTHONUNBUFFERED` and `PYTHONDONTWRITEBYTECODE` helps optimize Python's behavior in the container, improving performance and avoiding unnecessary bytecode files.

3. Combining commands into a single `RUN` statement helps reduce the number of layers in the final image, which can lead to a smaller image size.

4. Copying `requirements.txt` and installing dependencies before copying the application code takes advantage of Docker's caching mechanism. This way, dependencies are only reinstalled if the `requirements.txt` file changes.

5. Exposing port to indicate the used port

6. Switching to non-root user prevents privilege escalation

7. Using `--no-cache-dir` with `pip install` reduces the final image size by preventing pip from caching packages.
