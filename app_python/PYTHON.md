# Python Web Application

## Lab 1: Web Application Development

## Task 1: Python Web Application

### Framework Choice

I chose Flask framework to build a web application.
Flask is a popular choice when you need to develop simple backend application fast because of its advantages:

- Easy to learn framework with no unnecessary boilerplate
- Easy to build simple JSON APIs. New endpoint handlers are added with simple decorator-annotations to functions
- Flask automatically sets up HTTP server for local testing
- Good built-in JSON support with `jsonify` package

## Task 2: Well Decorated Description

### Best Practices Applied

- Used `pytz` library for accurate timezone calculation and formatted datetime using human-readable ISO-like format
- Formatted code using `Black`. `Black` eliminates manual code style decisions and formats code according to PEP8
  guidelines
- Created `requirements.txt` with required dependencies
- Added `.gitignore` file
- Used descriptive variable names
- Maintained clean import structure

These best practices helped me follow coding standards and ensure code quality.

### Testing

To test web application I used debug mode in Flask and
made several `GET http://127.0.0.1:5000` requests via web browser.
Requests return current time in Moscow timezone as expected.

--

## Lab 3: Continuous Integration Lab

## Task 1: Code Testing and Git Actions CI

This application uses unit tests written with [pytest](https://docs.pytest.org).

## Overview of Unit Tests

- **test_moscow_time:** This test checks the "/" endpoint.
  - It checks that the server returns a 200 status code.
        - It ensures that the JSON response contains the keys "timezone" and "current_time".
        - It validates that the "timezone" value is "Europe/Moscow".
        - It confirms that "current_time" follows the format "YYYY-MM-DD HH:MM:SS" using a regular expression.

## Best Practices Applied for Unit Tests

- Isolation: The test client is configured with `TESTING=True` to isolate the tests from the production environment.
- Independence: Each test is isolated from other tests and does not depend on or affect the state of other tests.
- Clear Naming: Test function name clearly indicate what is being tested.
- Minimal Dependencies: Tests avoid external dependencies (e.g., database and external services calls) to ensure
  stability.
