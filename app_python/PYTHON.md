# Lab 1: Web Application Development

## Framework

For this task I chose `flask` because the project we are working on is small and simple which makes a framework like `flask` a great fit for the task

## Best practices applied

- **Separation of Concerns:** The logic and the presentation in the app are sperated following the Model-View-Controller (MVC) pattern
- **Minimalistic and effecient code:** The code does exactly what it should do without any extra features and unecssary complexity, making it easier to understand and maintain

## Code standards and code quality

- **PEP8 Compliance:** The code follows PEP8, making it easier to read and understand
- **Clear and descriptive names:** The use of descriptive names for the function and variables in the code making it easier to understand code
- **Documented code:** The code is documented making it easer to read and understand the code's workflow

## Unite testing

- **Overview:**
  - The unit test simply checks if the app is working by first checking if the homepage is loading by checking the status code, then it checks if the structure of the app is correct by checking some elements in the homepage and the time format
- **Best practices followed:**
  - Using `pytest.fixture` which improves the test's maintainability and avoids redundant code
    - Using Regex to validate dynamic content, since the time in the app is not constant, ensuring correct time format without checking specific values
    - Checking the HTTP status code to ensure that the application responds correctly and is accessible
