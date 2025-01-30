# Python Web Application Details

## Framework Choice

**Framework Used**: Flask  
**Reasoning**:

- Lightweight and straightforward to set up for a simple app.
- Large community support and extensive documentation.
- Easy to integrate with testing tools and follow best practices.

## Best Practices

1. **Proper Folder Structure**:
   - We keep our application code (`main.py`), documentation (`README.md`, `PYTHON.md`), and dependencies (`requirements.txt`) separate.
2. **Version Control**:
   - Using `.gitignore` to exclude unnecessary files (e.g., virtual environments, compiled bytecode).
3. **Dependency Management**:
   - Minimal dependencies listed in `requirements.txt`.
4. **Code Readability**:
   - Clear function names and docstrings.
   - Consistent use of Pythonic conventions, including PEP 8.
5. **Error Handling** (if expanded):
   - In more complex applications, use error handlers to return meaningful error messages.

## Coding Standards

- Followed [PEP 8](https://peps.python.org/pep-0008/):
  - Indentation with 4 spaces.
  - Descriptive naming for functions/variables.
  - Line length typically 79-100 characters.
- Used docstrings to explain the purpose of routes.

## Testing & Code Quality

- **Manual Testing**:
  - Run `python main.py` and open `http://127.0.0.1:5000/` in a browser, verifying the displayed time.
  - Refresh the page to confirm the time updates.
- **Linting**:
  - Tools like `flake8` or `pylint` ensure code style and potential error checks.
