# Python Testing Guidelines

## Unit Tests

We use [pytest](https://docs.pytest.org/en/latest/) for unit testing our Flask application. The tests are located in the `tests/` directory.

### Test Details
- **Setup:** A `client` fixture initializes the Flask test client with `TESTING` configuration enabled.
- **Test Coverage:** The `test_show_time` function checks that the home route (`/`) returns a status code of 200 and the expected HTML content indicating the current time in Moscow.
- **Assertions:** We use assertions to validate the presence of the expected strings in the response data.

## Best Practices Applied
- **Isolation:** Each test runs in isolation to avoid dependencies on the order of execution.
- **Fixtures:** Using fixtures for setup and teardown ensures a clean testing environment.
- **Descriptive Naming:** Test names and docstrings describe the test intent and behavior.
