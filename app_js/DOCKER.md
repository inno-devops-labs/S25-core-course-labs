# Docker Integraion

## Best practices used

- **Slim Node Image**: Reduces size & attack surface (node:20-slim).
- **Layer Caching**: package*.json copied first for efficient builds.
- **Environment Variables**: Configured via .env and run.sh.
- **Graceful Shutdown**: entrypoint.sh catches SIGINT for clean shutdown.
- **Dynamic Volume Binding**: source files are mounted only in DEV mode.
- **No root user**: less risk of an attack when container is compromised.
