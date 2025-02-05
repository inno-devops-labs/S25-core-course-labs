# Best Practices Applied in the Web Application

1. **Type Annotations**:  
   - Used type hints in function signatures to improve code readability and ensure type safety.

2. **Asynchronous Programming**:  
   - Used an asynchronous server (ASGI) with coroutines for handling endpoints, ensuring that requests are processed concurrently and efficiently, especially under high load.

3. **Timezone Management**:  
   - Used the `pytz` library to handle timezone-aware datetime operations, ensuring accurate time representation for Moscow.

---

## Coding Standards

- **Code Linting and Formatting**:  
  - Integrated **Ruff** to enforce PEP 8 standards and maintain consistent style across in the code

- **Adherence to PEP 8**:  
  - Followed PEP8 format

---

## Testing

1. **Unit Testing**:  
   - Implemented tests for the `/msc_time` endpoint using FastAPI's `TestClient`.
   - Verified response formats and ensured time accuracy within a defined tolerance.

2. **Automated Testing**:  
   - Used `pytest` for running the test suite
