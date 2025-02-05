# Python Web Application

## Framework Choice

I chose **Flask** for this Python web application because:
- It is lightweight and simple to learn.
- It is well-suited for small projects or quick prototypes.
- It has a wide ecosystem of extensions and good community support.

## Best Practices

1. **Virtual Environment**  
   Using a virtual environment (e.g., `venv`) helps isolate project dependencies from the system-wide Python installation.

2. **Coding Standards (PEP 8)**  
   - We follow standard Python coding guidelines.
   - We use descriptive variable and function names.

3. **Testing**  
   - Basic tests can be done using `unittest` or `pytest`.
   - For this small project, it is enough to test the server response and status codes.

4. **Security**  
   - Avoid storing secrets (tokens, passwords) in code.
   - Ensure the Flask server is not exposed publicly with `debug=True` in production.

## Testing

1. Start the application with `python main.py`.
2. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/).
3. Refresh to confirm the displayed time updates correctly.


## Unit Tests

We use **pytest** to test our Flask application. Our tests are located in the `tests/` directory. Main test points:

1. **Status Code Check**  
   Ensures that the root endpoint (`/`) returns HTTP 200.
2. **Content Check**  
   Confirms the response contains specific text like `"Current time in Moscow"`.

### Best Practices in Our Tests

- **Arrange-Act-Assert**: We set up the app in a testing mode, call the endpoint, then assert the response.
- **Isolated Tests**: Each test only verifies a small piece of functionality.
- **Pytest Fixtures**: Simplifies test client creation and teardown.
