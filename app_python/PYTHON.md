## Introduction

Hey there! For this lab assignment, I decided to build a very simple **Moscow Time** web application in Python. Instead of using a more complex web framework (like FastAPI, LiteStar, Django, and so on), I went with Python's built-in `http.server` module. It’s an excellent choice for quick, lightweight demos and completely satisfies our requirement to display the current time in Moscow. This approach also means we don’t add extra dependencies—just one file that is ready to run on any machine with Python installed!

## Why `http.server`?

- **Built-in and Lightweight**: Since `http.server` is included with the standard Python library, no additional installation is needed. This matches perfectly with our lab’s requirement for a simple web application.
- **Simplicity**: The lab is straightforward—show the current Moscow time. We don’t need database connections, templates, or any complex web structure. Using a minimal built-in server keeps everything lean and easy.
- **No Extra Dependencies**: A big plus for projects like this is avoiding “dependency bloat.” With `http.server`, we just run the script, and it works out of the box on any system with Python installed.

## Best Practices

1. **Clear Code Structure**  
   - An `import` section for modules.  
   - A `MoscowTimeAPIHandler` class to handle GET requests.  
   - A `main()` function to run the server to avoid cluttering the global namespace.
2. **PEP 8 Compliance**  
   - Adequate spacing (4 spaces per indent).  
   - Descriptive naming for classes and variables.
   - Linting with Ruff.
3. **Conventional Commits**  
   - I followed the [Conventional Commits](https://www.conventionalcommits.org) approach with short, descriptive commit messages (e.g., “feat: implement server returning Moscow time”). This practice keeps history readable and helps understand changes at a glance.
4. **Time Zone Handling**  
   - We explicitly set the timezone to Moscow (UTC+3) using `datetime` and `timedelta`. This ensures we always display the correct local time in Moscow.
5. **Security Considerations**  
   - Although this is a simple project, Python’s built-in server is not intended for production. For real-world scenarios, a hardened web server or WSGI server should be used.

## Coding Standards

1. **Naming Conventions**:  
   - The class name `MoscowTimeAPIHandler` follows PascalCase.  
   - Functions like `main()` use snake_case.
2. **Single Responsibility**:  
   - The handler class is solely responsible for request handling.  
   - The `main()` function only starts the server and prints a message.
3. **Modular Code**:  
   - Even though it’s short, the logic is grouped—making it easy to expand if we need more features in the future.

## Testing

1. **Manual Testing**:  
   - I ran the application locally using `python main.py`.  
   - Visited `http://localhost:8000` in my browser to ensure the server responds correctly.  
   - Refreshed the page multiple times to confirm the displayed time updates properly.
2. **Simple Verification**:  
   - Checked that it always displays the correct Moscow time (cross-checked with other world clock sources).  
   - Confirmed it handles multiple requests without error.

## Additional Setup

- **MIT License**:  
  I have included an MIT License file in the project. This keeps our code open-source and permissive for anyone to use or modify under the license terms.

- **Linting with Ruff**:  
  To maintain code quality and consistency, I used [Ruff](https://github.com/charliermarsh/ruff). Ruff checks for PEP 8 compliance and other best practices. It’s extremely fast and easy to configure within the project.

- **`pyproject.toml`**:  
  The project is configured with a basic `pyproject.toml` specifying:
  - Python version (3.12)  
  - Build and metadata information  
  - A placeholder for dependencies (in this case, we have no external dependencies)

## Conclusion

This tiny Python application was a fun way to quickly spin up a web server and showcase time zone handling! By leveraging Python’s built-in `http.server`, we avoided extra dependencies and focused on learning and applying best practices. If this application needed more complex features—like templating or database interactions—we could always switch to a full-fledged framework like FastAPI in the future.

> **Tip**: If you are running into permission issues on certain ports, pick a higher port (e.g., 8000) or run as an administrator. Also, remember that Python’s built-in server is not recommended for production-level deployments.
