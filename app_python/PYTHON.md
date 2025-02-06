# Python Web Application

## Framework

I chose **Flask**. Flask is a framework for building web applications in Python. It is lightweight and fast to use, yet powerful enough to create full-fledged applications. Projects created in Flask fit into a single code file. The framework has extensive and well-structured documentation, which can help me in my development.

## Best Practices Applied

- **Linting**: I performed code validation using `pylint` to adhere to Python's coding standards.
- **Code Formatting**: I used `black` to maintain consistent code style and readability.
- **Code Readability**: I used meaningful function names and dockstrings to ensure clarity.
- **Version Control**: Project is maintained in Git with clear commits and patch requests.
- **.gitignore**: Excludes unnecessary files like virtual environment and cache files.

## Unit Tests

### Testing Best Practices

- **Isolation:** Each test runs independently of others.
- **Consistency:** Tests check expected behaviors and use a predefined format.
- **Automated Execution:** Tests run automatically in the CI/CD pipeline.
- **Code Linting:** Ensuring that code follows PEP 8 standards.
- **Assertions:** Using precise assertions to check expected output.

### Implemented Unit Tests

1. **Test Current Time Format**
   - Ensures that the application returns the current time in Moscow in the expected `YYYY-MM-DD HH:MM:SS` format.
   - Uses `pytz` for timezone consistency.

2. **Test Homepage Content**
   - Checks if the homepage contains the correct heading.
   - Ensures that the response status code is `200`.
