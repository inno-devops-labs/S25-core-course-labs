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
