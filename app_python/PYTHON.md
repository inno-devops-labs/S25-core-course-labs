# Unit Tests and Best Practices

## Unit Tests Overview
Implemented unit tests to ensure the correctness and reliability of Flask app. The tests cover the following aspects:

1. Testing `get_moscow_time` Function
   - Ensures the function returns a string in the correct datetime format (`YYYY-MM-DD HH:MM:SS`).
   - Uses regex to validate the returned string.

2. Testing the Home Page (`/`)
   - Sends a GET request to the root URL (`/`).
   - Asserts that the response status code is `200`.
   - Checks if the response contains the expected text "Current time in Moscow:".

3. Testing 404 Error Handling
   - Sends a request to a non-existent route.
   - Asserts that the response status code is `404`.
   - Verifies that the response contains the correct error message.

## Best Practices Applied

# 1. Test-Driven Development (TDD)
We wrote tests to define expected behavior before implementing changes, ensuring robust and reliable code.

# 2. Automated Testing with GitHub Actions
- Integrated unit tests into the CI pipeline.
- Ensured that tests run on every push and pull request.

# 3. Separation of Concerns
- Kept tests in a separate `test_app.py` file to maintain modularity and readability.
- Used `unittest.TestCase` to structure test cases properly.

# 4. Error Handling Validation
- Tested how the application handles incorrect URLs with a 404 response.
- Ensured exceptions in `get_moscow_time` are logged correctly.

# 5. Code Style and Linting
- Enforced PEP8 standards using `flake8` to maintain code quality.



