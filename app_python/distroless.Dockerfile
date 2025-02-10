FROM python:3.12.0-slim AS builder

WORKDIR /app

COPY requirements.txt .
COPY app/.env* ./
COPY app ./app
COPY run.py .

RUN pip install --no-cache-dir --target=/app/dependencies -r requirements.txt

FROM gcr.io/distroless/python3-debian12:nonroot

WORKDIR /app

COPY --from=builder /app .

ENV PYTHONPATH=/app/dependencies

ENTRYPOINT ["python", "run.py", ".env"]
