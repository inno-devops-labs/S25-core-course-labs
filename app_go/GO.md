# Lab 1 Bonus: Go App

## Why Gin Framework?
1. **Lightweight and Fast**: Gin is ideal for creating simple and efficient web applications.
2. **HTML Template Support**: Built-in support for rendering HTML templates makes it easy to create dynamic web pages.
3. **Ease of Routing**: Gin simplifies HTTP route handling for both GET and POST requests.

## Application Description
This application is a simple "Guess the Number" game where:
- The server generates a random number between 1 and 100.
- Users submit their guesses through a form.
- The server provides feedback: "Too Low", "Too High", or "Correct".

## Best Practices
1. **Random Number Generation**:
   - The `rand` package is seeded with the current timestamp to ensure unique random numbers.
2. **Error Handling**:
   - Invalid inputs (non-numeric guesses) are handled with appropriate feedback.
3. **HTML Templates**:
   - Dynamic content is rendered using Gin's built-in template engine.
4. **Game Reset**:
   - The game resets automatically when the user guesses correctly.

## Testing
Unit tests were written to ensure the correctness and reliability of the application using the `httptest` package for simulating HTTP requests and `testify/assert` for structured assertions. The following key scenarios were tested:

1. **Homepage Loading**:
   - Ensures the main page loads successfully with a valid HTTP response and contains the expected HTML structure.

2. **Invalid Input Handling**:
   - Tests form submission with a non-numeric guess to verify the application properly handles errors and returns an appropriate message.

3. **Guess Evaluation**:
   - Tests various numeric inputs to verify whether the server correctly responds with "Too Low", "Too High", or "Correct" feedback.

4. **Game Reset Mechanism**:
   - Ensures the game resets after a correct guess by verifying that the secret number changes.

These tests follow best practices by:
- Using known values for deterministic testing.
- Checking both success and failure cases.
- Ensuring proper error handling and response codes.
- Keeping tests isolated and independent.
