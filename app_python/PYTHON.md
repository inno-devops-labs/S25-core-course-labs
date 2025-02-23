# Python Web Application

## Framework choice

To develop this web application, I chose the [**bottle**](https://bottlepy.org/docs/dev/) web framework for Python. Bottle is a lightweight Python framework, making it ideal for small, straightforward applications like this one.

## Best practicies

I implemented following Python best practices:

* Follow PEP 8 Code Style

* Documenting code with Docstrings and Comments

* Using pre-commit hooks with following tools:

  * [`black`](https://github.com/psf/black) code formatter

  * [`flake8`](https://github.com/PyCQA/flake8) code checker

  * [`isort`](https://github.com/PyCQA/isort) library sorter

  * [`mypy`](https://github.com/python/mypy) static type checker

  * [`bandit`](https://github.com/PyCQA/bandit) security analyzer

  * [`pylint`](https://github.com/pylint-dev/pylint) static code analyser

* Maintain a clean `.gitignore` file

* Manage Dependencies with `requirements.txt`

* Using [gunicorn](https://gunicorn.org/) WSGI server instead of bottle's default one

## Testing code

For automatic code testing I use [`pytest`](https://docs.pytest.org/) framework.

Here are a few code testing best practices I've learned and applied:

1. Use a Clear Testing Strategy
    * Apply **unit tests** for individual functions or components.
    * Use **integration tests** to verify how different parts interact.
    * Implement **end-to-end tests** to ensure the whole application behaves correctly.

2. Isolate Unit Tests
    * Unit tests should not depend on external systems (e.g., databases, APIs, file systems).
    * Mock external dependencies where needed.

3. Test Edge Cases
    * Validate boundary conditions (e.g., leap years).

### How to run tests?

I use `pytest 8.3.4`, so first of all we need to install it:

* ``` pip install pytest==8.3.4 ```

Also for testing we need `requests`

* ``` pip install requests==2.32.3 ```

* ``` pytest test_app.py ```
