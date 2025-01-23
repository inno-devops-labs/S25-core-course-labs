# Python Web Application

## Tech Stack

* Python
* FastApi, as it's most used Python Framework
for backend nowadays and has all needed functionalities.

## Best practises

* I have followed KISS principle which is the most suitable for such simple apps.
* I have configured project using [poetry](https://python-poetry.org/)
* I have configured `pre-commit` hooks (see [.pre-commit-config.yaml](.pre-commit-config.yaml))
* I have configured static type checking using [mypy](https://mypy-lang.org/)
* I have configured code formatting
  with [pylint](https://www.pylint.org/), [black](https://black.readthedocs.io/en/stable/#),
  and [isort](https://pycqa.github.io/isort/)
* I have configured [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli)
for formatting markdown files.

## Testing

The application is tested manually by me by comparing output
with [timeanddate.com](https://www.timeanddate.com/worldclock/russia/moscow)
