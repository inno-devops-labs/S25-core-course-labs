# Coding description

## Frameworks used

Flask is used for its lightweight. It is efficient enough for such small apps (Django or similar will be to heavy for that).

Timezone is handled with use of `pytz`, it doesn't depend on server location.

## Code style

- Separation of logic and template (`app.py` and `index.html`)
- Readable code, following PEP8
- Manual testing
- Dependencies in `requirements.txt`
- Unnecessary files are indicated in `.gitignore`

## Unit tests

Unit tests are developed for the application to ensure its functionality and further use them on CI.
The tests include check the root route to verify that the index page renders correctly 
and checking of the /time route to ensure that it returns correct JSON response.

Best practices: test isolation, repeatability, simplicity 
are applied to make the tests effective and maintainable. 
Also Flask test_client is used to simulate requests to the application.
