# Framework and Coding Standards & Practices

## Framework choice

I decided to choose **FastAPI** for this task and let's see why.

### Task nature

We are required to create a web app that displays Moscow time.
The task is very simple, and a lightweight framework with simplistic design would suffice.

### Popular options

+ Django
+ Flask
+ FastAPI

### Reasoning

Django is a heavyweight framework that includes a lot of task irrelevant features like
ORM, admin panel, database migrations, and more. This fact makes it a questionable choice.

Flask and FastAPI are both lightweight python frameworks for creating http servers. Here comes the
factor of experience and personal bias. I like FastAPI better because it is easier to get up
and running (IMO), it is more performant, native asynchronous support is great, and it also has a bunch of pre-built docker images.

## Used Practices and Standards

1. PEP8
    + Proper indentation and spacing
    + Clear naming
    + Limited line length
    + Organized imports

2. Project Structure
    + Application logic is located in the app/ directory
    + Static files (html) are in a dedicated templates/ folder
    + **init__.py file to signal that it is a package for modular usage
    + main.py is a starting point of the application
    + Bash script for simpler startup

3. FastAPI practices
    + Usage of appropraite HTTP methods
    + Dynamic templating
    + Typed function parameters

4. Dependency management
    + Clean requirements.txt that specifies only necessary dependencies

5. Semantic HTML
