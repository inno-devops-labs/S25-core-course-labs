FROM python:3.9-alpine3.20 AS builder

COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

FROM gcr.io/distroless/python3-debian12:nonroot

WORKDIR /app

COPY templates ./templates
COPY app.py ./
EXPOSE 8000

ENV PYTHONPATH=/app/site-packages

COPY --from=builder /usr/local/lib/python3.9/site-packages /app/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

CMD ["/usr/local/bin/python", "app.py"]

# This fails and I do not know why