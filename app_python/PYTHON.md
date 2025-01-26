# Lab 1: Web Application Development

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
