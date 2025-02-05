# Justification for Framework Choice

I selected **Flask** as the framework for this web application because:

- **Lightweight and Simple:** Flask is minimalistic and easy to use, which aligns with the simplicity required for this task.
- **Flexible:** It doesn't enforce a particular project layout or dependencies, giving more control over the components.
- **Popularity:** Flask is a popular framework so it has detailed documentation and also making it easier to find resources.

## Best Practices Applied: Flask

- **Virtual Environment:** Used a virtual environment to manage project dependencies.
- **Code Readability:** Followed PEP 8 coding standards for Python code style.
- **Modularity:** Kept the code modular for scalability.
- **Dependencies** Use of concise requirements.txt file for required dependencies with specified versions.
- **Error Handling:** Basic error handling is implicitly managed by Flask for undefined routes.

## Testing and Code Quality

- **Manual Testing:** Tested the application by running it locally and refreshing the page multiple times.
- **Code Quality:** Used coding guidelines and thoroughly tested my implementation to ensure the code quality.

## Unit Tests

I have implemented unit tests using `pytest` to ensure the application's reliability and correctness.

### Tests Implemented

- **test_index_status_code**: Ensures that the home page (`/`) returns an HTTP 200 status code.
- **test_index_content**: Checks that the phrase "Current Time in Moscow" is present in the response, confirming that the page loads correctly.

### Best Practices Applied: Unit tests

- **Test Coverage**: Focused on critical parts of the application.
- **Isolated Tests**: Each test runs independently using `pytest` fixtures.
- **Meaningful Names**: Test functions are named to reflect their purpose clearly.
- **Reusable Fixtures**: Used fixtures to avoid repetition and set up a consistent testing environment.
