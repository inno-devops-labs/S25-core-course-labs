# Moscow Time Web App

## Best practices

- **Running CI only when needed**: trigger CI only when specified directory is changed.

 ```yml
on:
  push:
    paths:
      - 'app_golang/**'
      - '.github/workflows/app_golang.yml'
    branches:
      - '**'
  pull_request:
    paths:
      - 'app_golang/**'
      - '.github/workflows/app_golang.yml'
 ```

- **Code linting and testingh**: use code test and linting to ensure maintainable code.
- **Security scan**: user `Snyk` to look for vulnerabilities in the code.
