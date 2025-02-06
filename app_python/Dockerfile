FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    adduser \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser && \
    pip install --no-cache-dir -r requirements.txt

USER appuser

COPY . .

RUN chown -R appuser:appgroup /app

CMD ["python", "app.py"]