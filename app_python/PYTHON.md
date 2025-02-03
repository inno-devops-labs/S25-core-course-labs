# Python application

## FastAPI web framework

This framework was chosen for the application implementation because of its simplicity and popularity.
It also supports wide range of functionalities that may be applied in web application development.
In comparison with Flask, it also has asynchronous functionalities support.

## Best practices

In order to keep this project maintainable I've used simply configured
`black` code formatter and `pylint` linter.

## Testing

`pytest` Python framework together with `fastapi.TestClient` is used to comprehensively test an application.

Tests check

- whether time returned by API is actually correct
- whether the page with time returned by API will be updated after some time
