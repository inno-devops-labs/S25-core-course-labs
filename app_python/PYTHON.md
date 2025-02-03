## Framework Choice: Flask

For this assignment, I chose the Flask framework because it avoids unnecessary complexity 
and provides enough functionality to complete this task.

## Best Practices Applied

1. **Modular Design**: The application is structured into separate modules for better maintainability and scalability.
2. **Code Documentation**: The code includes meaningful comments for better readability.
3. **Timezone Accuracy**: Time handling is managed with the `pytz` library for better precision.
4. **Dependency Management**: The `requirements.txt` file was generated using `pipreqs`, ensuring only necessary libraries are included.

## Coding Standards

1. **PEP 8**: The code follows PEP 8 for consistency and clarity.
2. **Clear Naming**: Variables and functions are named descriptively for better readability and maintenance.

## Testing

Performed manual testing by reloading the web page to verify that the Moscow time updates correctly.

## Ensuring Code Quality
Used `flake8` to check the code style.

## Unit tests

1. `test_moscow_time_calc`: Checks that the displayed Moscow time is correctly calculated and formatted.
2. `test_home_page_rendering`: Checks that the homepage (`/`) renders the correct template containing "Moscow Time:".

## Best practices for Unit tests

1. **setUp method**: Initializes the test client before each test, ensuring isolation and avoiding duplication.
2. **Descriptive Naming**: Clear test names indicate what’s being tested.
3. **Test Isolation**: Each test runs independently and does not rely on others.
4. **Assertions Usage**: Assertions validate expected behavior.