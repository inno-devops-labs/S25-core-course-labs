# DevOps lab1

## Choice of the framework

For the web application which displays the current time in Moscow I used **FastAPI** because I had an experience of working with it earlier. Moreover, this framework offers high performance and scalability, has built-in data validation (Pydantic), and proposes simple and intuitive design.

## Best practices applied in the Web application

- **code organization:** the logic of the application is divided into corresponding special functions such as ```get_moscow_time()``` for handling time retrieval and formatting and ```read_root()``` for handling HTTP GET requests for the root endpoint. This approach makes the code modular and reusable.
- **coding standarts:** the use of *type hints* improves code readability, *following naming conventions* confirms Python's official style guide, and *clear and descriptive naming* ensures better developer experience.
- **error handling:** ```get_moscow_time()``` function includes ```try-except``` block to handle unexpected errors gracefully with corresponding erroe message instead of crashing the app.
- **logging:** logging mechanism helps to impove error tracking and unexpected behavior in the code.

## Testing

For this simple functionality the web application was tested manually to ensure the displayed time updates upon page refreshing.
