# Python Web Application Development

I chose Flask for this web application because it is lightweight, easy to set up, and well-suited for small projects
like displaying current time. Flask provides a simple setup and allows for quick development and testing of web
applications.

## Development Best Practices

- **Use a Minimal Base Image** The python:3.9-slim image is used to reduce the size of the final Docker image.
- **Avoid Running as Root** A non-root user (`appuser`) is created and used to run the application for improved security.
- **Code Quality:** Maintain code quality by adhering to PEP 8 standards and comments to make code more readable.
- **Gitignore:** Keep the .gitignore file clean to prevent sensitive data and unnecessary files from being tracked.

