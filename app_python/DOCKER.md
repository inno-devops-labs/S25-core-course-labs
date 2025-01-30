# Docker Best Practices Implemented

In this Dockerfile, I have implemented various Docker best practices to enhance the security and efficiency of my containerized application.

## Avoid Unnecessary Privileges

I've ensured that my container runs as a non-root user by creating a user 'nobody' and setting appropriate file system permissions. This improves security and compatibility with other platforms.

```

RUN mkdir /app && chown -R nobody /app
...
USER nobody

```

## Also some basic stuff

- Use official base image.
- Minimize number of layers.
- Use COPY instruction instead of ADD.
- Add comments in dockerfile to describe instructions.
- Use Dockerfile linter `hadolint`.
