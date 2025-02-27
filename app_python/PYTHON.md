# Python Web Application

## Framework Choice
We used Flask because:
- It is lightweight and simple.
- Quick to set up and deploy.
- Supports route handling efficiently.

## Best Practices
- Followed PEP 8 coding standards.
- Used environment-specific configurations.
- Kept dependencies minimal in `requirements.txt`.

## Testing and Quality
- Verified Moscow time updates correctly on refresh.
- Used Flask's built-in debugging for troubleshooting.

# Unit Testing for Flask App

## Best Practices Applied
- Used `pytest` for easy and readable testing.
- Created tests for:
  - Checking if the app runs correctly.
  - Validating the time format in the response.
  - Ensuring unsupported HTTP methods return appropriate errors.

## How to Run Tests
Run all tests using:
```bash
pytest tests/