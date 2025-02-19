FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

COPY app.py /app/
COPY templates /app/templates/

FROM gcr.io/distroless/python3:nonroot

WORKDIR /app

COPY --from=builder /install /usr/local

COPY --from=builder /app /app

EXPOSE 5001

CMD ["python3", "/app/app.py"]
