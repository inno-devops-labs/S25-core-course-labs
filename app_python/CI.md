# CI Pipeline

## Best Practices

1. Branch and Path-Based Triggers

   The workflow runs only when files in app_python/ or the workflow itself change, preventing unnecessary runs.

2. Separate Stages for Better Modularity

    The CI pipeline is split into dependencies, lint, run, test, and docker stages, ensuring clear separation of concerns.

3. Job Run Reduction

    Each job only runs when its dependencies are met, avoiding redundant work and improving efficiency.

4. Fail Fast on Linting Errors

    The pipeline stops immediately if linting fails, ensuring that no further steps run with improperly formatted code.

5. Detached Mode

    Using nohup pipeline runs containers in deatached mode for stability.

6. Virtual Environment Caching

   Python virtual environment (venv) is cached and restored across jobs. This prevents redundant dependency installation, reducing execution time.

7. Efficient Docker Caching

   The pipeline uses cache-from and cache-to in Docker builds to speed up image creation.
