### Choosing a framework
Flask is best suited for creating this web application, as it is a simple framework for small projects.

### Applied best practices
- Clean code structure.
- Using the `pytz` library to work with time zones.

### Testing
During the testing of the application, the time was updated every time the page was refreshed.

### Implemented Unit Tests:
## 1. `test_homepage`
- Checks that the home page loads successfully.
- The response code should be `200 OK`.
- The page should contain the text `"Current time in Moscow:"`.

## 2. `test_time_format`
- Checks that the page displays the correct time format.
- A regular expression is used to check the `YYYY-MM-DD HH:MM:SS` format.

### Best Practices Applied:
1. **Using `unittest`**
- Structured tests with `setUp()` to prepare the environment.
- Tests are isolated and independent of each other.

2. **Checking the page content**
- `assertEqual(response.status_code, 200)` — checking the status code.
- `assertIn(b"Current time in Moscow:", response.data)` — checking the key text.

3. **Test automation**
- Tests are run via `unittest discover`, which makes them convenient for CI/CD.
