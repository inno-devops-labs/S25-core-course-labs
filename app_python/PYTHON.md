# Python application

## Framework Choice

I decided to use FastAPI since it provides really fast creation of a simple web app like this, without any boilerplates. Additionally, it has very friendly documentation, which makes developing process faster and bug fixing easier.

Also, for further enhancement of an application, unlike Django, this framework has good support and ease of use for an async functions.

## Best practices

- Compliance with PEP-8 (it was ensured by configured autopep8 in neovim text editor, which formats on the save)
- Pydantic validation (schemas.py)
- Using asynchronous HTTP client/server by aiohttp
- Separating logic to different files, routes - in router.py, main.py - running the application

Testing was done by hands (browsing [localhost](http://localhost:8000/time)), since no code testing needed by the task.
