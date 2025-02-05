# Stage 1
FROM python:3.11-slim-bookworm AS builder

WORKDIR /app 

COPY ./app /app
COPY ./templates /templates
COPY requirements.txt .


RUN pip install --no-cache-dir --upgrade -r requirements.txt && cp "$(command -v uvicorn)" /app

# Stage 2
FROM gcr.io/distroless/python3:nonroot

COPY --from=builder /app /app
COPY --from=builder /templates /templates
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

WORKDIR /

ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages
CMD ["app/main.py"]