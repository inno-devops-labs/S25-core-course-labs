# CI workflow

## Best practices applied

- All information that may change and secrets are stored in the GitHub environment to ensure their safety and maintainability of the GitHub Actions workflow

- Build cache is utilized so the workflow efficiency is enhanced

- The needs keyword is used wisely: the Docker stage is blocked until the linter and tests are run successfully, so the code that does not pass the test would not break into the latest Docker app image

- The workflow may be cancelled in progress if a new push occurs to save the build minutes of GitHub Actions

- If a key job fails, the workflow is marked as failed as soon as possible

- Added vulnerability check using [Snyk](https://snyk.io/)
