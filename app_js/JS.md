# JavaScript Testing Guidelines

## Unit Tests

We use [Jest](https://jestjs.io/) and [Supertest](https://github.com/visionmedia/supertest) for unit testing our Express application. Tests are located in the `tests/` directory.

### Test Strategy
- **Setup:** The tests import the Express app from `app.js` without starting the actual server.
- **Assertions:** Tests check that the response status is 200 and that the HTML response contains the text "Current Time in New York:".
- **Isolation:** Each test is self-contained, ensuring no cross-test interference.

## Best Practices
- Write tests that clearly indicate their purpose.
- Use libraries like Supertest to simulate HTTP requests.
- Maintain tests in a separate directory (`tests/`) for clarity.
