I chose Flask because this project is very simple and doesn't require a complex architecture or a full technology stack.
Flask is easy and quick to set up compared to other frameworks.


# Best Practices

1) **Correct Project Architecture**: The project structure is organized in a way that the code is divided into logical modules. 
For example, HTML templates and static files (CSS) are placed in the appropriate `templates`, `static` folders,
which improves the organization and readability of the code.

2) **Debug Mode**: The application runs in debug mode, which allows for quick detection and correction of errors during 
development, as well as providing detailed error messages for diagnostics.

3) **Code Modularity**: I aimed to divide the application's logic into several modules for easier expansion and better
maintainability. For example, the function for retrieving the time is placed in a separate `routes.py` file,
and the timezone settings are handled in the `config.py` file. This makes it easier to work on the project in the future
and add new features.

# Coding standards

1) Function and variable names follow the standard conventions.
2) Tabs are used for each level of indentation.
3) Code lines are not too long.

# Testing

The application was tested manually. To ensure the code works correctly, I ran the project and refreshed the page,
checking that the displayed time matches the current time in Moscow.

# Code quality

I ensured code quality by following best practices and coding standards. This included using proper naming conventions,
maintaining consistent indentation, and keeping the code clean and well-structured.
