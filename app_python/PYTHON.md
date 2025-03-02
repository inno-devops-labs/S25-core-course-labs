# Python Web Application

## Chosen Framework
This python application was developed using Flask framework because of its simplicity and flexibility which is perfect for small project like this task. 

## Best Practices
The best practices followed in the application are as follows:
- PEP 8: code is formatted according to PEP 8 standart.
- File organisation: files are separated into modules according to their function (e.g. templates).
- requirements.txt: all dependencies are listed for quick setup.
- python venv: application is launched inside of venv to avoid dependcy version conflicts.

## Coding Standards
Code follows standard python guidelines (PEP 8).

## Testing
Flask's built in server was used to ensure correct functionality during development. The timestamps were verified manually against Moscow's current time. Page was refreshed few times in order to verify that the displayed time is in fact updated.

I use pytest for unittesting. Currenlty there is 1 main test for application that verifies correctness of shown time.

## Code Quality
The use of comments was minimal as the code was developed to be self-explanatory. README file was used to provide necessary documentation. The `requirements.txt` file was used to list all the dependencies for the project. 
