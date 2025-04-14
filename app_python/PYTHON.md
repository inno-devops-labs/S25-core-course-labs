# Python Web Application

## Framework choice

I chose the `Flask` framework because I have a little experience with it, and this framework is one of the most common frameworks.
`Flask` has all possible functionalities that can be used in web development.

## Best practices

- Code is well-commented and has documentation for further usage.
- Configured the `pre-commit` hooks (check the `.pre-commit-config.yaml` file).
  - The code is formatted by `black` formatter, linted by `pylint`, statically checked by `mypy`.
  - The `markdownlint` is used to check the documentation style.

## Testing

This application was tested using unit tests and the `pytest` library. There are 3 tests:

1. **Availability Test**: Verifies that the application is accessible by checking the HTTP status code of the page.
2. **HTML Structure Test**: Ensures that the page returns a valid HTML response containing the keyword "Moscow," indicating the page's proper structure.
3. **Time Display Test**: Verifies that the time displayed on the page is correct (excluding milliseconds) and matches the current Moscow time.

## Testing best practices

- **Write Isolated Tests**: each test is independent and does not rely on the state or results of another test. This isolation prevents flaky tests and makes debugging more reliable.

- **Avoid Infrastructure Dependencies**: tests decoupled from external systems such web-server.

- **Leverage Fixtures**: `pytest fixtures` is used to set up and tear down testing environments, ensuring consistency and reducing repetitive code.
