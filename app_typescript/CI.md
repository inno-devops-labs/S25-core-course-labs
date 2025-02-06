# CI best practices implemented in the repo

- Status checks are enforced on the default branch
- Matrix of Node versions and are tested
- Docker credentials are saved as env / secrets in the repo settings
- Docker buildcache (layers are pushed to a separate tag in Docker Hub) and npm cache (enabled in the CI setup-node action) are making the CI workflow faster and more efficient.
- lockfile-defined dependency installation is used to rule out the flaky npm install process