# Python web application - best practices and code quality

## Framework choice: Flask

For this web application, I chose **Flask** as the web framework.

### Reasons of choice:

- **Minimalistic and lightweight**: Flask doesn’t impose unnecessary restrictions on how to structure the application,
  giving developers more control over the app's components.
- **Easy to learn and use**: Flask's simple design and straightforward API make it an excellent choice for quick
  prototyping.
- **Extensive documentation and community support**: Flask has an extensive set of resources and a large community,
  making it easy to find solutions and tutorials.
- **Built-in development server**: Flask includes a built-in server that makes it easy to start the app without needing
  to configure additional infrastructure.

Overall, Flask is a best web framework for building small to medium-sized web applications.

## Best practices applied

### 1. Code organization

The project follows a clean structure:

- The **Flask app** is located in the `app/` directory, keeping everything organized.
- The **templates** for HTML files are stored in a dedicated `templates/` folder.
- **Static files** (like CSS and JavaScript) can be placed in the `static/` directory.

### 2. Use of Virtual Environments

A virtual environment (`.venv/`) is used to isolate project dependencies. This ensures that the project’s dependencies
don’t conflict with those of other projects on the system.

To activate the virtual environment:

```bash
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

### 3. Testing with pytest

The project uses pytest for robust and efficient testing. Key reasons for choosing pytest:

- Ease of use: Writing and running tests is simple and intuitive.
- Fixture support: Allows setup and teardown of test cases using pytest.fixture.

### 4. Dependency management

Dependencies are managed through requirements.txt.
This file includes all the necessary libraries to run the application.

### 5. Code quality

- PEP 8 compliance: The code follows the PEP 8 style guide, ensuring it is readable and maintainable.
- Clear function names

### 6. Version Control with Git

The project uses Git for version control. It follows the standard best practices:

- Regular commits with clear, concise messages.
- A .gitignore file is included to prevent unnecessary files (such as virtual environments and IDE-specific files) from
  being tracked by Git.

## Unit tests

### Best practices applied
- **Arrange, Act, Assert (AAA) pattern** for clarity and maintainability.
- **Fixture-based testing** using `pytest.fixture` to manage test client instances.
- **Mocking with `unittest.mock.patch`** to isolate dependencies and avoid real-time dependency issues.
- **Assertions on HTTP response codes** and content validation.

### Implemented tests
1. **Dynamic Time Test:**  
   - Checks if the displayed time on the homepage matches the current Moscow time (formatted as `YYYY-MM-DD HH:MM`).
   - Uses `pytest` and `pytz` to compare timestamps.
  
2. **Static Time Test (Mocking):**  
   - Mocks `datetime.now()` to return a fixed value for predictable test results.
   - Ensures the webpage correctly formats and displays the predefined timestamp.
