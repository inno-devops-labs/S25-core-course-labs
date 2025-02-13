# Python Web Application

## Framework Choice: Flask
Flask was chosen for its simplicity, lightweight design, and ease of use for small web applications. It is beginner-friendly and suitable for displaying dynamic data like the current time.

## Best Practices
- Followed Python's PEP 8 coding standards.
- Separated the logic into clear routes and functions.
- Used `requirements.txt` to manage dependencies.
- Verified the code with testing.

## Testing
- The application was manually tested by refreshing the page to confirm the time updates dynamically.

---

# Unit Testing in Python

## Overview

Unit testing ensures the reliability and correctness of Python application by verifying that individual components work as expected. The tests are written using pytest and focus on checking core functionality, including HTTP responses and content validation.

The unit tests are located in the tests/ directory and currently include test_app.py.

This test suite verifies the application’s homepage behavior.

## Test: test_homepage(client)

Setup:
-	Uses pytest.fixture to create a test client for the Flask application.
-	Enables TESTING mode to ensure a controlled test environment.

Execution:
-	Sends a GET request to the homepage (/).

Assertions:
-	Checks if the response status code is 200 (OK).
-	Verifies that the response contains the expected text: "Current Time in Moscow".

## Best Practices Applied
	
1.	Fixture Usage
- client() fixture ensures that each test runs in isolation with a fresh instance of the application.
2. HTTP Response Validation
- Ensures correct status codes and expected page content.
3. Minimal Dependencies
- The test only relies on the Flask test client, avoiding unnecessary complexity.
4.	Automation & CI Integration
-	The test suite is designed to be executed automatically in the GitHub Actions CI workflow.
5.	Clear & Readable Assertions
-	Explicitly checks response data and HTTP status for clarity.
