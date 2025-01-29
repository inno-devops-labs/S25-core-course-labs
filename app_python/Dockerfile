FROM python:3-alpine3.15

WORKDIR /app

COPY requirements.txt .

RUN addgroup -S appgroup && \
    adduser -S appuser -G appgroup && \
    pip install --no-cache-dir -r requirements.txt

USER appuser

COPY . .

CMD ["python", "app.py"]