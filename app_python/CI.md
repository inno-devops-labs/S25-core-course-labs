## CI Best Practices
- **Caching**: Reuse pip dependencies to speed up workflows.
- **Security**: Use secrets for Docker Hub and Snyk tokens.
- **Modular Jobs**: Split into `build-test` and `docker-publish` for clarity.