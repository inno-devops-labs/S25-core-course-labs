FROM python:3.11-alpine3.21 AS builder

COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

FROM gcr.io/distroless/python3-debian12:nonroot

WORKDIR /app

COPY resources ./resources
COPY app.py ./
EXPOSE 8000

ENV PYTHONPATH /usr/lib/python3.11/site-packages

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

CMD ["/usr/local/bin/waitress-serve", "--host", "0.0.0.0", "--port", "8000", "app:app"]
