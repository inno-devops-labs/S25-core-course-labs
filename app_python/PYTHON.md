# Python web application

## Framework choice

Flask is perfect for our small and simple application due to its lightness and undemanding nature.

## Best practices

### Coding standards

- [PEP8](https://peps.python.org/pep-0008/)
- Use of virtual environment
- Well-structured application architecture
- Code readability

### Code quality

- [Ruff](https://docs.astral.sh/ruff/) was used for code linting and formatting.

## Testing

### Manually

- Flask application has been manually tested locally with local server.
- The behavior of app was expected and stable.

### Automatically

This project uses *pytest* as a simple and flexible unit testing solution.

Unit tests:

- *Route response testing:* Test root route to ensure it responds with an HTTP 200 status.
- *Function to get current time testing:* Test function `get_current_time` to ensure it returns a correctly formatted
  date/time string.
- *Testing the date/time displaying on page:* Tests verify that the rendered template displays correct data/time and
  timezone.
