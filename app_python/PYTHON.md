# Moscow Time Web-Application

## Technological Stack

For this application I have used [FastAPI](https://fastapi.tiangolo.com/).
It is modern, high-performance, easy to use Python framework.
It is appropriate for this application because it is easy and fast to develop with it.

## Best Practices

- Automatic interactive OpenAPI documentation.
- Pydantic models for response validation and serialization.
- Code documentation and comments.
- Proper code naming.
- Clean code structure.
- PEP8 coding style.

## Coding Standards and Code Quality

- I used [Black](https://black.readthedocs.io) to format the code.
- I used [isort](https://pycqa.github.io/isort/) to sort the imports.
- I used [Flake8](https://flake8.pycqa.org) to check the code style and quality.

## Testing

- I tested the application by running it and checking the displayed time in Moscow using the browser.
- Then I tested the application by refreshing the page and checking if the displayed time updates.

![First Opening](img/app_python_hand_test_1.png)
![Second Opening](img/app_python_hand_test_2.png)

## Unit Testing

### Technologies

For the unit tests, I used the following technologies:

- [Pytest](https://docs.pytest.org) - testing framework.
- [Httpx](https://www.python-httpx.org) - HTTP client for Python.
- [FastAPI TestClient](https://fastapi.tiango.com) - test client for FastAPI applications.

### Description

#### Unit test `test_get_current_time()`

This test verifies that the `/api/time` endpoint:

- Returns a `200` status code.
- Has the correct `JSON` content type.
- Contains a `time` field in the response.
- Ensures the `time` field is a valid string.
- Confirms the time format is correct using `datetime.strptime()`.
- Compares the returned time with the actual time in the specified timezone.
- Ensures the time difference between the server and response is within 1 second.

#### Unit test `test_get_current_time_html()`

This test verifies that the root (`/`) endpoint:

- Returns a `200` status code.
- Has the correct `HTML` content type.

### Best Practices

- __Constants for readability__ – defined `SECONDS_IN_HOUR`, `SECONDS_IN_MINUTE`, `MAX_DIFF`.
- __Clear assertions with messages__ – helps debugging.
- __Error handling for time parsing__ – catches incorrect formats.
- __Reusable function__ – `get_seconds(t: time) -> int` improves clarity.
- __Strict time validation__ – ensures minimal time difference (<= 1 sec).
- __Content-Type checks__ – confirms correct response format.
