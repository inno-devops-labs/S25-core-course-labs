## Followed best practices
- Uses a precise version of docker base image. In my case "python:3.13-alpine"
- Unnecessary files are ignored via dockerignore
- Number of layers is minimized
- Separate stages for local development and production
- Minimized release image sized
- No root user. Access to source code is restricted
- Dockerfile is checked with linter hadolint