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

---

## Manual Testing

- **Verification Steps**:  
  1. Run `uvicorn app:app --host 0.0.0.0 --port 5000` and access `http://localhost:5000` in a browser.  
  2. Confirm the displayed time matches [Moscow’s current time](https://time.is/Moscow).  
  3. Explore the interactive API docs at `http://localhost:5000/docs`.

---

## How to Run

```bash
uvicorn app:app --host 0.0.0.0 --port 5000
