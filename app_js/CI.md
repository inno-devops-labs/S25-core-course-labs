# CI/CD
*for Node.js*

### Best practices
* **Caching**: used to speed up building and installation parts
(applied for the `install` and `docker` stages)
* **Parallel computations**: `lint`, `test`, `snyk` stages
are performed in parallel after `install` stage was completed
* **Security**: I set secret variables related to 
DockerHub account and the api key to the Git repo.
* **Snyk**: was applied


### Snyk
Snyk was successfully integrated and applied. No vulnerabilities
were found. It helps to prevent app from using vulnerable
dependencies. Snyk token was stored as a secret at the repo.

### Two workflows
`js.yml` runs only when changes in app_js folder occur, 
`py.yml` - only when in app_py folder. It is achieved simply
by defining `paths` in `on` part of each workflow file.
