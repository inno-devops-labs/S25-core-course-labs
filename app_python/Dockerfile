FROM python:3.9-slim

WORKDIR /app

RUN apk add --no-cache \
    shadow \
    && rm -rf /var/cache/apk/*
    
COPY requirements.txt .

RUN addgroup -S appgroup && \
    adduser -S appuser -G appgroup && \
    pip install --no-cache-dir -r requirements.txt

USER appuser

COPY . .

RUN chown -R appuser:appgroup /app

CMD ["python", "app.py"]