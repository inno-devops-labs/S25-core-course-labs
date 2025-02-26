# CI Workflow Best Practices

1. **Workflow Efficiency**: Job Matrix for Parallel Execution

    - Jobs (`build-and-test`, `docker`) run independently to improve efficiency.
    - Reduces waiting time between tasks.

2. **Dependency Caching**:

    - Uses **GitHub Actions Cache** to store Python dependencies.
    - This prevents re-downloading the same packages in every workflow run.
    - Applied using:

    ```yaml
    uses: actions/cache@v3
    with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('app_python/requirements.txt') }}
    ```
