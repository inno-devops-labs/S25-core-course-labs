
# Overview

This is a small python service that displays time !

## The choise of Fastapi as web-framework

Fastapi is one of the most performative ASGI framework, supporting async operations. It also comprises simplicity, ideal for implementing such a small service like that.

## Best practices

- **Formatting** (flake8)
- (Coding standarts) **Linting** (Pylint)
- (Code quality) **Static type checking** (mypy)
- Multiple files separated by responsibility

## Testing implementation

Manual testing is performed for the lab 1, involving

- Polling the web page in browser locally

## Unit testing

For the lab 3, additional automated testing was implemented.

As codebase of the service is small, and it has single functionality, the only subject that we may reasonably test. Thus, in tests, we make a simple client that requests the root endpoint and verifies that it really shows current time.
