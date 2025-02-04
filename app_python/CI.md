# CI Features

Let's dive deeply into all the optimizations and features I used during the CI configuration:

---

## `app_python`

### Common env variables

- It is useful to properly define the environments across the CI pipeline in the beginning.
  of the .yaml file in terms of laconic and easily reconfigurable

### Selectors

- Before jobs there are specified selectors on the triggers to run another pipeline.
  I set actions to start on PR (main, master branch) and changes in the source code/files..yaml

### Separating jobs

- Separated jobs for linting, testing, Snyk testing, and pushing the Docker image.
  in the GitHub registry

### Dependencies Cache

- The goal of dependency caching is to reduce the amount of time/space that can be consumed by the
  repeatable steps of environment configuration

### Snyk Actions

- My .yaml file was configured with the GitHub actions mostly, and to keep everywhere
  when possible, the same style, the `snyk-actions...` used (not manual snyk installation)

### Jobs dependency

- The build-push job mostly depended on the previous job. This was made to avoid
  building and pushing images that do not satisfy the common criteria: high code quality,
  correct functionality, no security vulnerabilities

### Docker cache

- This is a new feature for me, but we can get caches from the layer using the already
  pushed image to the registry. This is simply cool that we can use the cache from
  the remote place, and instantly use it in our current building process, without
  necessary need to rebuild something again. I also store the app_python_buildcache
  in the GitHub registry

---
