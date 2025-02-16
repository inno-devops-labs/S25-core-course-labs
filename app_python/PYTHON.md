# Python Web Application

## Framework choice

I chose `Flask` framework because it is one of the most used frameworks applied to web frameworks. It is simple to use, very lightweight, flexible in adding new features, and has great scalability.  

## Best practices

- Code contains commentaries to improve readability.
- The application is kept simple and focused on a single responsibility: displaying the current time in Moscow. So the code is written using Single Responsibility principle.
- Code was formatted by `black` formatter, so it is adhered to PEP-8 guidelines.
- Code was analyzed using `pylint` framework and was rated 10/10.

## Unit tests

There are three unit tests provided:

1. Checking response code of the web application.
2. Checking content of the response.
3. Checking correctness of time provided.
