# Continuous Integration Best Practices

## 1. Workflow Status Badge

There was added a badge to monitor the CI state.

## 2. CI workflow optimization

- `lint` and `test` stages are set to work in parallel.
- `docker` is built only after successfull test pass.

## 3. Automated security testing

There was added SNYK security check stage to the CI to be checked after each push to remote repository.
