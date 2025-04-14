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
This application was manually tested by interacting with the web interface to ensure proper functionality and feedback.
