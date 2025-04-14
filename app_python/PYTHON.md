## Framework Choice

For this project, I chose Flask web framework because it is lightweight, simple to use, and very extensible. With Flask, one can easily create small applications like this one without having to write too much boilerplate code. Also, Flask is well-documented and has a huge community of developers, which makes it perfect for both starters as well as professionals.

## Best Practices

- **Function Naming**: Functions were named appropriately (`moscow_time`) to reflect their purpose clearly.
- **Modular Code**: I separated concerns by keeping the route logic simple and contained.
- **Timezone Handling**: The `pytz` library is used for accurate timezone calculations, which ensures the application is reliable and correct.
- **PEP 8 Compliance**: The code follows Python’s PEP 8 style guide, including proper indentation and function naming conventions.
- **Testing**:
  - Unit tests were implemented using the `unittest` framework.
  - The following tests were added:
    - **Response Status Test**: Ensures that accessing the `/` route returns a `200 OK` status.
    - **Content Test**: Checks that the response contains the expected text (`Current Time in Moscow:`).
  - The tests are located in the `app_python` directory and are executed as part of the CI workflow.
  - The CI workflow runs automated tests using `unittest` to ensure correctness.

These best practices help maintain code quality, readability, and reliability.
