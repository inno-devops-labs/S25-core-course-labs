# Python Web Application

## Framework Choice: FastAPI

FastAPI was chosen for following reasons:
- **High Performance**: FastAPI is one of the fastest Python web frameworks.
- **Asynchronous Support**: Native support for async/await.
- **Automatic Documentation**: Generates interactive API documentation automatically.

### Best Practices

1. **Modular Code**: The application is structured in a single file for simplicity, but it can be easily modularized.
2. **Error Handling**: FastAPI automatically handles validation errors and provides detailed error messages.
3. **Environment Variables**: For production, environment variables should be used for configuration (port, host).

## Unit Tests
The application includes comprehensive unit tests located in `test_main.py`. These tests verify:
- The `/` endpoint returns a 200 status code.
- The response contains the key `current_time_in_moscow`.
- The returned time matches the expected format (`%Y-%m-%d %H:%M:%S`) and is within 5 seconds of the actual Moscow time.

### Best Practices
1. **Modular Testing**: Tests are isolated and focus on specific functionalities.
2. **Assertions**: Clear and concise assertions ensure correctness.
3. **Time Validation**: The tests account for minor delays by allowing a 5-second tolerance.