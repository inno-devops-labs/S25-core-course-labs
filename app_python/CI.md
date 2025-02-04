# CI best practices used

1. **Worflow triggers**. The pipeline only executes on pull-requests to the master branch and on pushes to the lab3 (
   feature) breanch.
2. **Dependencies caching**. The dependencies are cached to optimize the worflow efficiency.
3. **Automated linting**. The linter is automatically executes to check the code style.
4. **Security scanning**. Snyk security check is implemented to automatically scan for security issues.
5. **Secret management**. GitHub secrets are used to make store and use tokens safely.
6. **Automated testing**. The pipeline automatically runs tests make sure the application functions correctly.
