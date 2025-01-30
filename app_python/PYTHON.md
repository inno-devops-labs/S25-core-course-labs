# Python Web Application: Best Practices

## Framework Choice
**Flask** was chosen because:
- Lightweight and minimal boilerplate.
- Easy to set up for small applications.
- Built-in development server for testing.

## Best Practices Applied
1. **Virtual Environment**:
   - Used `venv` to isolate dependencies.
   - Added `requirements.txt` for reproducibility.
2. **Coding Standards**:
   - Followed PEP8 guidelines.
3. **Testing**:
   - Added unit tests with `pytest`.
   - Verified time updates on page refresh.
4. **Time Zone Handling**:
   - Used `pytz` to fetch Moscow time (avoids server timezone dependency).