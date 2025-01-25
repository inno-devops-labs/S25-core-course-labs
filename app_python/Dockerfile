# use python3.12 and alpine3.18 as the most stable versions for production
FROM python:3.12-alpine3.18 AS base

RUN addgroup -S app_python_user_group
# use --uid to prevent user_id inconsistencies
RUN adduser --system --no-create-home --uid 1001 app_python_user -G app_python_user_group

# cd to /app_python
WORKDIR /app_python

# copy all needed files
# specify app_python_user file ownership
COPY --chown=app_python_user:app_python_user_group app.py requirements.txt ./
COPY --chown=app_python_user:app_python_user_group templates/ ./templates/
COPY --chown=app_python_user:app_python_user_group utils/ ./utils/

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# login as app_python_user
USER app_python_user

EXPOSE 8080

# run the web-app
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:app"]
