## Framework choice

The framework used for this app is **Flask**: 
It is relatively easy to use and does not require any additional modules, wich is perfect for small apps like this.

The unit tests for this application are written using the `unittest` framework. The following tests have been implemented:

1. **Test Moscow Time Response**:
   - Verifies that the application returns the correct Moscow time in the expected format.
   - Uses mocking to simulate a fixed time for consistent results.

2. **Test Invalid Route**:
   - Ensures that the application returns a 404 error when an invalid route is accessed.

## Best practices applied

1. **Code Organization**
    - Separated application logic into modules to maintain clarity and scalability.
    - Followed a clean directory structure with clearly named files.

2. **PEP 8 Compliance:**
   - Used tools like `flake8` to ensure adherence to PEP 8 standards.
   - Indented properly, named variables meaningfully.

3. **Performance Optimization:**
    - Used efficient libraries for time and date manipulation (e.g., `pytz`).
    - Minimized unnecessary computation and reduced the app's response time.

4. **Isolation**
    - Each test is isolated and does not depend on the state of other tests.

5. **Mocking**
    - Used mocking to simulate the `datetime` module to ensure consistent test results.

6. **Assertions**
    - Used appropriate assertions to validate the response status code and content.

7. **Test Coverage**
    - Ensured that both valid and invalid routes are tested.