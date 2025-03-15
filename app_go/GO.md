# DevOps lab1

## Choice of implementation language

I chose **Go** for this web application because of its high performance, simplicity, and scalability. **Go** is a programming language with a clean and straightforward syntax, allowing for rapid development without sacrificing maintainability.

## Choice of the framework

For this web application, which displays a random motivational quote on each page refresh, I used **Gin** because it is a lightweight and high-performance web framework for Go. It provides an intuitive API, has minimal setup requirements, and offers robust support for routing, middleware, and JSON handling.

## Best practices applied in the Web application

- **code organization:** the logic of the application is modular and clear. The random quote selection is handled directly within the route definition, while the list of quotes is maintained as a reusable slice. This structure ensures simplicity while making the code easy to maintain and extend.
- **coding standarts:** the application adheres to Go's standard coding conventions:
  - Functions, variables, and packages follow *camelCase* naming conventions.
    - Code is formatted consistently using ```gofmt```, ensuring readability and maintainability.
- **error handling:** although error scenarios are minimal for this functionality, the Gin framework's built-in mechanisms ensure robust handling of invalid routes or HTTP methods.

## Testing

For this simple functionality the web application was tested manually to ensure that random quotes are displayed on each page refresh and the JSON structure of the response is valid and correct.
