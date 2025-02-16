# Docker

Best practices used in Dockerfile:

- Rootless container: user that starts the app is `webApp`;
- Used renown base image: python;
- Written .dockerignore;
- Linted by `hadolint`;
- Specified exposed port: 5000.
