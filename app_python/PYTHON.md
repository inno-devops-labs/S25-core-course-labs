# Python Web Application (Django)

## Why Django?
- Django follows the **Model-View-Template (MVT)** architecture.
- Model(M) handles the database and business logic, View(V) contains the logic to process user requests and return responses, and Template(T) manges the HTML structure and presentation.
- This all makes the codebase more maintainable and scalable.
- Built-in admin panel, security features, and easy routing.

## Best Practices:
- Used `pytz` for timezone accuracy.
- Followed Django's **MVT architecture**.
- Structured project properly with `views.py` and `urls.py`.
- Used `.gitignore` to ignore unnecessary files.

## How to test time_app?
- Run server and check that current moscow time is present on website, check that displyed time updates upon refreshing the page.

# Unit Testing Best Practices for Django

## Unit tests
The tests ensure that the `moscow_time` view:
- Returns a valid HTTP response.
- Displays a correctly formatted timestamp.
- Shows the actual Moscow time within an acceptable margin.

## 2. Best practices applied
1. **Test Independence:** Each test runs independently to avoid unintended interference.
2. **Automated Assertions:** Using `assertEqual`, `assertIsNotNone`, and `assertLessEqual` ensures correctness.
3. **Regular Expressions for Validation:** The response is checked for correct date-time format using regex.
4. **Time Accuracy with Allowance:** A 5-second tolerance ensures tests don't fail due to execution delays.
