# Python Web Application

## Framework Choice: **FastAPI**

- **Justification**:
  - **High Performance**: Built on ASGI, FastAPI is significantly faster than Flask.  
  - **Modern Features**: Supports async/await, automatic data validation, and dependency injection.  
  - **Automatic Documentation**: Generates interactive API docs (Swagger UI and ReDoc).  
  - **Production-Ready**: Designed to work with Uvicorn, a production-ready ASGI server.

---

## Best Practices Applied

1. **Coding Standards**:
   - Followed **PEP8** guidelines (e.g., snake_case naming, line length ≤ 79 chars).  
   - Used `pytz` for accurate timezone handling (MSK time = UTC+3).  

2. **Code Quality**:
   - Isolated dependencies using a **virtual environment**.  
   - Used FastAPI’s built-in validation and serialization for robust API design.

3. **Project Structure**:
   - Separated application code (`app.py`) from documentation.  
   - Added `.gitignore` to exclude virtual environments and cache files.  

4. **Testing**:
   - Implemented **unit tests** using `pytest` to ensure correctness and reliability.

---

## Manual Testing

- **Verification Steps**:  
  1. Run `uvicorn app:app --host 0.0.0.0 --port 5000` and access `http://localhost:5000` in a browser.  
  2. Confirm the displayed time matches [Moscow’s current time](https://time.is/Moscow).  
  3. Explore the interactive API docs at `http://localhost:5000/docs`.

---

## Unit Tests

- **Purpose**: To validate the functionality of the `/` endpoint, ensuring it returns the correct Moscow time.
- **Framework**: Used `pytest` with `fastapi.testclient.TestClient` for testing the FastAPI application.
- **Test Description**:
  - Simulated a GET request to the root endpoint (`/`) using `TestClient`.  
  - Compared the returned time with the current Moscow time generated using `pytz`.  
  - Allowed for a small delay in execution by comparing seconds within a ±5-second tolerance.
- **Best Practices Applied**:
  - Ensured test independence by not relying on external services or shared state.  
  - Used assertions to verify HTTP status codes and response content.  
  - Included detailed time comparisons to account for potential delays in execution.

## How to Run

```bash
uvicorn app:app --host 0.0.0.0 --port 5000
