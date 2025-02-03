# Python Web App

-----

## Framework

I chose **Flask** framework to implement this web application.
The reasons for this decision are:

- It is lightweight;
- Easy to set up the project.

So, for small projects like this one, **Flask** is one of the best choice from my point of view.

-----

## Best Practices

- **Virtual Environment**: The use of virtual environment while running the local projects ensures the isolation of dependencies and security;
- **Modularity**: The code is modular (as it can be in such small projects): separate creation of Flask instance, time function and app running;
- **Time Zone Awareness**: The use of the pytz library to handle time zones avoids issues with local system time (actually, it is incorporated to the task condition);
- **Lightweight and Scalable Design**: Flask is a lightweight framework, making it suitable for microservices and scalable applications;
- **Testing**: All application features (time showing, updating the time while web page refreshing) were tested locally.

-----

## Coding Standards

- PEP 8 guidelines for Python;
- Meaningful names for variables;
- Comments where needed.

-----

## Unit Tests

Unit tests for the Flask application are implemented using Python's built-in framework `unittest`.

### Unit Testing Best Practices

- **Timezone Awareness**: Both naive and aware datetime objects are handled appropriately to avoid errors during comparisons.
- **Tests Should Be Simple**: Low cyclomatic complexity for low number of possible execution paths.
- **Test Shouldn’t Duplicate Implementation Logic**: In order not to make the same mistake in the code and in tests, implementation logic of the code and tests made in different ways.
- **Tests Should Be Readable**: Commented tests, Assert pattern for tests, one assertion per test method.

-----
