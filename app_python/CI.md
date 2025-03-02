# Github CI best practices

## 1. Define timeouts for each job

Set time limits for every job to avoid scenarios where jobs run indefinitely 
due to configuration errors, deadlocks, or other issues.

## 2. Utilize actions with fixed Versions

Enhance the pipeline’s stability and security by using actions pinned to specific versions.

## 3. Use Github Secrets with restricted permissions

Ensure that secrets remain confidential by not exposing them. 
Additionally, grant only the necessary access rights.

## 4. Activate Workflows only when relevant files change

Avoid unnecessary workflow runs by configuring triggers 
to respond only to changes in specific directories or file types.

## 5. Job dependencies

Implement clear dependencies between jobs to optimize the workflow. 
For instance, if tests fail, prevent the pipeline 
from pushing a faulty image to Docker Hub, allowing the workflow to fail quickly.

## 6. Use caches

Use caching mechanisms, such as in the build_push job, 
to speed up the following pipeline executions by reusing previously built components.
