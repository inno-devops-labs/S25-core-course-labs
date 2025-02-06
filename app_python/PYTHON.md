# Python web application design

## Framework choice

I decided to use [Flask](https://flask.palletsprojects.com) for this task since
it is easy to deploy, lightweight and concise, so I can focus more on troubleshooting
the code that is doing the work required. Additionally, it also is very scalable and
supports multithreading, which will maybe help in future tasks.

For hosting the WSGI server, I used [Waitress](https://github.com/Pylons/waitress), since it is
cross-platform, decently fast, and easy to deploy. Also, it is written in pure Python, so it does
not require any more dependencies, which contributes to the cleanliness of the project.

## Best practices in application

### Code quality

I used the following techniques to ensure code standarts and code quality:

- Moving the timezone into a global constant variable
- Commenting
- Following PEP8 style
- Using tools such as pylint to check the code
- Descriptive variable names

### Testing

I tested the application in different timezones, and it provided me with the
same time as before, the Moscow time. The time is neatly formatted and even
displays nicely on mobile devices. CSS sheet loads correctly and affects page.

### Other

I have maintained a clean requirements.txt file, since the program only requires Flask and Waitress
to run. Furthermore, instead of inlining the HTML and CSS, I moved them into their respective
directories, so that they can be changed independently of the code.

## Unit tests

For unit tests I have used pytest module that can automatically integrate with Flask,
run multiple tests, and provide clear output, including code coverage with another
module.

I have implemented multiple various unit tests to test different parts of application:

- Check the accessibility of website
- Check the unavailability of time at any page other that the root (/)
- Check that the root page has relevant text (In this case, the word "Moscow")
- Test that the time on the page matches the current time in Moscow (with 1 second margin of error)
- Test that the time on the page changes if we internally change the timezone
- Test that the format on the page changes if we internally change the format

### Best practices

I have implemented these best practices in my unit testing:

- Avoid infrastructure dependencies
  There are no dependencies in the test except on the standart library and the testing library
- Naming your tests
  All tests' names describe what should happen in them
- Arranging your tests
  As some tests are small, they fit into just act and assert, but the last tests first setup
  relevant variables, then get the page status, then check if it is correct
- Write minimally passing tests
  Tests only have things that are necessary for them to check what they need to check
- Avoid magic strings
  All parameters of tests are in global variables with descriptive names
- Avoid multiple acts
  All tests only make one request and then check it for correctness on one things
