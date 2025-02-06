# Web Application Framework Choice

I chose **Flask** for this Python web application because it is lightweight, easy to set up
and doesn't require much coding, which is ideal for a small project like this one.
Flask also has a good documentation, great internet resources that describe it, 
provides sufficient flexibility to handle small web applications and lastly, I have at least some experience in it. 

I chose **Datetime** for the inside logistics of the application, since it is bundled with python and is sufficient to
build an application of this type, provided that the host machine itself has a correct time 
(not necessarily the correct timezone, as was required).

# Best Practices and Coding Standards:

Code structure: The code is organized into clear, separate files (app.py and the template in the templates folder).
Flask conventions: Proper usage of render_template to separate HTML from Python code, making the code more maintainable (as per Flask coding standards).
Time formatting: The time is formatted as '%Y-%m-%d %H:%M:%S' for clarity and consistency.

For testing I have thoroughly tested the application myself by launching it in different environments, 
which included changing the timezone of the host machine, which did not affect the time in Moscow, as was intended.
However, by changing the machine's system time itself I was able to fool the application and change the time 
and date in Moscow, however I believe that this vulnerability is not critical to the application as 
it is meant to be initialized on a machine with a proper system time, 
which works perfectly even if the machine changes the region mid-execution.

Ultimately, I simply researched the available fixes for such a rare vulnerability, and
it is only fixable using external APIs (which is to be expected from our knowledge of the course of Networks), 
which I consider to be a much more major source of vulnerabilities than the host machine system time.

For checking the quality of the app.py I used Pylint, and it gave 7.78/10 score and noted the lack of docstrings.
I consider this to be too small of a program to warrant docstrings,
provided that I commented on all the non-obvious lines and provided a README file.
I also used Peer-review and my peer commented that "this is good code". None more comments were given.

I used pipreqs to generate requirements.txt (and checked it manually again for good measure).

# Unit testing

For unit testing I have had to check [this article about general unit tests](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices)
as well as well as [this article about python unit tests](https://codefresh.io/learn/unit-testing/unit-testing-in-python-quick-tutorial-and-4-best-practices/)
(Although it was not very useful) and also [this article about flask specifically](https://flask.palletsprojects.com/en/stable/tutorial/tests)
, as it had very clear examples of what to do.

### Avoid infrastructure dependencies

I have no dependencies on the infrastructure and that (along with other factors) makes the tests surprisingly fast.

### Naming your tests

I have named my tests clearly.

### Arranging your tests

In [here](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices#arranging-your-tests)
there is a structure of the tests:
1. Arranging the objects
2. Acting on the objects
3. Asserting expectations

I have followed this structure when creating my tests, to the best of my abilities (some parts may not have all the steps, see the comments)

### Avoid multiple acts

I have just one action in each test.

### Also acknowledged best practices for unit tests:

1. Stub static references:
    - No need to stub any static reference in my tests.
3. Validate private methods by unit testing public methods:
    - No extra methods to use this on.
3. Prefer helper methods to setup and teardown:
   - [This structure](https://flask.palletsprojects.com/en/stable/tutorial/tests/) 
   seems to be the best practice specifically for flask, but these points are taken from 
   [here](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices#arranging-your-tests),
   so I kept it the way it is.
4. Avoid magic strings:
   - There are no magic strings except for time format, which I believe to be best left there.
5. Write minimally passing tests:
   - There is no way to write my tests any other way.