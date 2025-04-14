# Precise version - taken from lab description
FROM python:3-alpine3.15

# Some environment variables for Python optimization
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8080

RUN addgroup -g 1001 appuser && \
    adduser -u 1001 -G appuser -D appuser

WORKDIR /app

COPY requirements.txt .
RUN apk add --no-cache --virtual .build-deps gcc musl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

COPY . .
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE $PORT

# Run Gunicorn 
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT} --access-logfile - --error-logfile - app:app"]
