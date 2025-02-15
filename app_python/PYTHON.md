# Framework to work with: FastAPI

## Explaining the choice of framework
FastAPI is fast, easy to learn. Applications like **"Moscow Time"** can be written very quickly. There are many more advantages of FastAPI, but it is enough for this app.

## Best Practices
1. **Code Structure**: It is the simplest version but easy to navigate and run the app. One `main.app` file with all routes inside.
2. **Package management**: Used `requirements.txt` for dependencies.
3. **Testing**: Easy to write tests for more complex apps. I didn't use them as the app is easy to launch and refresh the page to see that the time changes in real time.
4. **Handling specific timezone**: Used the `pytz` library for Moscow timezone.

## Unit tests best practices
1. **Use of `pytest`**: It is lightweight and provides powerful.
2. **Regex Validation**: Used regex to confirm that the returned timestamp follows the `YYYY-MM-DD HH:MM:SS` format.
3. **Project Structure**: Created a `tests/` directory. Used `test_*.py` naming convention to allow pytest to discover tests automatically.