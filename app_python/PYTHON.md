# Python Web Application

## Framework Choice:
I have chosen Flask as the web framework for this application, because it is lightweight, easy to set up, 
and ideal for small applications like displaying the current time.

## Best Practices Applied:
- **Code Readability**: Used meaningful function and variable names for clarity.
- **Modular Structure**: Separated route logic from the main app structure.
- **Time Zone Handling**: Used `pytz` to ensure correct Moscow time handling.
- **Security**: Avoided hardcoded configurations and enabled debug mode only in development.
- **Minimal Dependencies**: Kept the `requirements.txt` minimal to avoid unnecessary packages.

## Coding Standards & Quality:
- Followed **PEP 8** coding conventions.
- Used `black` for code formatting.

## Testing:
- Verified time updates by refreshing the page.
- Checked that the time displayed on the web page matches the current time in Moscow.

## Unit Testing:

I implemented unit tests to validate the HTTP response status, template rendering, and the accuracy of the displayed time.

### **Unit Tests Implemented:**
- **Response Code Test**: Ensures that the homepage (`/`) returns a **200 OK** response.
- **Template Rendering Test**: Confirms that the `index.html` template is properly rendered.
- **Time Presence Test**: Verifies that the `current_time` variable is included in the rendered template context.
- **Time Format Validation**: Ensures that the displayed time follows the correct `HH:MM:SS` format (without the date).
- **Correct Moscow Time Test**: Checks that the displayed time matches the **current Moscow time**.

### Best Practices in Unit Testing:
- **Structured Test Organization**: `pytest` fixtures and `conftest.py` are used to separate concerns.
- **Reusable Fixtures**: `app()`, `server()`, and `captured_templates()` to prevent code duplication.
- **Testing Mode Enabled**: Configured `app.config["TESTING"] = True` to isolate tests from external dependencies.
- **Strict Assertions**: Explicit assertions like `assert response.status_code == 200` to guarantee correctness.
- **Format Validation with Regex**: Enforced strict time formatting rules using regex (`\d{2}:\d{2}:\d{2}`).
- **Timezone-Aware Validation**: Verified that the application correctly displays **Moscow time (Europe/Moscow)**.


