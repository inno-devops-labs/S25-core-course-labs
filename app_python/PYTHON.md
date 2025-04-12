# PYTHON.md

## Framework Choice

I chose FastAPI for this web application because it is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. It is easy to use and allows for rapid development.

## Best Practices

- **Code Structure:** Organized the code into separate modules and directories for better maintainability and scalability. Althought the initial requirement is for Moscow timezone, it could be effectively scaled up in the future with different timezones. I used a main.py file, in which I import a router from the routers module. In order to implement the endpoint for the time operations router, I use utility functions from the util module and the templates for rendering the data.
- **Error Handling:** Implemented error handling for invalid time zones (in our case, a timezone which is not moscow).
- **Templates:** Used Jinja2 templates for rendering HTML pages.
- **Environment Variables:** Used `dotenv` to manage environment variables if necessary.
- **Testing:** Manually ensured the application updates the displayed time upon page refreshing, and renders the error page in case of an exception.

## Coding Standards

- Followed PEP 8 coding standards.
- Used meaningful variable and function names.
- Added docstrings for functions.

## Testing: Unit tests

### Best Practices Applied
- **Isolation:** Each test is independent and does not rely on the state of other tests.
- **Fixtures:** Used for setup and teardown processes.
- **Mocking:** External dependencies are mocked to ensure tests are focused on the unit being tested.

### Unit Tests Created
- **Utility Functions:**
  - `test_get_current_time_valid_zone`: Tests the `get_current_time` function with a valid zone.
  - `test_get_current_time_invalid_zone`: Tests the `get_current_time` function with an invalid zone.
- **Endpoints:**
  - `test_root`: Tests the root endpoint.
  - `test_display_time_valid_zone`: Tests the `/current-time/{zone}` endpoint with a valid zone.
  - `test_display_time_invalid_zone`: Tests the `/current-time/{zone}` endpoint with an invalid zone.