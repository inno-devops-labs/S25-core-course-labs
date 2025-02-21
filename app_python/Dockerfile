FROM python:3.11-bullseye

RUN apt-get update && apt-get install -y \
    procps \
    adduser \
    coreutils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R appuser:appgroup /app && chown -R appuser /app

USER appuser

CMD ["python", "app.py"]