# Python Web Application

## Tech Stack

* Python
* FastApi, as it's most used Python Framework
for backend nowadays and has all needed functionalities.

## Best practises

* I have followed KISS principle which is the most suitable for such simple apps.
* I have configured project using [poetry](https://python-poetry.org/)
* I have configured `pre-commit` hooks (see [.pre-commit-config.yaml](.pre-commit-config.yaml))
* I have configured static type checking using [mypy](https://mypy-lang.org/)
* I have configured code formatting
  with [pylint](https://www.pylint.org/), [black](https://black.readthedocs.io/en/stable/#),
  and [isort](https://pycqa.github.io/isort/)
* I have configured [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli)
for formatting markdown files.

## Testing

### Tests Created

#### `test_root_endpoint()`
- **Purpose**: Validate root endpoint ("/") functionality
- **Checks performed**:
  - Successful HTTP response (status code 200)
  - Correct HTML content type
  - Accurate time representation

#### `test_static_files_served()`
- **Purpose**: Verify static file serving mechanism
- **Checks performed**:
  - Confirm static files can be accessed
  - Handle potential absence of static files

#### `test_templates_configured()`
- **Purpose**: Ensure Jinja2 templates are correctly set up
- **Checks performed**:
  - Validate template directory configuration
  - Catch configuration errors

### Best Practices Applied

#### Testing Principles
- Comprehensive coverage of application features
- Isolation of individual components
- Minimal external dependencies
- Clear, descriptive test names

#### Testing Tools
- `pytest` for test framework
- `TestClient` for simulating HTTP requests
- Datetime manipulation for time-related tests

#### Recommendations
- Keep tests independent
- Use minimal setup and teardown
- Prioritize readability and maintainability