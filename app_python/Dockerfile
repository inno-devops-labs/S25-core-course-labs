FROM python:3.11-alpine3.18  AS build

RUN adduser -D app_python_user

USER app_python_user

WORKDIR /app_python

COPY --chown=app_python_user:app_python_user app.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app_python_user:app_python_user templates/ ./templates/

EXPOSE 5000

CMD ["python3", "app.py"]

