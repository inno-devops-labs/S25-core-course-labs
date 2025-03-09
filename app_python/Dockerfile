# Build stage
FROM python:3.11-alpine3.20 as builder

WORKDIR /app

ENV PYTHONUSERBASE=/app/packages

COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.11-alpine3.20

WORKDIR /app

RUN apk add --no-cache tzdata

COPY --from=builder /app/packages/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

COPY app.py .

RUN adduser -D myuser && \
    chown -R myuser:myuser /app

USER myuser

EXPOSE 8080

CMD ["python", "app.py"]