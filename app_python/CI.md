# CI Best Practices for Moscow Time Web Application

## 1. **Using Cache for Dependencies**
   - **Why it's beneficial**: By caching pip dependencies (`~/.cache/pip`), we avoid reinstalling the same dependencies for every workflow run, which speeds up the build process.
   - **How it's done**: We use the `actions/cache@v2` GitHub Action to cache dependencies based on the `requirements.txt` file’s hash.
   
   ```yaml
   - name: Cache pip dependencies
     uses: actions/cache@v2
     with:
       path: ~/.cache/pip
       key: ${{ runner.os }}-pip-${{ hashFiles('app_python/requirements.txt') }}
       restore-keys: |
         ${{ runner.os }}-pip-
   ```

## 2. **Failing Fast**
   - **Why it's beneficial**: This ensures that the CI process doesn’t waste resources running further steps if critical errors are found early (e.g., linting or tests).
   - **How it's done**: The workflow structure ensures that linting and tests are run before Docker steps. If any step fails, the workflow stops immediately.

## 3. **Lint Only Relevant Files**
   - **Why it's beneficial**: Running `flake8` on the entire repository can be time-consuming. We run `flake8` on the Python files that are relevant and changed in the repository to save time.
   - **How it's done**: The linting is run on the `app_python` directory to check for issues in Python code.

## 4. **Job Dependencies**
   - **Why it's beneficial**: We ensure that jobs are executed in a defined order (dependencies). For example, Docker-related tasks should only run if tests pass.
   - **How it's done**: The `needs` key ensures that the `docker` job only runs after the `test` job has passed.
