FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    adduser \
    coreutils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R appuser:appgroup /app

USER appuser

CMD ["python", "app.py"]