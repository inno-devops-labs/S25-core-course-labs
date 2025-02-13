# Docker image report

## Best practices

- Multi-stage build to omit having node.js and node_modules after the static site has been built
- Versioned images are better for security and reproducibility.
- App file copied after requirements to avoid reinstalling dependencies on every layer change.
- Non-root user is used to avoid potential security issues.
- Official image is used
- Buildx cache (buildx required) is used for npm to speed up the installation even if the previous layers have been changed
