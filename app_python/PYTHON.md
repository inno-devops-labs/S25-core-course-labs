# Python Web Application - Moscow Time Display

## Framework Choice: FastAPI

FastAPI was chosen as the web framework for this application for several key reasons:

1. **Performance**: FastAPI is one of the fastest Python web frameworks available, built on top of Starlette and Pydantic.
2. **Modern Features**: Built-in support for async/await, type hints, and automatic API documentation.
3. **Developer Experience**: Excellent documentation, intuitive API design, and minimal boilerplate code.
4. **Scalability**: Easy to scale and maintain as the application grows.
5. **Built-in OpenAPI Support**: Automatic interactive API documentation (Swagger UI).

## Best Practices Applied

### 1. Code Organization and Structure

- **Separation of Concerns**: Configuration, routes, and templates are separated into distinct modules
- **Settings Management**: Using `pydantic-settings` for type-safe configuration
- **Environment Variables**: Sensitive data and configuration managed through `.env` files
- **Template Organization**: HTML templates stored in a dedicated `templates` directory

### 2. Code Quality and Standards

- **Type Hints**: Comprehensive use of Python type annotations for better code clarity and IDE support
- **Docstrings**: Detailed documentation for functions and endpoints following Google style
- **Error Handling**: Proper exception handling with meaningful error messages
- **Async/Await**: Efficient handling of concurrent requests using FastAPI's async capabilities

### 3. Frontend Best Practices

- **Responsive Design**: Mobile-friendly layout using flexbox
- **User Experience**: Clean, intuitive interface with visual feedback
- **Performance**: Client-side updates using fetch API to minimize server load
- **Accessibility**: Semantic HTML and proper contrast ratios

### 4. Security Considerations

- **CORS Protection**: Built-in CORS middleware configuration
- **Environment Variables**: Sensitive configuration stored in `.env` file
- **Input Validation**: Automatic request validation using Pydantic models
- **Error Handling**: Safe error responses without exposing internal details

### 5. Testing and Quality Assurance

- **Type Checking**: Static type checking with Python's type hints
- **Error Scenarios**: Comprehensive error handling and edge cases
- **Code Style**: Adherence to PEP 8 standards

## Development Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python main.py
```

4. Access the application:

- Web Interface: <http://localhost:8000>
- API Documentation: <http://localhost:8000/docs>

## Code Quality Tools

The project uses several tools to maintain code quality:

1. **Type Checking**:
   - mypy for static type checking
   - Pydantic for runtime type validation

2. **Code Style**:
   - Black for code formatting
   - isort for import sorting
   - flake8 for style guide enforcement

# Python Application Testing Documentation

## Testing Strategy

Our application implements comprehensive testing using pytest as the primary testing framework. The testing strategy follows these best practices:

### Unit Tests
Located in the `tests/` directory, our unit tests cover:

1. **Core Functionality Tests**
   - Time formatting and timezone handling
   - Data type and structure validation
   - Error handling and edge cases

2. **API Endpoint Tests**
   - Response status codes
   - Response content validation
   - Content-type headers
   - Async functionality

3. **Configuration Tests**
   - Timezone validity
   - Settings validation

### Test Coverage
We use pytest-cov to maintain high test coverage:
- All core functions are tested
- Edge cases and error conditions are verified
- Async operations are properly tested
- HTML template rendering is validated

### Best Practices Applied
1. **Test Organization**
   - Clear test file structure
   - Descriptive test names
   - Comprehensive docstrings
   - Isolated test cases

2. **Code Quality**
   - Flake8 for linting
   - Coverage reporting
   - Async testing support
   - Proper test isolation

3. **CI Integration**
   - Automated testing in CI pipeline
   - Coverage reporting in CI
   - Linting checks
   - Docker build verification

## Running Tests

To run the tests locally:

```bash
# Install test dependencies
pip install -r requirements.txt

# Run tests with coverage
pytest --cov=.

# Run specific test file
pytest tests/test_main.py

# Run with verbose output
pytest -v
```

## Test Configuration

The `pytest.ini` file configures:
- Test discovery patterns
- Coverage reporting
- Async test mode
- Verbose output

## Continuous Integration

Tests are automatically run in GitHub Actions:
1. On every push to branch
2. On pull requests
3. Before Docker image builds
