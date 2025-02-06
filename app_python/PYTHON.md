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
1. **Response Status Code**:
    - Ensures that the HTTP response returns 200 OK, confirming that the endpoint is accessible.

2. **Content-Type Validation**:
    - Verifies that the response contains text/html in the Content-Type header, ensuring the returned data is HTML.

3. **Time Format Validation**:
    - Extracts the timestamp from the HTML response using regular expressions to match the format dd.mm.YYYY HH:MM:SS.
    - Checks that the extracted timestamp is present and correctly formatted.

4. **Timezone Awareness and Time Accuracy**:
   - Converts the extracted timestamp into a timezone-aware datetime object using MOSCOW_TZ.localize(extracted_time).
   - Retrieves the current Moscow time from the system (datetime.now(MOSCOW_TZ)) and calculates the time difference.
   - Asserts that the difference between the response time and the actual time is less than 5 seconds.

## Best Practices Applied for Testing
1. **Isolation of Test Cases**  
   - The test runs independently of external dependencies, such as a network calls. The FastAPI `TestClient` is used to simulate API requests.

2. **Validation of Response Type and Format**  
   - Ensures that the API response is structured correctly as an HTML page.
   - Uses a **regular expression** to extract and validate the timestamp format.

3. **Handling Timezone Differences**  
   - Avoids `TypeError` (caused by naive vs. aware datetime comparison) by explicitly making the extracted timestamp **timezone-aware** with `MOSCOW_TZ.localize()`.

4. **Tolerance for Execution Delays**  
   - Allows a small time difference (≤ 5 seconds) to prevent flakiness due to execution lag.

5. **Maintainability and Readability**  
   - Uses clear variable names (`now_moscow`, `extracted_time`, `time_difference`).
   - Includes assertions with **meaningful error messages** to make debugging easier.

6. **Automated Testing with `pytest`**  
   - The test is compatible with `pytest`, allowing seamless execution and integration into CI/CD pipelines.