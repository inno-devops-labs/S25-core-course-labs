# Web Application Language Choice

I chose **PHP** for my language of choice because I wanted to figure out how it works and learn something new. 
As it turned out nothing else is necessary, although I would like to launch it originally in *Docker*,
as it is currently the main way of using **PHP**, but I decided to leave it for lab 2.

# Best Practices and Coding Standards:

Code structure: the code is now in a single file, which makes this small application very easy to debug and port.

Best practices: the user experience should be better since the time is now in the center, 
unlike in my previous application (Although I chose not to modify that web application to better differentiate).

Testing: I have tested the application by launching it with a different timezone, yet it always shows the correct Moscow time.
However, just like with the previous application, if we change the system time directly, then that will affect the result,
but since the fix for this is to create a request to gain accurate time, which itself is prone to errors, I chose to leave it (just like the last time).
