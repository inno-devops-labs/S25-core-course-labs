# Python Web Application. Current time in MSK

## ✅ Code Structure & Best Practices
- **Separation of Concerns**: Flask follows MVC-like architecture: **HTML** in `templates/`, **styles** in `static/`
- **Modular Design**: The app is structured with separation between logic, templates, and static files
- **Environment Variables**: The `web.py` uses host `"0.0.0.0"` and port `5000`
- **PEP 8 Compliance**: Code follows PEP8

## ✅ Timezone Setup
- `pytz` to accurately fetch **Moscow Time**
- Ensures that the displayed time updates dinamicaly

## ✅ Code Quality and Testing
- **Linting**: Used `flake8` and `pylint` for code cleanliness and finding potential errors
- **Logging**: Can be enhanced using Python’s `logging` module for debugging
- **Unit Testing**: Unit tests can be added with `pytest`. Unit test is implemented in `unit_test.py` file
