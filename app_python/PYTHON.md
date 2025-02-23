# Python Web Application Documentation

## Framework Choice: Flask

Flask was chosen for this web application due to its lightweight nature and flexibility, making it ideal for developing simple to moderately complex applications. Its minimalistic design allows for easy customization and scalability.

## Best Practices Applied

1. **Virtual Environment:**
   - Utilized a virtual environment to manage project dependencies, ensuring an isolated and consistent development environment.

2. **Code Organization:**
   - Structured the application with separate folders for templates to maintain a clean and organized codebase.

3. **Use of `requirements.txt`:**
   - Listed all dependencies in `requirements.txt` to facilitate easy installation and version control.

4. **Error Handling:**
   - Implemented basic error handling by using Flask’s built-in debugging mode during development.

## Coding Standards

- **PEP 8 Compliance:**
  - Followed PEP 8 style guidelines to ensure readable and maintainable code.
  
- **Descriptive Naming:**
  - Used clear and descriptive variable and function names for better code clarity.

## Testing

- **Manual Testing:**
  - Verified that the application displays the current Moscow time accurately.
  - Ensured that refreshing the page updates the time accordingly.

## Code Quality

- **Readability:**
  - Maintained high code readability through proper indentation, commenting, and logical structuring.

- **Modularity:**
  - Designed the application with modularity in mind, allowing for easy future expansions or feature additions.

## Unit Tests Documentation

### Test Framework: pytest

I use pytest for our testing framework due to its simplicity and powerful features.

### Tests Implemented

1. **Home Page Test (`test_home_page`)**
   - Verifies that the home page returns a 200 status code
   - Checks if the page contains the expected heading
   - Ensures the basic functionality of the Flask application

2. **Time Format Test (`test_moscow_time_format`)**
   - Validates the correct formatting of Moscow time
   - Ensures the time string follows the expected format (YYYY-MM-DD HH:MM:SS)

### Best Practices Applied in Testing

1. **Test Fixtures**
   - Used pytest fixtures for setting up test client
   - Ensures clean test environment for each test

2. **Isolated Tests**
   - Each test focuses on a single functionality
   - Tests are independent of each other

3. **Clear Test Names**
   - Descriptive test names that indicate what is being tested
   - Makes it easy to identify test purposes

4. **Assertions**
   - Specific assertions that check exact conditions
   - Clear failure messages for debugging
