# syntax=docker/dockerfile:1
FROM python:3.9-alpine@sha256:43e2664b1c5cc23c9f1db305f2689191f1235de390610a317af7241fe70e19cc

ENV APP_TIMEZONE=Europe/Moscow
EXPOSE 8080

# Add user
RUN adduser app --system -s /bin/false

# Install requirements
COPY --chown=app:app requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY --chown=app:app app.py .
COPY --chown=app:app app_start.py .
COPY --chown=app:app app_test.py .

USER app

# Run tests
RUN [ "python", "app_test.py" ]

# Run application
CMD [ "sh", "-c", "python app_start.py -t \"${APP_TIMEZONE}\"" ]
