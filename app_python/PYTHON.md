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