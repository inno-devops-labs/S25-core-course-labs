# Continuous integration documentation

## CI workflow overview

Our CI workflow consists of three main jobs:

### 1. Test job

- Runs unit tests and linting
- Uses Python 3.8 with dependency caching

### 2. Docker job

- Builds and pushes Docker image
- Uses layer caching for efficiency

### 3. Security job

- Runs Snyk vulnerability scanning
- Checks for high-severity issues

## Best practices implemented

1. **Build cache optimization**
   - **Python dependencies cache**
     - Uses GitHub Actions built-in pip caching
     - Speeds up dependency installation
     - Automatically invalidated when requirements.txt changes

   - **Docker layer cache**
     - Stores layers in Docker Hub with buildcache tag
     - Optimizes build time for subsequent runs
     - Preserves layer cache between workflow runs

2. **Workflow efficiency**
   - Dependency and layer caching
   - Path-based triggering
   - Parallel execution where possible
   - Optimized job dependencies

3. **Quality & security**
   - Automated testing and linting
   - Code coverage tracking
   - Vulnerability scanning
   - Secure secrets management

## Required secrets

- `DOCKERHUB_USERNAME`: Docker Hub username
- `DOCKERHUB_TOKEN`: Docker Hub access token  
- `SNYK_TOKEN`: Snyk API token
