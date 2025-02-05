# Python Web Application

## Framework choice
**I selected Flask as the framework because of this reasons:**
1. I already worked with Flask on other projects.
2. It is lightweight, easy to use and it is the best for small web applications.
3. It also widely used and well-documented.
4. Flask is flexible and can grow with additional features if needed in the future.

## Best Practices Applied
1. **Coding Standards:**
   - Followed PEP 8 guidelines for Python coding style to maintain readability and consistency.
   - Used descriptive variable names (e.g., moscow_tz and current_time) to make the code self-explanatory.
   - The application logic is simple and modular, making it easy to understand and maintain.
  
2. **Code quality and testing**
   - Added comments to clarify important parts of the code
   - Used consistent indentation and spacing to enhance readability.
   - The application was tested locally and verified that the time displayed when the web page was refreshed was updated. The testing process also included verifying 
     the clock format and accuracy against real Moscow time to ensure that Flask's embedded development server could run the application smoothly.

3. **Timezone Menegement**
   - Utilized the **pytz** library to ensure accurate, dynamic and reliable timezone handling for Moscow.

## Code Testing

### Best Practices Applied
    - Followed PEP 8 guidelines for clean and readable code.
    - Used unittest framework for writing automated tests.
    - Checked edge cases, such as incorrect timezones or missing dependencies.
    - Tested the Flask route to ensure it returns the expected response.

### Unit Tests
I wrote unit tests for:
- Checking if the Flask app initializes correctly.
- Validating the HTTP response from / route.
- Ensuring the returned time format is correct.
