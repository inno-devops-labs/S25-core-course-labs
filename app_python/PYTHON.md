## framework choice
I chose flask as a suitable framework for my web application because it is 
easy and most used for small web apps.

## best practices
-used 'requirements.txt' file for dependencies
-clean folder structure
-followed PEP8

## testing
- tested locally to ensure time updates on page refresh
- used 'pytz' library to handle timezone

## Unit testing
implemented unit testing using pytest and Flask's test client to validate 
that web app returns expected HTTP status and content.

how to run test:
```bash
pytest test_app.py
```

**BEST PRACTICES**
- keep tests independent
- Verify both status codes and responce content

the tests are located in `test_app.py`.

