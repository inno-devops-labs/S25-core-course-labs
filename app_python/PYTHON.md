# Lab 1

## Task #1

Let's start with the description of used dependencies in the project. Because I am not the Python programmer at all, I choose a very popular `flake` framework among others. There are a lot of guides for it, and in terms of fast and single-featured applications developments, it is one of the best choices.

## Task #2

Let's separate the practice I used by parts, to properly investigate all the stuff:

- **Code Structure**: The code is separated by logical functionality, with different code files (.py):
  - `__init__.py`: The main program initialization, to start up the web application.
  - `config.py`: The startup config loader (from the dotenv file).
  - `routes.py`: The main handlers to render the static pages on the user side (browser).
  - `templates` and `static/css`: The additional user-side views, like HTML pages or CSS styles.

- **Code Style**: Linter is used, along with the useful code comments

- **Environment Files**: In the `app` folder, we also see the `.env.example` file. It is a very common practice to use such files when deploying to different production environments: dev, stage, prod.

- **Testing**: When we elevate to one level, we can see the `tests` folder. I write a single test (for the single functionality application though) just to check if it is working correctly (in some terms).

- **Ignore Files**:
  - `.dockerignore`, `.gitignore`: To get rid of unnecessary or sensitive-data files.

- **Deployment**:
  - `Dockerfile`: To properly deploy our application on different machines & different environments.
  - `requirements.txt` and `run.py`: To enumerate necessary application's dependencies and start the application by a single `.py` file.

In addition, I added the GitHub Actions that lint & test my code after it finds the open PR to the default branch (main, master). I also protect the main branch to not push on it without PR beforehand.

And that is mostly all. Information about the application you can see in the `README.md`.

# Lab 3

## Task 1

I created the next two types of unit tests:

- Tests to check the correct application functionality, like getting 200 HTTP and time in UTC+3 (MSC), or
404 when we route onto an undefined endpoint
- Tests to define the possibility of the config loader to handle different types of variables and change them
in runtime

The Best Practices:

- **Test Separation**: Separate tests into the different files to make them clearly understandable
- **Naming**: I use the proper naming for the tests to understand the main test's goal by the name only
- **Automated Tests**: To properly run tests in the different environments, I use the `unittest.main()` to automatize it
- **SetUp**: The usage of special setUp functions that configure the necessary test's environment keep the code
  clear and concise
