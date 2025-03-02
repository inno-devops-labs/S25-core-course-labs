# Python application

## Framework Choice

I decided to use FastAPI since it provides really fast creation of a simple web app like this, without any boilerplates. Additionally, it has very friendly documentation, which makes developing process faster and bug fixing easier.

Also, for further enhancement of an application, unlike Django, this framework has good support and ease of use for an async functions.

### Best practices

- Compliance with PEP-8 (it was ensured by configured autopep8 in neovim text editor, which formats on the save)
- Pydantic validation (schemas.py)
- Using asynchronous HTTP client/server by aiohttp
- Separating logic to different files, routes - in router.py, main.py - running the application

Testing was done by hands (browsing [localhost](http://localhost:8000/time)), since no code testing needed by the task.

## Unit tests

Probably there are not so many tests are might be implemented for one GET endpoint, so I came up with two:

- Test if application returns 200 status code by GET request to the endpoint
- Test if correct timezone (in our case is MSK, so UTC+3) is shown after retrieval

I used test client application provided by fastapi so there is no need to run it by hands on another process.

Applied best practices:

- Simple atomic independent tests
- Separated logic - class with methods to operate with application and class for unit tests which uses these methods keeping clean testing class itself
- URL is specified in class variable making it easier to change or load from `.env` afterwards
