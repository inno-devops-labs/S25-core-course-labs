# Flask Web Application: Moscow Time Documentation

## Framework Choice: Flask

I chose the **Flask** framework for this web application because it is a lightweight and flexible Python web framework. Flask is ideal for small to medium-sized applications, and it provides the necessary tools to build a web application quickly without unnecessary complexity. Its modular design allows for easy scalability and customization.

---

## Best Practices Applied

### 1. **Modular Architecture**

- The application follows a modular structure, separating the main application logic (`app.py`) from the templates (`index.html`). This makes the codebase easier to maintain and extend.

### 2. **PEP 8 Compliance**

- The code adheres to the **PEP 8** style guide for Python, ensuring readability and consistency. Tools like `pylint` and `flake8` were used to enforce these standards.

### 3. **Virtual Environment**

- A virtual environment was used to isolate the application's dependencies. This ensures that the application runs consistently across different systems and avoids conflicts with other Python projects.

### 4. **Testing and Code Quality**

- **Static Code Analysis**: Tools like `pylint` and `flake8` were used to check for code quality and adherence to coding standards.
  - **Manual Testing**: The application was manually tested to ensure it displays the correct Moscow time and updates dynamically upon page refresh.

---

## Testing

To ensure the application works as expected, the following steps were taken:

1. **Static Code Analysis**:

   ```bash
   python3 -m pylint app.py
   flake8 app.py
   ```

2. **Dependency Installation**:

   ```bash
   pip3 install -r requirements.txt
   ```

3. **Manual Testing**:
   - The application was run locally, and the displayed time was verified to match the current time in Moscow.
   - The page was refreshed multiple times to ensure the time updates correctly.

---

## Code Quality

The application follows best practices for code quality, including:

- Proper documentation and comments in the code.
- Adherence to PEP 8 standards.
- Use of a virtual environment for dependency management.
- Testing with both automated tools and manual verification.

---
