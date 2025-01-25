# Best practices

## Elaborate on the best practices you employed within your Dockerfile

### Chose the right base image

The base image python:3.11-slim-bullseye is minimal and officially maintained, which reduces the image size.

### Used non-root user

The Dockerfile follows the principle of running applications as a non-root user, which improves security by minimizing the impact of potential vulnerabilities.

### Layer sanity

The things that changes rarely are upper in the Dockerfile and the things that changes frequently are lower.

### Excluded with .dockerignore

To exclude files not relevant to the build, without restructuring your source repository, used a .dockerignore file.

### Didn't install unnecessary packages

In the Dockerfile there are requirements, that install all necessary packages and nothing else.
