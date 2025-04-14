# Python Web Application Documentation

## Framework Selection
**Flask** was chosen for its ease of use and effectiveness in small-scale applications. It enables rapid development with minimal complexity.

## Development Best Practices
- **Coding Standards:** Adhered to PEP8 guidelines, used descriptive variable names, and modularized HTML into templates.  
- **Testing:** Employed `pytest` for unit testing to ensure route functionality.  
- **Code Quality:** Maintained clean project structure, utilized `flake8` for linting, and enforced coding best practices.

## Unit Testing
- **Test Coverage**: Tests validate the `/` route and ensure the time is displayed in the correct format.
- **Best Practices**:
  - Used `pytest` for test automation.
  - Mocked dependencies (e.g., timezone) to isolate tests.
  - Followed AAA (Arrange-Act-Assert) pattern.