# CI best practices implemented in the repo

- Status checks are enforced on the default branch
  - GitHub doesn't mark path-filter skipped checks as successful (see [discussions](https://github.com/orgs/community/discussions/44490)), so I implemented a summary action that takes skipped checks as successful (`summary.yml`). This sounds like a potential cause of bugs, but I believe that it's a relatively safe solution until GitHub implements path filter in a way that would pass enforced status checks in the PRs.
- Matrix of Python versions and OSes are tested. For example, this way I discovered that my code doesn't work on Windows. Realistically nobody is going to host this app on Windows, but now I know there's an issue with ZoneInfo on that platform.
- Docker credentials are saved as env / secrets in the repo settings
- Docker buildcache (layers are pushed to a separate tag in Docker Hub) and pip cache (enabled in the CI setup-python action) are making the CI workflow faster and more efficient.
