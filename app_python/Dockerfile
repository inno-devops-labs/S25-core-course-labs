FROM python:3.12.0-slim AS base

RUN useradd -m appuser

USER appuser

WORKDIR /app

COPY --chown=appuser:appuser requirements.txt .
COPY --chown=appuser:appuser app.py .
COPY --chown=appuser:appuser templates ./templates

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "app.py"]
