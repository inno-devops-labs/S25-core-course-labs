# Moscow Time Web App

## Best practices

- **Caching**: cache pythons dependencies.

 ```yml
with:
  python-version: '3.12'
  cache: 'pip'
 ```

- **Running CI only when needed**: trigger CI only when specified directory is changed.

 ```yml
on:
  push:
    paths:
      - 'app_python/**'
      - '.github/workflows/app_python.yml'
    branches:
      - '**'
  pull_request:
    paths:
      - 'app_python/**'
      - '.github/workflows/app_python.yml'
 ```

- **Code linting and testingh**: use `unittest` and `flake` to ensure maintainable code.
- **Security scan**: user `Snyk` tolook for vulnerabilities in the code.
