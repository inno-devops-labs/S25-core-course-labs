# CI/CD

### Best practices
* **Caching**: used to speed up building and installation parts
(applied for the `install` and `docker` stages)
* **Parallel computations**: `lint`, `test`, `snyk` stages
are performed in parallel after `install` stage was completed
* **Security**: I set secret variables related to 
DockerHub account to the Git repo.
* **Snyk**: was applied


### Snyk
Snyk was successfully integrated and applied. No vulnerabilities
were found. It helps to prevent app from using vulnerable
dependencies. Snyk token was stored as a secret at the repo.
