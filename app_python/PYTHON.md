# Python app report

## Decisions

- FastAPI as the framework. Django is overkill for this simple task, Flask is okay but isn't as expressive. App isn't the main focus of a DevOps course anyway
- Uvicorn as an ASGI server. Any ASGI server will do but FastAPI uses Starlette which is built on Uvicorn so it's one dependency less if I use Uvicorn as an ASGI server.
- Pytest is used for testing. It's as simple as unittest but with optional async support and less boilerplate required.

## Best practices

### Coding

- Type linter in the IDE is used to check for potential type errors.
- TzInfo is used. Who knows what kind of deranged regulations might be applied to Moscow time zone in the future? Doesn't work on Windows because of that decision, but it's not important to the project.
- Ruff is used for linting and formatting (code readability is important). It's same as Black but faster (and contains isort and flake8 functionality as well)
- venv is proposed to the user as a way to isolate dependencies.

### Testing

- The endpoint behavior and timezone parsing is thoroughly tested.
- Code coverage is not a particularly reliable metric. You could have 100% code coverage just checking it doesn't throw any errors.
- A unit test should direct express the intent of a user story. East step in the story is the "unit".
- It is good to use helper methods to set up the env to not add noise to the test code. Since the code is time-sensitive, I've moved the time retrieving logic to a separate class and mocked its response in the tests that are not related to the time retrieving logic itself and made an easy-to-inherit fixture.
- Testing only one concern is generally good. For example, if your unit test asserts on more than a single object, it may be testing more than one concern.

