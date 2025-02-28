# Python Web Application - Moscow Time Display

## Framework Choice: FastAPI

FastAPI was chosen for this project for several reasons:

1. **Performance**: FastAPI is one of the fastest Python web frameworks available, based on Starlette and Pydantic.

2. **Modern Features**: Built on Python 3.6+ type hints, providing excellent editor support and automatic validation.

3. **Easy to Learn**: Simple and intuitive API design makes it perfect for both small and large applications.

4. **Automatic API Documentation**: Provides Swagger UI and ReDoc out of the box.

5. **Async Support**: Built-in support for async/await syntax, making it efficient for I/O operations.

## Best Practices Applied

1. **Error Handling**: Implemented proper exception handling with try-catch blocks.
2. **Type Hints**: Used Python type hints for better code clarity and IDE support.
3. **Clean Code**: Followed PEP 8 style guide for Python code.
4. **Separation of Concerns**: Structured HTML and styling separately from the Python logic.

## Testing Strategy and Best Practices

### Unit Tests Implementation

1. **Test Structure**

   - Organized tests in dedicated `/tests` directory
   - Used pytest as the testing framework
   - Implemented TestClient for FastAPI endpoint testing

2. **Test Coverage**

   - Main endpoint functionality testing
   - Response format validation
   - Template rendering verification
   - Error handling scenarios

3. **Best Practices Applied**

   - Isolated test cases
   - Clear test naming conventions
   - Proper assertion messages
   - Mock-free timezone testing
   - Comprehensive HTTP response testing

4. **Running Tests**

   ```bash
   pytest
   # With coverage report
   pytest --cov=. tests/
   ```

### Testing Best Practices

1. **Isolation**

   - Each test is independent
   - No shared state between tests

2. **Naming Conventions**

   - Descriptive test names
   - Clear purpose indication
   - Consistent naming pattern

3. **Assertions**

   - Specific assertions
   - Clear failure messages
   - Multiple validation points

4. **Coverage**
   - Core functionality coverage
   - Edge case testing
   - Error scenario validation
