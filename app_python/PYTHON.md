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
