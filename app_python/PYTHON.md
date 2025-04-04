## Moscow Time Application
### 1. Choice Justification
Flask is easy and beginner-friendly framework that allows fast webapp coding. Hopefully, if the future labs will require us to extend this application, __flask lightweight nature__ will support highly covering the lack of __built-in admin interface__ that [Django](https://en.wikipedia.org/wiki/Django_(web_framework)) has.

### 2. Best Practices
1. [Docstring](https://peps.python.org/pep-0257/) briefly explaining every program component/module involved in the system. Yes, this regards Python conventions rather, but always putting reasonable comments makes developers/readers understand the structure faster... In most of the cases.
2. Constants Usage. In such a small example of moscow_app.py making MOSCOW timezone a constant makes no use, but in larger projects by changing the address of this variable all the rest code will get a new reference.
3. Confident requirements.txt via automatic __'pip freeze > requirements.txt'__ command.
4. Coding conventions: [Pylint](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint) extension highlights problematic pieces of code to be changed.

## Unit-Testing
### 1. Unit-test list
* ```test_status_code(self)``` - makes sure that GET request successfully returns an html page with __200__ Status Code
* ```test_response_content(self)``` - Checks that the received webpage contains lines that we needed 
* ```test_validate_time(self)``` - Time comparison between then one the program calculated and the one obtained from the response, with request-response delay considerations
### 2. Best Practices
* __Isolated environment__. Tests do not have any side effects hurting other tests' output
* __Setting test_app framework in class__. This avoids multiple application initialization for all the tests.
* __Assertion with considering possible environmental requests__. That is, when comparing the time values in assert, an error value must be introduced to allow some deviation between values to be approximately equal.