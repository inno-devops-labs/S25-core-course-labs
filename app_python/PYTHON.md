# Python Web Application - Current Time in Moscow

## Framework Chosen: Flask

**Flask** was chosen due to its:
- Simplicity and flexibility
- Lightweight design ideal for small-scale apps
- Minimal setup requirements
- Built-in templating support

---

## Best Practices Followed

- **Timezone Handling**: Used `pytz` to correctly represent Moscow time with timezone awareness.
- **Separation of Concerns**: The business logic is handled in `app.py`, and presentation logic is handled in `templates/index.html`.
- **Minimal Dependencies**: Only necessary packages are used (`Flask`, `pytz`).
- **Clean HTML**: Used semantic and minimal HTML structure for clarity and accessibility.
- **Docstrings & Comments**: Each function is documented with clear and concise docstrings.
- **PEP8 Compliance**: Code adheres to Python’s official style guide.

---

## Linting and Code Quality

To ensure code cleanliness and maintainability, linting tools were used:

### Tools Used
- **flake8** – For basic PEP8 checks, unused imports, and line length.
- **pylint** – For in-depth analysis, docstring checks, import order, and code rating.

### 🧼 Linting Commands

```bash
flake8 app.py
python3 -m pylint app.py
```

## Manual Testing Strategy

- Visited http://127.0.0.1:5000/ in browser.

- Refreshed the page to verify that time updates.

- Verified correct formatting (YYYY-MM-DD HH:MM:SS) for Moscow timezone.

- Checked HTML rendering and ensured no server-side errors occurred.

---

## Unit Tests and Best Practices

###  Unit Tests Written

- `test_home_status_code`: Verifies that the home route (`/`) returns HTTP 200.
- `test_home_content`: Ensures the page contains the expected heading text.
- Uses `pytest` and `Flask`’s test client fixture.

### Best Practices Followed

- Test function names are descriptive and readable.
- `pytest` fixtures used for cleaner setup and teardown.
- Coverage of both response code and content.
