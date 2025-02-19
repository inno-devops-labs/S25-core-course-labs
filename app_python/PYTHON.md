# Python web application: Moscow Time

## Overview

This web application displays the current time in Moscow, Russia. It is built using the Flask framework and follows best practices for web development in Python.

### Framework choice: Flask

__*Flask*__ was chosen for its simplicity and flexibility, ideal for small web apps. Flask allows for quick setup and provides the necessary tools to create a functional web application with minimal boilerplate code.

### Key features of Flask

- __*Lightweight*__: Flask has a small core but is extensible.
- __*Flexibility*__: Developers have the freedom to choose their tools and libraries.
- __*Simplicity*__: Flask's documentation is clear and beginner-friendly, making it easy to get started.

## Best practices applied

### 1. Code structure

- **Root directory `app_python/`:**
   - Contains the main application directory and other essential files.

- **Main application directory `app/`:**

   - **Static files `static/`:**
   Directory for static files such as CSS and images.

   - **HTML templates `templates/`:**
   Directory for HTML templates used by the Flask application.

   - **Initialization file `__init__.py`:**
   Makes the app directory a Python package, and contains the main body of the project, including Flask app initialization and route definitions.

- **Tests directory `tests/`:**
Unit tests `test_app.py`.

- **Entry point script `run.py`:**
Script to run the Flask application.

- **Dependencies file `requirements.txt`:**
Lists all the Python dependencies required for the project.

### 2. Time zone handling

- The `pytz` library is used to handle time zones accurately. The __*Europe/Moscow*__ time zone is explicitly set to ensure the correct time is displayed.

### 3. Template rendering

- Flask's `render_template` function is used to render the `index.html` template, passing the current time as a variable. This separates the logic from the presentation layer.

### 4. Coding standards

- The code follows PEP 8 guidelines for Python, including proper indentation, naming conventions, and spacing.

## Unit testing

### Best practices applied:

- **Use `pytest` as a testing framework**: `pytest` is lightweight and widely used for testing Python applications.
- **Use fixtures (`@pytest.fixture`)**: This ensures the Flask test client is properly set up and torn down after tests.
- **Check HTTP status codes**: Ensure that routes return the expected status codes (e.g., `200 OK`).
- **Verify content in response**: The tests confirm that the expected text (e.g., "Current Time in Moscow") appears on the page.
- **Validate the displayed time**: The test compares the rendered time with the actual Moscow time to ensure accuracy.

### Implemented unit tests:

1. **_test_homepage(client)_**
   - Ensures that the homepage loads successfully.
   - Confirms that the response contains the phrase "Current time in Moscow".
   - Checks if the HTTP response status code is `200`.

2. **_test_moscow_time(client)_**
   - Retrieves the current Moscow time.
   - Fetches the homepage and checks if the time displayed matches the actual Moscow time.
   - Ensures proper timezone handling.

## Requirements

The following dependencies are required to run this application:

- Flask 3.1.0
- pytz 2024.2
- pytest 8.3.0
- Jinja2 3.1.5

