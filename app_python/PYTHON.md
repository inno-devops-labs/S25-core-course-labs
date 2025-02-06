# Python Web Application

## Framework Choice

I chose **Flask** because:

- It is easy to find documentation and tutorials to work with.
- It is lightweight and efficient for small applications.
- It provides a simple structure and quick setup.
- It allows easy integration with templates.

## Best Practices Followed

- **Code Quality**: Followed PEP8 coding style.
- **Separation of Concerns**: Used Flask with templates to keep the logic separate.
- **Testing**: Manually tested by refreshing the page and checking the time update.

## How the App Works

- It fetches the current time in the **Europe/Moscow** timezone using `pytz`.
- The time updates every time the page refreshes.

## Unit Testing

- **Using `pytest`**: A lightweight and powerful test framework.
- **Fixture for test client**: Ensures Flask app is tested in isolation.
- **Multiple test cases**:
  - Homepage loads successfully.
  - Moscow time is displayed correctly.
- **Automated CI integration**: Tests run in GitHub Actions.
