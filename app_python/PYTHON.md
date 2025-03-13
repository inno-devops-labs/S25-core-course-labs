# Python Web Application: Current Moscow time

## Choice of the framework

For the web application which displays the current time in Moscow I used **FastAPI** because I had an experience of working with it earlier. Moreover, this framework offers high performance and scalability, has built-in data validation (Pydantic), and proposes simple and intuitive design.

## Best practices applied in the Web application

- **code organization:** the logic of the application is divided into corresponding special functions such as ```get_moscow_time()``` for handling time retrieval and formatting and ```read_root()``` for handling HTTP GET requests for the root endpoint. This approach makes the code modular and reusable.
- **coding standarts:** the use of *type hints* improves code readability, *following naming conventions* confirms Python's official style guide, and *clear and descriptive naming* ensures better developer experience.
- **error handling:** ```get_moscow_time()``` function includes ```try-except``` block to handle unexpected errors gracefully with corresponding erroe message instead of crashing the app.
- **logging:** logging mechanism helps to impove error tracking and unexpected behavior in the code.

## Unit Testing

### Unit Tests Implemented

1. ```test_get_moscow_time()``` – Ensures ```get_moscow_time```returns a valid string in the ```HH:MM:SS``` format.
2. ```test_read_root()``` – Mocks ```get_moscow_time``` and checks if the FastAPI root endpoint returns the expected response.
3. ```test_invalid_route()``` – Ensures that a request to a non-existent route returns a *404 Not Found* error.

### Best Practices Applied for Unit Testing

- ```pytest```: ```pytest``` is a simple and effective framework for easy test discovery and execution.
- **mocking external dependencies**: the ```get_moscow_time``` function was mocked to ensure the endpoint response is predictable.
- **following the AAA pattern**: each test case is structured into Arrange (setup), Act (execute function), and Assert (check results).
- **ensuring full test coverage**: tests include:
- checking if ```get_moscow_time``` returns a valid string format.
  - mocking time retrieval to validate endpoint response.
  - verifying that an invalid route returns a *404 error*.
