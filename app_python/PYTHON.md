# Justification for Choosing Flask

I chose Flask for this project because it is a lightweight and flexible micro web framework for Python that is perfect for small apps like that one.

# Best Practices Applied in the Web Application

## Coding Standards
- **Flask Framework**: Used for clean, modular code.
- **PEP 8 Compliance**: Descriptive variable names and consistent formatting.
- **Separation of Concerns**: Backend logic isolated from frontend using templates.

## Testing and Verification
- **Manual Testing**:
  - Verified correct time display on page load.
  - Ensured local time updates every second without server requests.
  - Validated Moscow Time accuracy regardless of local machine settings.

## Code Quality
- **Performance**: Handled time updates locally with JavaScript to reduce server load.
- **Reliability**: Used `datetime` and `pytz` for accurate Moscow Time handling.
- **Security**: Debug mode for development only; no sensitive data exposed.

# Python Testing Documentation

## Testing Strategy

Our testing approach follows these key principles:

1. **Unit Testing**: Testing individual components in isolation
2. **Integration Testing**: Testing components working together
3. **Test Coverage**: Aiming for comprehensive test coverage
4. **Automated Testing**: Tests run automatically with CI/CD

## Test Structure

The tests are organized in the `tests` directory:
- `test_app.py`: Contains tests for the main Flask application
- Future test files will be added for additional components

## Running Tests

To run the tests:
```bash
python -m unittest discover tests
```

For coverage report:
```bash
coverage run -m unittest discover tests
coverage report
```

## Current Test Cases

### Flask Application Tests (`test_app.py`)

1. **Index Route Test**
   - Verifies the main route returns HTTP 200
   - Checks if response contains time data
   
2. **Moscow Time Format Test**
   - Validates correct time formatting
   - Ensures timezone handling is correct

## Best Practices Applied

1. **Test Isolation**
   - Each test runs independently
   - setUp and tearDown methods handle test environment

2. **Meaningful Assertions**
   - Clear, specific test assertions
   - Descriptive test names and docstrings

3. **Coverage Goals**
   - Aim for 80%+ code coverage
   - Test both success and error cases

4. **Clean Code Principles**
   - DRY (Don't Repeat Yourself)
   - Single Responsibility Principle
   - Clear naming conventions
