# Python Web Application: The Current Moskow Time

## Framework

The **Flask** framework was selected for the web application because it provides all the essential features for developing small web applications and is simple to install and use.

## Best Practices

1. **Project Structure**  
   - A dedicated folder for the app `app_python`.
   - Documentation files `PYTHON.md` and `README.md`.
   - The file `requirements.txt` for managing Python dependencies.
   - A clean `.gitignore` file to exclude environment files.
   - Unit tests in `test_app.py`.

2. **Coding Standards**  
   - Code is written to follow **PEP-8** Style Guide for readability (e.g., consistent spacing, line length, naming conventions).

3. **Testing**  
   - The code is manually tested by running the Flask development server and refreshing the page to see the change in Moscow time.

## Unit Tests

Python’s built-in `unittest` framework is used for the project. Unit tests cover:

1. **Status Codes**: Ensuring `/` returns an HTTP `200 OK` status code.
2. **Content**: Verifying that the header `"The current time in Moscow:"` appears on the page.
3. **Time Format**: Using a regex to check if the time follows an `HH:MM:SS` pattern.
4. **HTML Tags**: Confirming `<h1>` and `<h2>` tags appear in the response.
