# Python application

## Framework:

For the current lab was chosen a Flask framework since it is a easy-to-understand framework that allows convenient debug mode for applications

### Best practices:

* Application was written according to the PEP8 standart.

* Testing was realised using a built-in Flask debugger. However, its functionality was tested by simply refreshing the page several times.

* Enabled SSL for security purposes using adhoc (that is the one of the simplest way to do it and for developement it is better to acquire a real sertificate rather than self-signed).

## Unit testing:

### Created tests:

* 1st test - check the availability of the app (check for response status code 200).

* 2nd test - check the speed of the response.

* 3rd test - check that the time aligns with the real time in Moscow at the moment request was created.

### Best practices:

* **@pytest.decorator** was used to create a client fixture to simplify creating the client for multiple tests.

* Each test function has a clear, descriptive name and addresses a single aspect of the application.
