FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y \
    shadow \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN addgroup -S appgroup && \
    adduser -S appuser -G appgroup && \
    pip install --no-cache-dir -r requirements.txt

USER appuser

COPY . .

RUN chown -R appuser:appgroup /app

CMD ["python", "app.py"]