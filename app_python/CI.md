# CI/CD


### Best practices
* **Caching**: used to speed up building (installation) part
* **Parallel computations**: `lint`, `test`, `docker` stages
are performed in parallel after `install` stage was completed


#### Cache
Using this command, 
