# Python Moscow Time Web Application

## Overview

A simple web application that displays the current time in Moscow. Built with Flask.

## Features

- Displays the current Moscow time.
- Updates time on page refresh.

### Framework Choice

Flask was chosen because it is lightweight, easy to set up, and perfect for small projects like this one.

### Best Practices

- Followed PEP 8 standards.
- Used descriptive function names and modular structure.
- Secured the `requirements.txt` file to avoid unnecessary dependencies.

## Testing

- Verified the application locally with various refresh intervals to ensure accurate time updates.
- Developed and executed unit tests to validate functionality and reliability.

### Unit Testing Best Practices

Unit testing is a crucial part of software development to ensure that individual components work as expected. The following best practices were applied in this project:

- **Isolation**: Each test runs independently and does not rely on external dependencies.

- **Assertions**: Proper assertions are used to verify expected outputs.

- **Edge cases**: Tests cover normal, boundary, and invalid inputs.

- **Automated execution**: The test suite runs automatically in the CI pipeline.

- **Readable & maintainable**: Tests are simple and well-documented.

### Implemented Unit Tests

The following unit tests have been implemented:

1. **Test Home Page Response**:
 checks if the home page (/) returns an HTTP 200 status code.
Ensures the endpoint is reachable.

2. **Test Time Format**: ensures the returned time follows the HH:MM:SS format. Uses regex validation to match the expected format.