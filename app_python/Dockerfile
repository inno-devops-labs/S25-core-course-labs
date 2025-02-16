FROM python:3.11.6-slim-bullseye

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

RUN chown appuser:appgroup /app

COPY --chown=appuser:appgroup requirements.txt /app/requirements.txt
COPY --chown=appuser:appgroup main.py /app/main.py
COPY --chown=appuser:appgroup app_python.py /app/app_python.py

RUN pip install --no-cache-dir -r /app/requirements.txt

USER appuser:appgroup

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
