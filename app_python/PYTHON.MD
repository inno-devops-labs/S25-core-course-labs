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