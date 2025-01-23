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

In addition to testing by running the application locally and comparing it with the current time, I have written several automated tests in `test_app.py` file.

### How to run tests?

I use `pytest 8.3.4`, so first of all we need to install it:

* ``` pip install pytest==8.3.4 ```

Also for testing we need `requests`

* ``` pip install requests==2.32.3 ```

* ``` pytest test_app.py ```
