# PYTHON.md

## Framework Choice
We chose FastAPI as our web framework due to its high performance, ease of use, and support for asynchronous programming. FastAPI provides automatic interactive API documentation which makes it easier to develop and test APIs quickly.

## Best Practices Applied
- Modularized code structure.
- Proper error handling.
- Use of environment variables for configuration.
- Clean and readable code with proper comments.

## Coding Standards
- Followed PEP 8 style guide for Python code.
- Used meaningful variable and function names.
- Added docstrings where necessary.

## Testing
- Manually tested the application by refreshing the page and verifying the time update.
- Ensured the application runs without errors in debug mode.

# Python Testing Best Practices

## Overview
- **Isolated Tests:** Each test focuses on a single function or behavior.
- **Parametrized Tests:** Using `pytest.mark.parametrize` to test multiple inputs with the same test.
- **Clear Naming:** Test function names describe the behavior being tested.
- **Arrange-Act-Assert Pattern:** Organizes each test into setup, execution, and verification phases.

## Running the Tests
- Install dependencies: `pip install -r requirements.txt`
- Run tests: `pytest`
