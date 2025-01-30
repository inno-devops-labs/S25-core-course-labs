# Python web application design

## Framework choice

I decided to use [Flask](https://flask.palletsprojects.com) for this task since
it is easy to deploy, lightweight and concise, so I can focus more on troubleshooting
the code that is doing the work required. Additionally, it also is very scalable and
supports multithreading, which will maybe help in future tasks.

For hosting the WSGI server, I used [Waitress](https://github.com/Pylons/waitress), since it is
cross-platform, decently fast, and easy to deploy. Also, it is written in pure Python, so it does
not require any more dependencies, which contributes to the cleanliness of the project.

## Best practices

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
