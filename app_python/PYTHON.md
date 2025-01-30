# Python app report

## Decisions

- FastAPI as the framework. Django is overkill for this simple task, Flask is okay but isn't as expressive. App isn't the main focus of a DevOps course anyway
- Uvicorn as an ASGI server. Any ASGI server will do but FastAPI uses Starlette which is built on Uvicorn so it's one dependency less if I use Uvicorn as an ASGI server.
- Pytest is used for testing. It's as simple as unittest but with optional async support and less boilerplate required.

## Best practices

- Type linter in the IDE is used to check for potential type errors.
- TzInfo is used. Who knows what kind of deranged regulations might be applied to this time zone in the future?
- Ruff is used for linting and formatting (code readability is important). It's same as Black but faster (and contains isort and flake8 functionality as well)
- Since the code is time sensitive, I've moved the time retrieving logic to a separate class and mocked its response in the tests that are not related to the time retrieving logic itself.
