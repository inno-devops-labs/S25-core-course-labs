# Continuous Integration for Python Moscow Time Web App

Continuous Integration (CI) for the project is established via GitHub actions.
Check ~/.github/worflows/python.yml for the source code

## Best practices

- **Efficient source code changes trigger**: pipeline will trigger an updates
  only when changes occur in the source code of an app (~/app_python/)
  or in the source code of the workflow (~/.github/worflows/python.yml)

- **Branch safety**: to ensure that CI has access to the code but in the same time
  steps that runner will perform will not affect the source code in the branch,
  *checkout* step is performed from the target branch

- **Dependencies cache**: dependencies are cached to optimize the build time

- **Linter**: linter checks via [flake8](https://flake8.pycqa.org/en/latest/) are performed
  to check the consistency of the code style to pep8

- **Secrets management**: secrets for external services (DockerHub, Snyk) are managed via GitHub Actions.
  See the documentation on the setup
  [here](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)

- **External services**:
    * [DockerHub](https://hub.docker.com/repository/docker/paranid5/app_piton/general) is used to publish actual Docker image.
    * [Snyk](https://app.snyk.io) is used to indentify known vulnerabilities in the current dependencies of the project.