# Framework choosing

## For this task I created a Python web application using Flask, a lightweight and powerful web framework. Flask is ideal for this use case because

1. **Simplicity & Lightweight** – It provides an easy-to-use structure without unnecessary complexity.
2. **Quick Development** – We can set up a functional app with minimal boilerplate code.
3. **Built-in Server** – It includes a development server that makes testing easy.
4. **Extensibility** – Can be easily extended with plugins if additional features are needed.

# Coding standarts

## For my project, I followed several standarts to make code clean and readable

- The logic for retrieving the Moscow time is encapsulated in a dedicated function (get_moscow_time()), ensuring reusability.
- The Flask routes are defined separately, making it easy to extend functionality.
- Backend and Frontend parts are also separated.
- The Python code follows PEP 8, the standard style guide for Python.
- Runs the app inside the main block, which ensures that the script behaves correctly when imported as a module.

# How to run

## Please follow this steps to run this application

1. run command **pip install -r requirements.txt**
2. run command **python app.py**
3. follow **<http://127.0.0.1:5000>** on your web browser

# Unit Tests Description

## I built 3 tests for my app.py program

1. test_home_page : ensures that the home page loads successfully with 200 response.
2. test_get_time_endpoint: calls /time API and check JSON response to contain **time** field.
3. test_get_moscow_time: ensures the returned string in correctly formatted and compares with expected Moscow time.

## For my test I followed several practices, including tests separation by functions, using main block, etc
