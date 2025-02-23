# Python Moscow Time Web App

## Framework Choice

I chose **Flask** as the framework for this project
because it is ***lightweight*** and ***easy to set up***,
making it suitable for small projects, such as displaying the current time.

## Best Practices

- **Modular Code**: The application is structured in a modular way.
  The business logic is separated from presentation through the use of templates.

- **PEP 8 Compliance**: The code conforms to PEP 8,
  Python's style guide for writing readable code, ensuring consistent formatting.

- **Naming Conventions**: snake_case is used for all variables and functions
  to enhance code readability and maintainability.

- **Code Comments**: Individual sections of the code are documented.

- **Integration testing**: Unit / Ui testing is implemented with
  Flask test client to ensure that primary functionality is valid

## Unit tests

Two unit tests that check the correctness
of the primary web page can be found at `/tests` folder

### Best practices

- **Isolate Execution**: both unit tests are independent of each other execution,
  meaning that steps that were executed for previous test are not affecting the next one.

- **Network test client**: Flask provides its own test client that not only does not depend on network conditions
  but also does not require to provide any unnecessary mocks and stubs.

- **Consistent Naming Conventions**: Tests are named according to the scenario they follow:
    * `test_time_display` - checks the correctness of the web page only once
    * `test_continuous_time_display` - checks the correctness of the web page every second for 5 seconds

- **Tests documentation**: Tests have documentation on what they are expected to cover
  and what constraints they will follow (e.g. one time request or continuous requests)
