FROM python:3.9-slim AS builder

WORKDIR /app

COPY app.py .
COPY requirements.txt .
COPY templates/ templates/

RUN pip install --no-cache-dir -r requirements.txt

FROM gcr.io/distroless/python3:nonroot

COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
ENV PYTHONPATH=/usr/local/lib/python3.9/site-packages

WORKDIR /app

ENV FLASK_APP="app.py"

EXPOSE 8080

ENTRYPOINT ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]