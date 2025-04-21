FROM python:3.10-alpine3.18 AS base
LABEL authors="dmhd6219"

RUN adduser app_python_user --system --shell=/bin/false
WORKDIR /app_python
RUN mkdir -p /data && chown app_python_user:app_python_user /data

COPY --chown=app_python_user:app_python_user main.py requirements.txt ./
COPY --chown=app_python_user:app_python_user templates/ ./templates/
COPY --chown=app_python_user:app_python_user static/ ./static/
COPY --chown=app_python_user:app_python_user pyapp/data/ ./data/

RUN pip install --no-cache-dir -r requirements.txt



USER app_python_user

EXPOSE 8000
ENTRYPOINT ["fastapi", "run", "--host", "0.0.0.0", "--port", "8000"]