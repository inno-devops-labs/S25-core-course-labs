# Go application

## Fiber web framework

This framework was chosen for the web application implementation because of its convenience
and performance. Fiber is one of the fastest web frameworks along with good ecosystem of
middlwares and other features allowing easy application building.

## Best practices

I've used [standard Go project layout](https://github.com/golang-standards/project-layout). It is very
popular and well known in community.

Configured `golangci-lint` linter was used to maintain code readability and safety.
This is most widely used and efficient Go linter.

`gofumpt` popular formatter was used to maintain code formatting.

In the implemented Go application logging is enabled for troubleshooting and debugging.

## Testing

Web application was tested with usual Go `testing` and `httptest` packages whether it is
able to return responses with 200th status code.
