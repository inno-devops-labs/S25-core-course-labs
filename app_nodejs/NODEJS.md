# Node.js Web Application

## Framework Choice

I chose **Express.js** because:

1. It is minimalistic and efficient for web applications.
2. Built-in routing support.

## Best Practices

1. Organized the app into modular components.
2. Used `moment` for timezone handling, which simplifies date and time management.

## Coding Standards

1. Code is written in a modular and readable way.
2. Variable names are descriptive and named in lowerCamelCase.

## Testing

1. Manualy verified that the app endpoint correctly displays Abu Dabi time.
2. Manualy tested app stability by loading the HTML page in the browser for multiple concurrent times.

## Unit Testing

The unit tests are written using **Jest** and **Supertest** to test the Express API endpoint `/current-time`. The following test cases have been covered:

1. **Valid Response Format**

   - Ensures the `/current-time` endpoint returns a JSON response containing a valid time in `HH:mm:ss` format.

2. **Correct Abu Dhabi Time (UTC+4)**

   - Verifies that the API returns the expected time with the correct UTC offset.

3. **404 Not Found for Invalid Routes**
   - Checks if the server returns a `404` status for unknown routes.

### Best Practices in Unit Tests

1. Comprehensive Test Coverage

   - Covered **normal, edge, and failure scenarios** to ensure robustness.

2. Mocking Dependencies for Consistency

   - Used **Jest mocks** to control the output of `moment.js`, ensuring consistent test results regardless of the system time.

3. Proper Error Handling & HTTP Status Codes

   - Implemented error handling in `app.js` to gracefully handle internal failures and unknown routes.

4. Maintainable & Readable Tests
   - Used **clear test names** and grouped tests using `describe()` for better structure.
