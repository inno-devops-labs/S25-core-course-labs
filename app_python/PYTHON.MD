# Python Web Application: Moscow Time

## Overview

This project is a simple Python web application that displays the current time in Moscow using the **FastAPI** framework. The application serves an HTML page with the current time and an image of Moscow.

---

## Framework Choice: FastAPI

### Why?

1. **Performance**  
   FastAPI is one of the fastest Python web frameworks, making it ideal for lightweight applications like this one.

2. **Ease of Use**  
   FastAPI simplifies development with Python type hints and automatic API documentation (Swagger UI and ReDoc).

3. **Asynchronous Support**  
   Native support for asynchronous programming ensures scalability for future enhancements.

4. **Minimal Boilerplate**  
   The `/time/moscow` endpoint is implemented with minimal code while maintaining clarity and functionality.

---

## Best Practices Applied

### 1. Timezone Handling
- The `pytz` library is used to accurately handle timezone conversions. The timezone is explicitly set to `Europe/Moscow`, ensuring precise and reliable time display.

### 2. Code Organization
- The code is modular and follows the **Single Responsibility Principle**:
  - The `get_location_time` function is responsible for fetching the current time in a specified timezone.
  - The `/time/moscow` endpoint handles HTTP requests and returns the HTML response.

### 3. Coding Standards
- The code adheres to **PEP 8** guidelines:
  - Proper indentation, meaningful variable names, and consistent formatting.
  - Inline comments explain key functionality.

### 4. Error Handling
- Basic error handling is implemented to manage invalid or unsupported timezones:
  ```python
  def get_location_time(region):
      try:
          return datetime.now(pytz.timezone(region))
      except pytz.UnknownTimeZoneError:
          raise ValueError(f"Invalid timezone: {region}")
  ```

---

## Implementation Details

### Endpoint: `/time/moscow`

- **Purpose**: Displays the current time in Moscow with a simple HTML design.
- **Logic**:
  - The `get_location_time` function fetches the current time in the `Europe/Moscow` timezone using the `pytz` library.
  - The time is dynamically embedded into the HTML response using Python's `f-string`.

### HTML Design

- The HTML page includes:
  - A bold heading displaying the current time in Moscow.
  - An image of Moscow for visual appeal.
  - Basic CSS for centering and responsiveness.


## Unit Tests

### Overview
Unit tests have been implemented using the `pytest` framework to ensure the correctness of the `get_location_time` function. These tests validate both valid and invalid timezone inputs, ensuring robust functionality.

### Test Cases
1. **Valid Timezone**:
   - Verifies that the function returns a `datetime` object for a valid timezone (e.g., `Europe/Moscow`).
2. **Invalid Timezone**:
   - Ensures the function raises a `ValueError` with an appropriate error message when an invalid timezone is provided.
3. **Edge Case Timezones**:
   - Tests edge-case timezones like `Etc/GMT+12` to ensure compatibility with non-standard timezone names.
4. **Special Characters in Timezone**:
   - Validates that the function handles timezones with special characters (e.g., `America/New_York`) correctly.

### Best Practices Applied
1. **Test Isolation**:
   - Each test focuses on a single behavior of the `get_location_time` function, ensuring clarity and maintainability.
2. **Assertions with Descriptive Messages**:
   - Meaningful assertion messages provide clear feedback in case of test failures.
3. **Edge Case Testing**:
   - Includes tests for edge cases and uncommon timezone names to ensure comprehensive coverage.
4. **Readable and Maintainable Code**:
   - Tests are organized into a dedicated class (`TestGetLocationTime`) for better structure and readability.