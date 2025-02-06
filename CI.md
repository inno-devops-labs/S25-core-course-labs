# Continuous Integration

This project uses GitHub Actions as the continuous integration platform. Whenever changes are pushed to any branch, the Actions workflow executes automatically.

Following best practices are applied:
1. **Workflow status badge**: README.md in coresponding `app_python` project displays status of main workflow that is reliable for building the project.
1. **Dependenc caching**: to speed up build process, dependencies are cached using the actions/cache action. By doing this, GitHub will save and restore dependencies from a cache instead of installing all of them from scratch with each build.
1. **Linter integration**: linter (flake8) is used to check the syntax and style of the code. This is beneficial because it helps to enforce certain styles and standards, resulting in code consistency and clarity.
1. **Running tests**: unit tests are run automatically in the CI pipeline. This way, new issues can be immediately detected when a new commit or pull request introduces errors.
1. **Dockerization**: application is packaged into a Docker image, allowing for greater mobility and environment consistency when the application is deployed or run in different environments.

