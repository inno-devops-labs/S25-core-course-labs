# Framework Choice: FastAPI

**Justification for Choosing FastAPI:**

1. **High Performance:** FastAPI is built on Starlette and Uvicorn, offering high performance suitable for web applications.
2. **Ease of Use:** Simplifies API development with intuitive syntax and automatic interactive documentation.
3. **Asynchronous Support:** Native support for async operations enhances scalability.
4. **Data Validation:** Integrated Pydantic ensures robust data validation and serialization.
5. **Template Support:** Utilizes Jinja2 for server-side rendering, ideal for serving HTML pages efficiently.

This framework aligns with the project's needs for simplicity, efficiency, and maintainability.


# Best Practices and Coding Standards

This document outlines the best practices and coding standards followed in the development of the **Moscow Time Web Application**.

---

## **Best Practices Applied**

### 1. **Code Structure and Organization**
- The application follows a modular structure:
  - `main.py`: Contains the FastAPI application logic.
  - `templates/`: Stores HTML templates for rendering the frontend.

### 2. **Environment Management**
- Dependencies are explicitly listed in `requirements.txt` for reproducibility.

### 3. **Error Handling**
- FastAPI automatically handles validation errors and provides detailed error messages.

### 4. **Security**
- FastAPI includes built-in security features like data validation and protection against common vulnerabilities (e.g., SQL injection, XSS).
- Sensitive data (e.g., API keys) should be stored in environment variables.

### 5. **Performance**
- Asynchronous programming is used to handle multiple requests efficiently.
- FastAPI’s high performance ensures low latency for time-sensitive applications.

### 6. **Documentation**
- The application is documented in `README.md` and `PYTHON.md`.

### 7. **Coding Standards**
- Code follows **PEP 8** guidelines for readability and consistency.

### 8. **Version Control**
- A `.gitignore` file is maintained to exclude unnecessary files (e.g., `__pycache__`, virtual environment folders).

### 9. **Testing**
- Manual testing was applied, I checked page refresh and tried to request from different timezones

---

## **Dependencies**
- **FastAPI**: Web framework for building the application.
- **Uvicorn**: ASGI server for running the application.
- **Jinja2**: Templating engine for rendering HTML.
- **PyTZ**: Timezones from all over the world.

# Unit Tests
## Test File Structure

- **`tests/test_main.py`**: Contains the unit tests for the application's endpoint.

## Unit Tests Created

1. **`test_read_time_status_code`**:
   - **Purpose**: Verify that the GET request to the root endpoint (`"/"`) returns an HTTP 200 status code.
   - **Best Practice**: Ensures that the endpoint is reachable and responds as expected.

2. **`test_read_time_format`**:
   - **Purpose**: Verify that the rendered HTML response contains a datetime string in the correct format (`YYYY-MM-DD HH:MM:SS`).
   - **Best Practice**: Uses regular expressions to validate the output, ensuring that the datetime formatting logic in the endpoint is correct.

## Best Practices Applied

- **Isolation of Tests**: Each test is independent, ensuring that no test depends on the state left by another.
- **Clear Assertions and Error Messages**: Assertions include helpful error messages to facilitate debugging in case of failures.
- **Use of FastAPI's TestClient**: The tests simulate HTTP requests using FastAPI’s `TestClient`, which provides an environment similar to production.
- **Descriptive Test Names and Docstrings**: Each test function has a descriptive name and a docstring explaining its purpose, making the test suite easier to understand and maintain.
- **Regular Expression Validation**: The use of regex ensures that the datetime string follows the expected format, making the test robust even if the surrounding HTML changes.
