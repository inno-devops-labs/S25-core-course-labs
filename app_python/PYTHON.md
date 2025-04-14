# Moscow Time Web-Application

## Framework Selection

I chosed FastAPI for this project because I'm already familiar with it, and it offers excellent performance, automatic validation, and ease of use for building modern web applications.

## Best Practices Followed

- The application was made as a python module so that unexpected import errors etc can be avoided.
- App route and logic is kept in separate files so that making changes get better.
- Code is formatted according to PEP8 standards.
- Clean code structure.
- Code documentation and comments.

## Coding Standards and Code Quality

- To have an unified coding styles, `black` was used
- To check the code style and quality, `Flake8` was used
- To sort and organize your import statements, `isort` was used.

## Testing

- I tested the application by running it and verifying that the displayed time in Moscow was shown correctly in the browser.

![First Opening](img/1.png)

- Then, I refreshed the page to ensure that the time updated properly.

![Second Opening](img/2.png)

## Unit Tests

The unit tests are currently maintained in a single `test.py` file. While it is typically recommended to organize tests into separate directories, this approach was chosen due to the small number of functions being tested. Tests for `app.py` were not written, as it simply wraps the `show_time` function, which is already tested. Additionally, testing `app.py` would be considered part of `integration testing` rather than `unit testing`. Several best practices were followed while writing the tests.

- Tests are fast and simple
- Each test works for individual functions
- All tests are deterministic
- Both positive and negative tests are maintained
- Code coverage is 95%. but 95% is covered here due to the simplicity of the project.
