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

## Unit Testing

We have implemented unit tests for our Python web application using Python's built-in `unittest` framework. The tests are located in `test_main.py` and cover:

- **Status Code Test**: Ensures that the main route (`/`) returns HTTP status code 200.
- **Content Test**: Confirms that the response from the main route includes the expected text "Current time in Moscow".

### Best Practices Applied

- **Modular Testing**: Tests are split into separate test cases for clarity.
- **Flask Test Client**: Utilizes Flask's built-in test client to simulate HTTP requests.
- **CI Integration**: Unit tests are integrated into the CI workflow to guarantee continuous code quality.
