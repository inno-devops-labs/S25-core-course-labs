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

This application was tested automatically using `testing` package. There are two tests:

- `TestJokeJson`: tests if the random joke is returned correctly in JSON format. It checks if the status code is 200, and then checks if the JSON body contains a random joke.
- `TestJoke`: tests the web page containing a random joke. Basically it tries to open the web page, checks if the status code is 200, and then checks if the web page contains a random joke.

Best practices applied:

- tests have only private dependencies (they are not shared), so the tests may be run independently
- tests are protecting from bugs - they test that the displayed time is correct (and therefore changing)
- tests are resistive to code refactoring - they only test the web application logic (i.e. the correctness of time)
- tests have a quick feedback since they run fast
- tests are simple to understand from the code and easy to run
