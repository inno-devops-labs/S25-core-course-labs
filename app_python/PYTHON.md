# Develop and Test Python Web Application

## Choosing a Framework

For this application, **FastAPI** was chosen due to its:

- **High performance** (asynchronous support with `uvicorn`)
- **Built-in support for type hints** and automatic API documentation
- **Ease of development and maintainability**

## Best Practices Applied

- **Separation of Concerns:** HTML templates are separate from Python logic using Jinja2.

- **Code Readability:** Good function names and code structure.
- **Modular Design:** Using FastAPI and template rendering makes the project scalable.

## Python Unit Tests

### Best Practices

- Naming of the tests describe the intent of the test clearly
- Testing only one concern with each testing fucntion
- Using the AAA pattern (Arange, Act, Assert)

### Unit Test Overview

The function `get_moscow_time()` is tested to verify:

- Correct dictionary structure.
- Valid time values.
