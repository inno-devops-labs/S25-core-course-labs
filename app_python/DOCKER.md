# Docker Integraion

## Best practices used

- **Slim Python Image**: Reduces size & attack surface (python:3.11-slim).
- **Layer Caching**: requirements.txt copied first for efficient builds.
- **Environment Variables**: Configured via .env and run.sh.
- **Graceful Shutdown**: entrypoint.sh catches SIGINT for clean shutdown.
- **Dynamic Volume Binding**: source files are mounted only in DEV mode.
- **No root user**: less risk of an attack when container is compromised.
