# Docker best practices applied
### <i><a href='https://docs.docker.com/build/building/best-practices/#exclude-with-dockerignore'>Source</a></i>
- **Exclude with `.dockerignore`** - to exclude files not relevant to the build.
- **Choose the right base image** - I have chosen minimal base image that matches my requirements.
- **Use COPY only to specific files.**
- **Rootless mode** - it allows running the Docker with nonroot user to avoid potential vulnerabilities.
