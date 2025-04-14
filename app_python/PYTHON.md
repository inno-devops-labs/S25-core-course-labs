# Lab 1: Web Application Development

## Framework choice

I have chosen:

- **FastAPI** _for web application development_. [FastAPI](https://fastapi.tiangolo.com/) is performant and easy to use framework for building web applications, with support of async operations. I believe that it is a good choice, especially for such simple applications.
- **Jinja2** _for template rendering_. [Jinja2](https://pypi.org/project/Jinja2/) is a fast, expressive and extensible templating engine. It includes a sandboxed environment and async operations support, which are very useful for web applications and untrusted templates rendering. I believe that it is a reliable choice with possibility of future extending of its functionality to our needs.
- **Pydantic** _for data models_. [Pydantic](https://docs.pydantic.dev/latest/) has a rich set of features to validate and transform data, which may become very useful in the future development of this application. Pydantic has built-in data processing tools, such as regex, enums, string manipulation, etc. Moreover, FastAPI supports specifying Pydantic models as a response models, which is very convenient.
- **BeautifulSoup** _for web page scraping_. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) is a Python library for parsing HTML and XML documents. It is useful to test if the correct time displayed on the web page.

## Implemented Best Practices

- **Logic separation** - the application logic belongs in Python (implemented in main.py), while the UI is implemented in a separate templates directory and its functionality is not restricted.
- **PEP8 standard compliance** - I have followed the [PEP8](https://peps.python.org/pep-0008/) coding standards while implementing this web application.
- **Documentation** - all functionalities of FastAPI application are documented (including docstrings). The Swagger documentation includes possible response codes and bodies, and the list of all available endpoints.
- **Data validation** - endpoints response bodies are validated using Pydantic models. They are specified in the endpoint decorator.
- **Linting and formatting** - I have used [pylint](https://docs.pylint.org/) for code linting and [black](https://black.readthedocs.io/en/stable/) for code formatting.
- **BEM methodology** - [BEM](https://en.bem.info/methodology/) helps to create extendable and reusable interface components. It was used in the HTML template.

## Testing

This application was tested manually by refreshing the page and checking if the displayed time is correct ([resource](https://time100.ru) with the actual Moscow time).
