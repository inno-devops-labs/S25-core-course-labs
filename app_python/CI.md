# CI best practices implemented in the repo

- Status checks are enforced on the default branch
- Matrix of Python versions and OSes are tested. For example, this way I discovered that my code doesn't work on Windows. Realistically nobody is going to host this app on Windows, but now I know there's an issue with ZoneInfo on that platform.
- Docker credentials are saved as env / secrets in the repo settings
- Docker buildcache (layers are pushed to a separate tag in Docker Hub) and pip cache (enabled in the CI setup-python action) are making the CI workflow faster and more efficient.
