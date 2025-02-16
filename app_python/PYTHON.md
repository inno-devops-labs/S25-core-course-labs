## Framework: Flask
- **Lightweight**: Minimal setup for a simple app
- **Flexible**: Easy to extend and modify
- **Built-in Server**: No need for additional tools to run locally

## Best Practices
1. **Timezone Handling**  
   Used `pytz` for accurate timezone conversion to Moscow (MSK).

2. **Code Quality**  
   - Followed PEP8 standards  
   - Used descriptive variable names  

3. **Security**  
   - Enabled debug mode only for development  
   - Used Flask's built-in HTML escaping  

4. **Maintainability**  
   - Added `requirements.txt` for dependency management  
   - Included a `.gitignore` file  
   
# Unit Testing in the Project

## Implemented Unit Tests
We have created unit tests for `some_function` in `app_python/app.py`. These tests verify that the function returns the expected squared value for different inputs.

### Example Test Cases:
- `some_function(2) → 4`
- `some_function(3) → 9`
- `some_function(4) → 16`
- `some_function(5) → 25`
- `some_function(6) → 36`

## Best Practices Applied:
1. **Test Naming Conventions** – Each test function follows a clear naming pattern (`test_some_function_caseX`) for readability.
2. **Assertions** – We use `assertEqual` to compare expected and actual values.
3. **Isolation** – Each test is independent and does not depend on external data or state.
4. **Automated Execution** – Tests can be run using `unittest` via:
   ```sh
   PYTHONPATH=$(pwd) python3 -m unittest discover app_python/tests -v

