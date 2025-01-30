FROM python:3.11-slim-bookworm

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY ./templates ./templates

WORKDIR /app

RUN groupadd --system appuser && useradd --system --gid appuser appuser && \
    chown -R appuser:appuser /app

USER appuser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
