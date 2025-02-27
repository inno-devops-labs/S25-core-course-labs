# CI Best Practices
- **Caching**: Pip dependencies are cached to speed up workflows.

- **Isolated Jobs**: Build and Docker steps are separated.

- **Security**: Docker credentials stored as GitHub Secrets.

- **Linting**: Enforced code style with `flake8`.