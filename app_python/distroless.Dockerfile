FROM python:3.9-slim as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --target /python/lib/python3.9/site-packages

COPY ./app .

# Production stage
FROM gcr.io/distroless/python3-debian11:nonroot

WORKDIR /app

COPY --from=builder /app ./app
COPY --from=builder /python/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]