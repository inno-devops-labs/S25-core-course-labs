# Python Web Application Documentation

I chose Flask for this web application because it is lightweight, easy to set up, and well-suited for small projects
like displaying current time. Flask provides a simple setup and allows for quick development and testing of web
applications.

## Unit Testing

### Unit Tests Implemented
1. **Test Index Route**:
   - Verifies that the root route (`/`) returns a status code of `200` and contains the text "Current Time in Moscow".

### Best Practices Applied
- **Test Isolation**: Each test is independent and does not rely on the state of other tests.
- **Fixtures**: Used `pytest` fixtures to set up the Flask test client.
- **Assertions**: Used meaningful assertions to validate the response data and status codes.