# Python based web application

## Used packages

- **FastApi** to establish simple codebase without batteries.
- **Jinja2** to use the power of HTML templates as simply as the web app itself.
- **Uvicorn** to serve the app, because it is most commonly used with FastApi.

## Utilized practices

1. Exposing config variables to manipulate deployment easily.
2. Clear code and assets folders structure.
3. Gitignore and requirements files for a cleaner shared development.

## Notes

>The **uvicorn** was chosen instead of **gunicorn** (however it is a more advanced process manager) because the latter works only in UNIX, this is the limitation that soon will be complied to.
