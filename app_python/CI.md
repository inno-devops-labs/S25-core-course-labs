# CI workflow

## Best practices applied

- Build cache is utilized so the workflow efficiency is enhanced

- All information that may change and secrets are stored in the GitHub environment to ensure their safety and maintainability of the GitHub Actions workflow

- All actions have a specific version specified to avoid breaking changes, which possibly would crash the pipeline

- The matrix strategy is used to ensure that the application will pass tests successfully on every popular platform

- The needs keyword is used wisely: the Docker stage is blocked until the linter and tests are run successfully, so the code that does not pass the test would not break into the latest Docker app image

- If a key job fails, the workflow is marked as failed as soon as possible

- The workflow may be cancelled in progress if a new push occurs to save the build minutes of GitHub Actions

- Added vulnerability check using [Snyk](https://snyk.io/)
