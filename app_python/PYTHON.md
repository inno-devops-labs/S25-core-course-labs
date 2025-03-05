# Lab 1

## Framework choice

FastAPI was choosen because it is one of the fastest framework, it is easy to use and has high perfomance.

## Best practices applied in the web application

* Proper code naming
* Logging
* Error hadling
* Code reusability

## Coding standarts

* Code adheres to PEP 8 standarts. This has been checked with ``flake8``.

## Test

To be sure that the displayed time is updated when the page is refreshed, the web application was manually tested.

## Unit Testing for Moscow Time API

### Best Practices Applied

The following best practices were followed while writing unit tests for the Moscow Time API:

* **Test Independence**: Each test runs independently and does not rely on the state of others.
* **Descriptive Test Names & Docstrings**: Each test function has a meaningful name and description.
* **Edge Case Testing**: Tests cover normal and edge cases, such as incorrect HTTP methods and simulated internal errors.
* **Regex-Based Validation**: Used regular expressions to extract and validate the time format from HTML.
* **Mocking with `monkeypatch`**: Simulated server errors to ensure robust error handling.
* **Consistent HTTP Status Checks**: Ensured correct response codes for valid and invalid requests.

### Unit Tests Implemented

| **Test**                     | **Description** |
|------------------------------|----------------|
| `test_get_moscow_time`       | Ensures that the `/` endpoint returns a valid HTML response with a title and time. |
| `test_moscow_time_format`    | Validates that the extracted time follows the `HH:MM:SS` format. |
| `test_unsupported_methods`   | Checks if `POST`, `PUT`, and `DELETE` return `405 Method Not Allowed`. |
| `test_internal_server_error` | Simulates an internal server error and ensures a `500` response is returned. |

### Running Tests

To run all unit tests, use the following command from the app_pyrthon folder:

```bash
    pytest tests/
```
