# PYTHON.md

## Best Practices Applied

### 1. **Code Structure & Organization**
- The application follows a **modular structure**.
- The `services` layer follows the **Single Responsibility Principle (SRP)** by delegating time retrieval to `GetTimeService`.

### 2. **Configuration Management**
- `config.py` is used to store timezone settings separately, ensuring **maintainability** and **easy configuration changes**.


## Coding Standards

### 1. **PEP 8 Compliance**
- The code adheres to **PEP 8** for readability, including proper spacing, indentation, and meaningful function/class names.
- Docstrings are included for classes and functions to **enhance code documentation**.

### 2. **Flask Best Practices**
- The application uses `@app.get("/")` for route definition, making it explicit that it handles HTTP GET requests.
- The `GetTimeService` class implements a **static method** to encapsulate logic and prevent unnecessary instance creation.

## Testing & Code Quality

### 1. **Manual Testing**
- The application was tested by refreshing the browser and verifying the **correct Moscow time updates dynamically**.
- The time output format (`%Y-%m-%d %H:%M:%S`) was checked to ensure accuracy.

### 2. **Edge Cases Considered**
- The application was tested with different timezone inputs to ensure `pytz` correctly converts time.
- The Flask server was run locally to verify `render_template` correctly injects the `current_time` value into the template.

### 3. **Error Handling**
- The `get_time_by_timezone` method ensures correct timezone formatting by using `pytz`.
- Future improvements could include try-except blocks for **better error handling of invalid timezones**.

## Unit Tests Description

### Unit Tests Overview
The unit tests for this application are designed to ensure the correctness and reliability of both the business logic and the Flask routes. The tests are written using Python's built-in `unittest` framework.

### Test Coverage
The unit tests cover the following aspects:
1. **Testing the `GetTimeService` Class**:
   - Verified that the `get_time_by_timezone` method works correctly for valid timezones.
   - Ensured proper error handling for invalid timezones.
   - Tested edge cases, such as the "UTC" timezone.

2. **Testing Flask Routes**:
   - Validated the `/` route to confirm it returns the correct HTML content.
   - Simulated an invalid timezone configuration to test error handling.

### Best Practices Applied
- **Isolation**: Used temporary configurations to isolate dependencies.
- **Coverage**: Aimed for high test coverage, ensuring critical paths were tested.
- **Readability**: Wrote descriptive test names and assertions to make tests easy to understand.