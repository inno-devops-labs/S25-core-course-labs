FROM python:3.12-alpine3.18 AS base

RUN adduser app_python_user --system --shell=/bin/false
WORKDIR /app_python

COPY --chown=app_python_user:app_python_user requirements.txt ./
COPY --chown=app_python_user:app_python_user app/ ./app/
COPY --chown=app_python_user:app_python_user app/templates/ ./app/templates/

RUN pip install -r requirements.txt

USER app_python_user
EXPOSE 8080

CMD ["sh", "-c", "python3 -m gunicorn --bind 0.0.0.0:8080 app.app:app"]
