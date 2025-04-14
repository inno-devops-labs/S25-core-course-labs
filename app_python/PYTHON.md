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

## Testing

- Tested the application manually to ensure it displays the correct time.
- Verified the error handling for invalid time zones.