# Best practices for CI/CD

I have implemented these best practices:

- Commit frequently
  As can be seen by the history of commits, I have commited
  a lot of times specifically to get feedback on my changes
- Optimize pipeline stages
  The main bottlenecks in the pipelines are interactions with
  outside services such as DockerHub and Snyk. The main building
  and testing job gets done in just 10 seconds, while the other
  two still take less than 25 seconds.
- Build code artifacts once
  As Python is an interpreted language, it is infeasible to
  build some executable before using it in several places. Moreover,
  two of the jobs require access to the source code so only building
  the Docker image is doing any compilation work, and it is doing it
  only once.
- Automate tests
  The CI workflow has 2 dedicated jobs for testing: one with our own
  unit tests, and the other for 3rd party security testing using Snyk.
- Keep builds fast and simple
  As I said above, the builds are very fast, not even taking half a minute
  to finish
- Take a security-first approach
  One of the jobs in the workflow uses Snyk to test the app for
  vulnerabilities. I have found no vulnerabilities this way, but it must
  be worth something.
