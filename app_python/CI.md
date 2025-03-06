# Continuous Integration

## 1. Job dependencies

I've set up job dependencies to run some of them (e.g. Snyk checks)
only if necessary ones (test, lint) pass.
Also, no need to push image to Docker Hub if tests do not pass.

## 2. Fixed Actions versions

I've set up fixed versions of Actions and Python
to make pipeline more stable in the future.

## 3. Run on demand

Jobs for Python application will run only if Python app
source code updated or the workflow itself.

## 4. Caching

I'm using PIP dependencies caching to speed up repeated workflow execution.
The same is applied to Docker build action.

## 5. GitHub secrets

I do not reveal any secret tokens in source code or workflow because
I have inherited them in GitHub Actions settings.

## 6. Snyk vulnerabilities check

I use Snyk action to check vulnerabilities in my code
and its dependencies.

## 7. Multi-platform Docker image building

With GitHub Actions it is convenient to build a Docker image for multiple target platforms.
I did it in the corresponding action.
