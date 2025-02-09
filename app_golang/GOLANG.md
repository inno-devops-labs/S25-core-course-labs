# Lab 1: Web Application Development

## Framework choice

I have chosen:

- **Gin** _for web application development_. [Gin](https://github.com/gin-gonic/gin) is a performant HTTP web framework written in Go. It features a Martini-like API with better performance, up to 40 times faster. I believe that it is a good choice, especially for such simple applications. Moreover, it supports the template execution, which is useful for this particular case.
- **net/http** _for HTTP client and server implementation_. [net/http](https://pkg.go.dev/net/http) is a Golang package used for HTTP client and server implementation. In this particular case, I used the code statuses from this package.
- **time** _for time formatting_. [time](https://pkg.go.dev/time) is a Golang package used for measuring and displaying time. In this particular case, I used the code to get the current time in Moscow and format it to the human-readable format.

## Implemented Best Practices

- **Logic separation** - the application logic is implemented in `main.go`, UI is implemented in `templates` directory and the endpoints logic is implemented in `endpoints` package.
- **Documentation** - all functionalities of this application are documented. The Swagger documentation includes possible response codes and bodies, and the list of all available endpoints.
- **Linting and formatting** - I have used [staticcheck](https://staticcheck.dev/) for code linting and [gofmt](https://pkg.go.dev/cmd/gofmt) for code formatting.
- **BEM methodology** - [BEM](https://en.bem.info/methodology/) helps to create extendable and reusable interface components. It was used in the HTML template.

## Testing

This application was tested manually by refreshing the page and checking if the joke was fetched and displayed correctly.
