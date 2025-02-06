# PYTHON.md

## Best Practices Applied

### Coding Standards
- **PEP 8 Compliance**: The application follows Python's PEP 8 standards.
- **Modular Structure**: The code is minimal, readable, and maintainable.

### Testing
- **Unit Testing**: Implemented using `pytest` to verify the application's correctness.
- **Manual Testing**: The application was tested by running it locally and refreshing the browser to verify time updates.
- **Time Zone Handling**: The `pytz` library was used to provide the correct Moscow time regardless of the system's local time.

### Code Quality
- **Readability**: The code is well-structured to be readable and understandable.
- **Dependencies**: Only required dependencies are included in `requirements.txt` for simplicity and efficiency.

### Framework Justification
Flask was chosen for its simplicity and lightweight nature, which perfectly matches the app. Unlike more complex frameworks such as Django, Flask ensures fast development without unnecessary complexity.

## Unit Tests
The following unit tests were created:
- **Test Time Format**: Ensures the returned time is in the correct format.
- **Test Time Zone**: Verifies that the application correctly retrieves Moscow time.
- **Flask Route Test**: Checks if the root route `/` returns a successful HTTP response.

To run the tests locally:
```bash
pytest test_app.py
```
