# Continuous Integration for Flutter Yekaterinburg Time Web App

Continuous Integration (CI) for the project is established via GitHub actions.
Check ~/.github/worflows/flutter.yml for the source code

## Best practices

- **Efficient source code changes trigger**: pipeline will trigger an updates
  only when changes occur in the source code of an app (~/app_dart/)
  or in the source code of the workflow (~/.github/worflows/flutter.yml)

- **Branch safety**: to ensure that CI has access to the code but in the same time
  steps that runner will perform will not affect the source code in the branch,
  *checkout* step is performed from the target branch

- **Dependencies cache**: Flutter setup with all dependencies
  is cached to optimize the build time

- **Linter**: linter and code analysis is performed via `flutter analyze`
  to check the consistency of the code style to dart formatting

- **Secrets management**: secrets (DockerHub) and environmental variables (Flutter version)
  are managed via GitHub Actions. See the documentation on the setup
  [here](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)

- **External services**:
    * [DockerHub](https://hub.docker.com/repository/docker/paranid5/app_flutter/general) is used to publish actual Docker image.

**Note on Snyk:** Snyk does not support Dart language and Flutter applications.
