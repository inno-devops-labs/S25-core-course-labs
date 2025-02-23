# Project reasoning

## Why FastAPI framework?

1. **Native Async support** - fast and convinient
2. **Automatic OpenAPI docs generation** - great for integration and documentation
3. **Validation and Serialization of data** - no need for manual labour!
4. **Easy to test** - `fastapi.testclient` provides all you might need from an endpoint
5. **Scalable and efficient, yet easy to use** - just what anyone might need

## Coding standards and code quality

1. Clear project structure
2. Type annotations - clear documentation and code hints
3. following PEP standards religiously
4. Modern and accessible UI where possible (i.e. `aria-label`)
5. No extra comments - code should speak for itself

## Unit Testing

By breaking down the system into the minimal logical units that are represented by functions, it becomes
very easy to test the entire system using mocking and unit tests. Also introduction of `REST API`
endpoints instead of regular functions gives an opportunity for the user to choose to either use API
or UI.

Currently each python file containing logic of the application has a dedicated testing file for each 
significant function/endpoint.

