FROM python:3.12.0-slim AS base

RUN useradd -m appuser

USER appuser

WORKDIR /app

COPY --chown=appuser:appuser requirements.txt .
COPY --chown=appuser:appuser app/.env* ./
COPY --chown=appuser:appuser app ./app
COPY --chown=appuser:appuser run.py .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "run.py", ".env"]
