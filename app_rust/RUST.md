# Rust Web Application

## Framework choice

I chose `Rocket` framework because I have a little experience with it, and this framework is one of the most common frameworks for `Rust`.
`Rocket` has all possible functionalities that can be used in web development.

## Best practices

- Code is well-commented and has documentation for further usage.
- Code passes `cargo check` and `cargo clippy`

## Testing

This Rust application has been tested using unit tests within the Rocket framework. The testing process ensures the availability, correctness, and expected behavior of the web application that displays the current time in Moscow.

The application includes three primary tests:

1. **Availability Test**: Uses Rocket's test client to send an HTTP request to the root endpoint (`/`) and verifies that the response status code is `200 OK`.

2. **HTML Structure Test**: Extracts the response body and checks for the presence of an `<h1>` tag containing timestamp checked by regexp.

3. **Time Display Test**:
     - Captures the current UTC time before making the request.
     - Extracts the time displayed in the response body.
     - Converts it to UTC and ensures it falls within the expected range between the recorded pre- and post-request timestamps.

## Testing Best Practices

- **Write Isolated Tests**: Each test runs independently using Rocket's test client, preventing flaky results and simplifying debugging.
- **Avoid Infrastructure Dependencies**: Tests run entirely within Rocket's test framework without requiring an actual web server.
- **Leverage Regular Expressions**: The validation of HTML structure and timestamps is performed using regex to ensure flexible and reliable pattern matching.
