# Docker Best Practices for app_go

This document outlines the best practices employed within my Dockerfile for the `app_go` application. Following these practices ensures that my containerized application is efficient, secure, and easy to maintain.

## 1. Multi-Stage Builds

I utilize multi-stage builds to separate the build environment from the runtime environment. This approach reduces the final image size significantly by only including the necessary files in the final stage.

```Dockerfile
FROM golang:1.23 AS builder
FROM alpine:3.14
```

### 2. Use Minimal Base Images

In the first stage, I use a specific version of the Golang base image (golang:1.23) to ensure compatibility with our Go code. In the second stage, I use the minimal alpine:3.14 image to reduce the size of the final image.
```Dockerfile
FROM golang:1.23 AS builder
FROM alpine:3.14
```

### 3. Create Non-Root Users
Running applications as non-root users enhances security. I create a user named builder for the build stage and executor for the runtime stage.
```Dockerfile
RUN useradd --create-home builder
USER builder

RUN adduser -D -h /home/executor executor && \
    mkdir -p /home/executor && \
    chown executor:executor /home/executor
USER executor
```

### 4. Specify WORKDIR
Using WORKDIR sets the working directory inside the container, making subsequent commands relative to this path and ensuring consistency.
```Dockerfile
WORKDIR /home/builder
WORKDIR /home/executor
```

### 5. Copy Dependencies First
Copying go.mod before the source code allows Docker to leverage layer caching effectively. If only the code changes but not the dependencies, Docker will reuse the cached layer.
```Dockerfile
COPY go.mod .
COPY main.go .
```

### 6. Optimize Build Environment
I disable CGO and set the target OS and architecture explicitly during the build process to produce a statically linked binary, which does not depend on external libraries at runtime.
```Dockerfile
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -buildvcs=false -o go-binary
```

### 7. Minimize Image Size
By copying only the necessary files from the build stage to the final image, I minimize the size of the final image.
```Dockerfile
COPY --from=builder /home/builder/go-binary .
COPY ./templates ./templates
```

### 8. Set File Permissions
Ensuring that the executable has the correct permissions is crucial for running the application successfully.

```Dockerfile
RUN chmod +x ./go-binary
```

### 9. Expose Necessary Ports
Explicitly expose the port used by the application (8080) so it’s clear what ports need to be accessible externally.
```Dockerfile
EXPOSE 8080
```

### 10. Use CMD Correctly
The CMD instruction specifies the default command to run when the container starts. I use an array format to avoid shell interpretation issues.
```Dockerfile
CMD [ "./go-binary" ]
```
