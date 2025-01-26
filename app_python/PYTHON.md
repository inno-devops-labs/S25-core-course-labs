# Python application

## FastAPI web framework

This framework was chosen for the application implementation because of its simplicity and popularity.
It also supports wide range of functionalities that may be applied in web application development.
In comparison with Flask, it also has asynchronous functionalities support.

## Best practices

In order to keep this project maintainable I've used simply configured
`black` code formatter and `pylint` linter.

## Testing

Web application was tested manually, refreshing the page and comparing the time with the answer of [following resource](https://www.timeanddate.com/worldclock/russia/moscow).
It can also be automated with `curl`.
