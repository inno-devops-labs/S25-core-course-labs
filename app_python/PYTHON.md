## Flask Framework
For this exercise, I chose Flask due to its simplicity. The task doesn’t require heavy infrastructure, so, for example, Django unnecessarily complex for this task. Flask's lightweight nature makes it perfect for small to medium-sized projects like this one.

---
## Best Practices
- Use logging for every request made to the page  
- I followed PEP 8 guidelines  
- Use `venv` for dependency management
- Using **Docker container** for easy deployment

---
### Unit Tests

#### ✅ Test Cases Implemented

- **test_moscow_time**: Ensures that the endpoint `/` returns a successful response and contains the expected "Moscow time :" text.
- **test_time_format**: Validates that the returned timestamp follows the format `%Y-%m-%d %H:%M:%S`.

#### 🧪 Testing Approach

- Used `pytest` for writing and executing tests.
- Applied the `pytest.fixture` mechanism to set up a test client for the Flask app.
- Verified response status codes and output correctness.