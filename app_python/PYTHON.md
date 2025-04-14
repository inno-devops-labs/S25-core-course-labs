# Python Web Application

## Task 1

### Choose a suitable framework for your web application and justify your choice

I chose Flask because:

1) I have an experience using this framework
2) It is suitable for small applications
3) It is easy to use, test and debug

## Task 2

### Describe best practices applied in the web application

1) Separation of Logic: The current_time function encapsulates the logic for fetching and formatting Moscow's time
2) PEP 8 Compliance: Code follows Python's style guide for
3) Debug Mode: app.run(debug=True) allows efficient debugging during development

### Explain how you followed coding standards, implemented testing, and ensured code quality

I followed the following coding standards:

1) PEP 8 Compliance
2) Descriptive naming: moscow_tz, current_time names are clear

**Testing:**

Obviously, I checked that the time is correct.
As it was stated I checked that the displayed time updates upon page refreshing.
Moreover, I made sure it works properly for smaller browser tab window.

**Code quality:**

The code runs without errors, the code is light and scalable.

## Unit Tests

### Describe the unit tests and the best practices you applied

Unit tests are written using pytest.
test_current_time_status_code - checks if the response returns code 200 (success)
test_current_time_content - checks if the string "Current time in Moscow" is present in the response

I have applied the following practices:

1) Used pytest.fixture to provide a reusable Flask test client
2) The TESTING mode is enabled to disable error catching and improve debugging
3) Isolation of Tests: each test function is independent
