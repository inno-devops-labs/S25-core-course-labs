# CI Workflow

CI workflow created using GitHub Actions to build and test the project. The file `ci.yml` includes the following actions:

1. **Dependencies**:
   Install project dependencies.

2. **Linter**:
   Check code quality using `flake8` linter.

3. **Tests**:
   Automatically run unit tests.

4. **Docker**:
   Login, build and push a Docker image to DockerHub.

5. **Snyk Check**:
   Identify and address vulnerabilities of the project.

## Best Practices

1. **Caching**: Utilize build cache to enhance workflow efficiency.

2. **Parallel actions**: `build`, `synk-scan` and `docker` actions run in parallel after the `setup`.

3. **Security**: Login to DockerHub and Snyk managed with GitHub secrets and access tokens.

4. **Snyk**: Check the project for vulnerabilities.
