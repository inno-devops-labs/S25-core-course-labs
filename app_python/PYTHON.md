# Python Web Application

## Overview

This document provides an overview of the Python-based web application developed using the **Flask** framework. The application displays the current time in Moscow, updating every time the page is refreshed.

---

## Choice of Framework: Flask

**Why Flask?**
- **Lightweight & Flexible**: Flask is a micro-framework that allows rapid development. It provides the essentials without imposing too many constraints.
- **Easy to Learn & Extend**: Flask's simple architecture is perfect for smaller applications. Additional features (e.g., database integrations, user authentication) can be added with various Flask extensions.

---

## Best Practices

1. **Separation of Concerns**  
   The logic for time zone retrieval is encapsulated within the route function. This approach ensures that each function handles a specific task, making the application easy to read and maintain.

2. **PEP 8 Compliance**  
   - Code adheres to Python's official style guide:
     - Descriptive variable and function names using `snake_case`.
     - Logical ordering of imports (`standard library`, `third-party`, and then local modules).
     - Line lengths are within 79 or 120 characters.
     - Consistent indentation (4 spaces) and spacing for readability.

3. **Use of Virtual Environments**  
   - A virtual environment (e.g., `venv`) is recommended to isolate dependencies and prevent conflicts with system-level Python installations.

4. **Code Readability**  
   - Clear and concise code with comments explaining key parts.
   - HTML and CSS embedded in the application are well-structured for easy adjustments.

5. **Proper Documentation**  
   - All files are well-documented using Markdown (`README.md`, `PYTHON.md`) to provide a clear understanding of the setup, usage, and design choices.

6. **Scalability**  
   - Although minimal, the application is structured in a way that it can be easily extended by separating logic into modules as needed.

---

## Testing & Code Quality

1. **Manual Testing**  
   - The Flask server was tested locally (`python app.py`).
   - The browser was used to verify the displayed Moscow time updates correctly on refresh.

2. **Automated Testing**  
   - Future integration with testing frameworks like `pytest` or `unittest` is planned. This can include:
     - Verifying HTTP response codes.
     - Testing time retrieval functionality with mocked data.

3. **Code Quality Tools**  
   - Tools like `flake8` can be used to ensure adherence to PEP 8 and highlight any potential style issues.

4. **Continuous Integration**  
   - A CI/CD pipeline (e.g., using GitHub Actions) can be configured for larger projects to automatically run tests and ensure code quality before deployment.

---

## 🧪 Unit Testing

To ensure the reliability of the Moscow Time Web Application, **unit tests were written using `pytest`**.

### ✅ What Tests Were Implemented?
1. **Homepage Status Code**
   - Ensures the `/` route returns a `200 OK` response.
2. **Correct Moscow Time Format**
   - Checks if the displayed time follows the `YYYY-MM-DD HH:MM:SS` format.
   - Compares it against the expected Moscow timezone.

### ✅ Best Practices Applied
- **Isolated Test Cases**: Each test function checks only **one aspect** of the application.
- **Fixtures for Test Clients**: Uses `pytest.fixture` to create a test Flask client.
- **Regular Expression Matching**: Ensures the time format is always valid.

### ✅ Running Tests
To run tests locally:
```bash
pytest test_app.py
```

These tests are also executed automatically in the CI/CD pipeline on every push or pull request.

---
## Conclusion

This Python web application exemplifies adherence to best practices, coding standards, and quality assurance methods. Flask was chosen for its simplicity and flexibility, and the `pytz` library guarantees accurate timezone handling for Moscow (MSK). By following these principles, the application is reliable, maintainable, and scalable for future improvements.
