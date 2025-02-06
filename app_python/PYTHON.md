# Python based web application

## Used packages

- **FastApi** to establish simple codebase without batteries.
- **Jinja2** to use the power of HTML templates as simply as the web app itself.
- **Uvicorn** to serve the app, because it is most commonly used with FastApi.

## Utilized practices

1. Exposing config variables to manipulate deployment easily.
2. Clear code and assets folders structure.
3. Gitignore and requirements files for a cleaner shared development.

## Testing

The tests were developed with the help of FastApi's **TestClient** and ran by **pytest**. This is the most straightforward way of testing a python application.

Tests implemented:

- `test_get_msk_time`: check webapp availability and correctness of displayed time.

## Notes

>We could mock functionality of getting the current time in the `main.py`, however it is not necessary as it is the builtin function.
