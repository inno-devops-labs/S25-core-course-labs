# Moscow Time Web App

## Framework

For this web application I chose `Flask` because it is lightweight, fast to set up, and overall one of the best choices for small sized projects. Moreover, `pytz` is used to ensure correct timezone conversion.

### Applied practices

- **Flask coding conventions**: practices taken from [Explore Flask]("https://explore-flask.readthedocs.io/en/latest/conventions.html"), a book about the best practices in `Flask`.
- **Testing**: app was tested locally to ensure that it works correctly.
- **Other**: virtual environment was used during development to ensure stable, and portable environment.

## Unit Tests

### Tests

- `test_status_code`: verifies that the `/` endpoint returns a status code of 200.

- `test_accuracy`: verifies that the time returned by the `/` endpoint is accurate within an allowed inaccuracy of 10 seconds.

### Best practices

- **Fast tests**: use small and fasts tests to avoid slowing down the development.
- **Test one thing**: each test should target one functionality.
- **Single assert**: use single assert tests to make code more maintainable.
