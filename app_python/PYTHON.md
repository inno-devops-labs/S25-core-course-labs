## Framework choice
For the web application fastapi framework was chosen due to the following strenghs:
- Easy to start. There is no need to long configuration to start.
- FastApi supports both synchronous and asynchronous approaches.
- It's a popular framework with a large community.

## Followed best practices
- Code is formatted according to PEP8 with ruff.
- Code contains type hints and typed checked with mypy.
- Requirements is separated to required and for development.
- Configuration via environment variables. 

## Testing 
- pytest is chosen as a test framework. Pytest is more flexible and prices compared to unittests
- tests follow AAA pattern: arrange, act, assert
- using fixtures for test configuration
- tests check response status, text and that returned time does not depend on a machine timezone