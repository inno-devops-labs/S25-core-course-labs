FROM python:3.11-alpine3.18

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

WORKDIR /app_python

COPY --chown=appuser:appgroup requirements.txt .
COPY --chown=appuser:appgroup time_app/manage.py .
COPY --chown=appuser:appgroup time_app/ ./time_app

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

CMD ["python3", "time_app/manage.py", "runserver", "0.0.0.0:8000"]
