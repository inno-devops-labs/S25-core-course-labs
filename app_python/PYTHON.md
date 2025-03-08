# Task 1. Framework Choice: FastAPI

I have selected FastAPI for this project because:

- High performance
- Minimal boilerplate code

For a simple time display application, FastAPI's lightweight nature and ease of setup make it an ideal choice

## Template: Jinja2

Selected Jinja2 because:
- Simple syntax
- Great performance
- Easy integration with FastAPI (Jinja2Templates)

# Task 2. Best Practices Applied

## Code Structure
- Modular organization with separate routes and templates
- Clear file hierarchy
- Separation of concerns (routing, templates, business logic)

## Code Quality
- PEP 8 compliance
- Descriptive variable and function names
- Proper documentation using docstrings

## Testing Implementation
- pytest for automated testing
- Coverage of main functionality:
  - Time format validation
  - Moscow timezone accuracy
  - HTML structure verification
  - API endpoint testing

## Project Standards
- Clean .gitignore file
- Comprehensive requirements.txt

## Testing Implementation Details

The project implements comprehensi testing using pytest and FastAPI TestClient. Main test categories include:

1. Interface Testing (test_root_endpoint)
   - Validation of correct HTML page rendering
   - Verification of key interface elements presence
   - Checking required CSS classes for styling

2. API Testing (test_time_endpoint)
   - JSON response structure validation
   - Time format verification
   - HTTP status code validation

3. Time Accuracy Testing (test_time_accuracy)
   - Comparison of returned time with reference Moscow time
   - Acceptable margin of error within 2 seconds
   - Proper handling of Moscow timezone

4. HTML Structure Validation (test_html_structure)
   - Verification of all required HTML elements
   - JavaScript time auto-update code validation
   - Meta tags and page title checking

Each test is developed following best practices:
- Test isolation
- Clear test naming reflecting their purpose
- Informative error messages