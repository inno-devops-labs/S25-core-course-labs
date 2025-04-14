# Framework Choice and Best Practices

## Framework Choice: Flask

For this web application, I chose **Flask** as the framework. Below are the reasons for selecting Flask:

- **Lightweight:** Flask is minimalistic and perfect for small-scale web applications.
- **Ease of Use:** Flask's simple API makes it easy to build and test applications quickly.
- **Well-Documented:** Flask has a large community and comprehensive documentation, making it beginner-friendly.

## Best Practices

In developing this application, I followed these best practices:

1. **Clear Code Structure:**
   - Used a single entry point (`app.py`) to define the application and routes.
   - Modularized the logic with reusable functions.
2. **Avoid Hardcoding:**
   - Utilized the `pytz` library for timezone handling instead of hardcoding time zones.
3. **Error Handling:**
   - Used Flask's built-in debugging tools to identify and fix issues.
4. **Readability:**
   - Added comments to explain key sections of the code.
   - Used descriptive variable names for better understanding.

## Coding Standards

The following standards were applied:

- **PEP 8 Guidelines:** Followed Python's official style guide to ensure consistent formatting.
- **Snake Case Naming:** Used `snake_case` for function and variable names.
- **Line Length:** Kept all lines under 79 characters for better readability.

## Testing and Code Quality

I ensured the application functions correctly through the following testing steps:

1. **Manual Testing:**
   - Ran the application locally and refreshed the browser to confirm the time updates.
   - Verified the displayed time matches the current time in Moscow.
2. **Cross-Browser Testing:** (Optional)
   - Tested the application on Chrome, Firefox, and Safari.
3. **Code Quality:**
   - Used clear, concise code and avoided redundant logic.
  
## Unit Testing in Python Project

### Running Tests Locally

```bash
python -m unittest discover tests/
```

### Best Practices for Unit Testing

- **Use a Test Client:** Flask provides a built-in test client to simulate requests.
- **Isolated Tests:** Each test runs independently with a fresh app instance.
- **Assertions:** Use assertions to check expected results.
- **Automated Execution:** Tests are automated using `unittest` and integrated into CI.

### Unit Tests Implemented

1. **Test `/` route response**:
   - Ensures the Moscow time page loads successfully.
   - Validates status code `200 OK`.

2. **Test `/` route content**:
   - Confirms the page contains the correct "Current Moscow Time:" text.
   - Ensures the response includes valid HTML.
