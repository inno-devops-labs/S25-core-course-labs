# Random Quote By Taylor Swift Web Application

## Framework:

The application uses Spring Boot for handling server-side logic.

## Best practices:

1. The project follows standard Java naming conventions and organizes code into controllers for better structure.
2. The project uses Maven for managing dependencies efficiently.
3. The application is designed to support additional albums and quotes with minimal code changes.
4. CSS and images are placed in the /static folder to ensure proper delivery.

## Coding standards:

- Album and quote data is organized using Java Map and List for ease of manipulation and extension.

- Randomization is handled using the java.util.Random class, ensuring varied quotes on each request.

## Testing:

Testing was done manually by verifying the following:

- Random quotes and albums display correctly.
- The appropriate image matches the album.
