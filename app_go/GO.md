# Go application

## Framework Choice

Gin simplifies building web applications. It was used in official tutorial from go.dev for RESTful API, so I decided to leave it as it is.

## Best practices

- Use of typed structs for JSON unmarshalling
- Error logging after actions which may lead to unexpected errors
- Removing API keys from the code by using `.env`
- Used `gofumpt` (strict formatter), `golines` (shorten long lines) and `goimports-reviser` (sort goimports) plugins, which autoformats accordingly on the save

Tesing done by hands, since no requirement for any written tests.
