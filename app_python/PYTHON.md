# PYTHON.md

This document outlines the best practices followed in this **Moscow Time Web Application** project, inspired by this [repo](https://github.com/zhanymkanov/fastapi-best-practices). It also explains why the official FastAPI documentation, while excellent for getting started, may not always suffice for large-scale industrial projects.

---

## Why FastAPI Best Practices Repository?

The repository [fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices) by **Zhanymkanov** is an excellent resource for implementing FastAPI in industrial-grade projects. Here’s why it was chosen as a reference:

1. **Real-World Experience**:
   - The repository is based on real-world industrial projects, ensuring that the practices are battle-tested and scalable.
   - It addresses common challenges faced in production environments, such as dependency management, testing, and deployment.

2. **Beyond Official Documentation**:
   - While the official FastAPI documentation is great for beginners, it often focuses on simplicity and may not cover advanced use cases or scalability concerns.
   - This repository fills the gap by providing patterns and practices that are essential for large-scale applications.

3. **Community-Driven**:
   - The repository is widely recognized in the FastAPI community and has been reviewed and improved by multiple contributors.

4. **Шеф топит за него**:
   - как уж тут поспорить.

---

## Best Practices Implemented in My Project

### 1. **Project Structure**

- The project follows a modular structure.
  - This structure separates application logic, tests, and configuration, making the project easier to maintain and scale.

### 2. **PEP 8 Compliance**

- The code adheres to **PEP 8** standards for readability and consistency:
  - Use of `snake_case`, docstrings, spacing and other popular standards.

### 3. **Dependency Management**

- Dependencies are listed in `requirements.txt` for easy installation:
  - A virtual environment is used to isolate dependencies and avoid conflicts.

### 4. **Logging**

- Logging is used to track application behavior and errors. Implemented as a middleware that writes logs in terminal.

### 5. **Testing**

- Unit tests are written using `pytest` to ensure functionality and correctness:
  - Test cases include:
    - Verifying the endpoint response.
      - Validating the time format.
      - Ensuring the time updates between requests.
     To run tests:

     ```bash
     pip install pytest
     pytest
     ```

### 6. **Code Formatting**

- Use the `black` module to ensure consistent style during development.
     To run styler formater run the following command in root directory:

     ```bash
     pip install black
     black .
     ```

### 7. **Documentation**

- A comprehensive `README.md` file is provided to guide users through setup, usage, and testing.
  - Docstrings are added to functions for better code documentation.

---

## Tests

- `test_get_moscow_time`:
  - This test checks that the `/get_moscow_time` endpoint returns a valid response with a status code of 200 and that the response contains the key `moscow_time`.

- `test_moscow_time_format`:
  - This test verifies that the `moscow_time` value returned by the endpoint is correctly formatted according to the "%Y-%m-%d %H:%M:%S" format.

- `test_moscow_time_updates`:
  - This test ensures that the Moscow time returned by the endpoint updates between consecutive requests.

- `test_moscow_time_timezone`:
  - This test ensures that the time returned by the `/get_moscow_time` endpoint is in the Europe/Moscow timezone.

## Tests best Practices

### **Asserting Status Code:**

- The test asserts that the response status code is 200, which is a standard practice to ensure the endpoint is working correctly.

### **Isolation of Tests:**

- Each test is isolated and focuses on a single aspect of the functionality (e.g., response structure, format, time update, time zone). This makes the tests easier to understand and maintain.

### **Use of TestClient:**

- The TestClient from FastAPI is used to simulate HTTP requests to the application. This is a standard practice for testing FastAPI applications, allowing you to test endpoints without running a live server.

### **Assertions with Clear Messages:**

- The assertions include clear error messages (e.g., "Time did not update between requests"), which help quickly identify the cause of a test failure.

### **Testing Edge Cases:**

- Testing the behavior of the endpoint under different time zones or handling potential errors.
