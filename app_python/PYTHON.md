# Lab 1

## Framework: FastAPI

### Why FastAPI?
1. **Ease of Use**: FastAPI provides a simple and intuitive interface for building APIs.
2. **Lightweight and Fast**: It is optimized for performance, suitable for small projects like this and scalable for larger applications.

## Best Practices
1. **SoC (Separation of Concerns)**:
   - The logic to calculate the current Moscow time is isolated in a single function, making it reusable and testable.
   
2. **HTML Response**:
   - The application uses `HTMLResponse` to return a HTML page instead of plain JSON.

3. **PEP 8 Compliance**:
   - The code is formatted to apply to PEP 8 standards.

4. **Testing**:
   - The application includes automated tests using `pytest` and FastAPI’s `TestClient`.
   - Tests check for correct status codes, HTML structure, and date format to ensure the application acts as expected.

5. **Documentation**:
   - Comprehensive documentation is provided in Markdown files (`PYTHON.md` and `README.md`), making it easier for others to understand and use the application.

6. **Dependencies**:
   - A `requirements.txt` file is created to specify the dependencies, ensuring that application can be easily installed.

## Testing and Code Quality
1. **Testing**:
   - Used `pytest` for unit testing.
   - Verified that the application correctly renders the current Moscow date in `dd.mm.YYYY HH:MM:SS` format.
   - Validated the HTML structure in the response.

2. **Testing By Hand**:
    - Checked by hand in browser.
    - Simulated high load (100 users per second)

3. **Code Quality**:
   - Used meaningful variable and function names for better readability.

4. **Git Practices**:
   - Maintained a clean `.gitignore` file to exclude unnecessary files (e.g., `__pycache__`).