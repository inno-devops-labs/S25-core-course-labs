## Framework Choice
I chose Flask for this web application because it is lightweight, easy to set up, and well-suited for small to medium-sized applications. Flask provides the necessary tools to build a simple web application quickly and efficiently.

## Best Practices and Coding Standards
- **Modular Code**: The application is structured with separate files for the main application logic (`app.py`) and the HTML template (`index.html`).
- **Timezone Handling**: I used the `pytz` library to handle timezone conversions accurately.
- **Template Rendering**: Flask's `render_template` function is used to render HTML templates, ensuring a clean separation of concerns.
- **Testing**: The application was tested manually by refreshing the page to ensure the time updates correctly.


## Unit Tests
- `test_home_route_status_code`: Verifies successful response (200 status)
- `test_home_route_time_display`: Validates correct time formatting and display

## Best Practices
1. **Test Isolation**: Each test focuses on a single responsibility
2. **Mocking**: Used to control time output for consistent testing
3. **Parameterization**: Ready for future expansion with multiple test cases
4. **CI Integration**: Tests automated in GitHub Actions