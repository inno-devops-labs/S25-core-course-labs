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
- **Modularity**: The code is modular (as it can be in such small projects): separate creation of Flask instance, time function and app running.
- **Time Zone Awareness**: The use of the pytz library to handle time zones avoids issues with local system time (actually, it is incorporated to the task condition).
- **Lightweight and Scalable Design**: Flask is a lightweight framework, making it suitable for microservices and scalable applications.
- **Testing**: All application features (time showing, updating the time while web page refreshing) were tested locally.

-----

## Coding Standards
- PEP 8 guidelines for Python;
- Meaningful names for variables;
- Comments where needed.