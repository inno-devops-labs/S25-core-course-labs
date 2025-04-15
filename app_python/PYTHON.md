# Platform selection: FastAPI

## Why FastAPI?
1. **Performance**: FastAPI surpasses all Python frameworks in performance (according to TechEmpower).
2. **Asynchronous Support**: FastAPI natively supports asynchronous programming, which is ideal for modern web applications.
3. **Automatic Documentation**: FastAPI automatically generates interactive API documentation (Swagger), which simplifies API testing and sharing.
4. **Ease of Use**: FastAPI is easy to set up, making it ideal for small projects

## Best Practices Applied
- **Coding Standards and Testing**: The code follows PEP 8 guidelines, ensuring readability.
- **Testing**: The application has been tested manually to ensure the time updates correctly upon page refreshing.
- **Dependency Management**: A `requirements.txt` file is used to manage dependencies.

## Unit Tests Description

In this project, unit tests were created to verify the basic functionality of the application. The tests are written using the `pytest` framework and the `TestClient' tool from `fastapi.testclient`.

### Basic tests:

1. **test_get_moscow_time**:
- Checks the correctness of the endpoint `/`, which returns the current time in Moscow.
- Make sure that the response contains the key `moscow_time'.
- Check that the value of `moscow_time` corresponds to the format `YYYY-MM-DD HH:MM:SS'.

2. **test_invalid_endpoint**:
- Checks the processing of requests to non-existent endpoints.
- Make sure that the server returns the status code `404' (Not Found).

3. **test_time_updates_on_reload**:
- Checks time updates after reloading the page.

## Best Testing Practices:
1. **Key Feature Coverage**: All the main features of the app are covered by tests.
2. **Edge case testing**: Tests take into account possible errors and incorrect input data.
3. **Automation**: Tests are integrated into the CI/CD pipeline, which ensures their execution at each push or pull request.

