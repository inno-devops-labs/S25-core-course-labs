# Go Web Application

## Framework Choice: Gin

Gin was chosen for following reasons:
- **High Performance**: Gin is one of the fastest web frameworks for Go.
- **Minimalistic**: Lightweight and easy to use.
- **Middleware Support**: Built-in support for middleware, making it extensible.

### Best Practices

1. **Modular Code**: The application is structured in a single file for simplicity.
2. **Error Handling**: Gin provides built-in error handling.
3. **Testing**: The application can be tested.

## Unit Tests

The application includes comprehensive unit tests located in `main_test.go`. These tests verify:
- The `/` endpoint returns a 200 status code.
- The response starts with "Current time in Moscow:".
- The returned time is in the expected format (`YYYY-MM-DD HH:MM:SS`).

### Best Practices

- **Modular Testing**: Tests are isolated and focus on specific functionalities.
- **Assertions**: Clear and concise assertions ensure correctness.
- **Edge Cases**: The tests account for potential formatting issues.