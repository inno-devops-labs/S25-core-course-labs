# Python web application - best practices and code quality

## Framework choice: Flask
For this web application, I chose **Flask** as the web framework.

### Reasons of choice:
- **Minimalistic and lightweight**: Flask doesn’t impose unnecessary restrictions on how to structure the application, giving developers more control over the app's components.
- **Easy to learn and use**: Flask's simple design and straightforward API make it an excellent choice for quick prototyping.
- **Extensive documentation and community support**: Flask has an extensive set of resources and a large community, making it easy to find solutions and tutorials.
- **Built-in development server**: Flask includes a built-in server that makes it easy to start the app without needing to configure additional infrastructure.

Overall, Flask is a best web framework for building small to medium-sized web applications.

## Best Practices Applied

### 1. Code Organization
The project follows a clean structure:
- The **Flask app** is located in the `app/` directory, keeping everything organized.
- The **templates** for HTML files are stored in a dedicated `templates/` folder.
- **Static files** (like CSS and JavaScript) can be placed in the `static/` directory.

### 2. Use of Virtual Environments
A virtual environment (`.venv/`) is used to isolate project dependencies. This ensures that the project’s dependencies don’t conflict with those of other projects on the system.

To activate the virtual environment:
```bash
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```