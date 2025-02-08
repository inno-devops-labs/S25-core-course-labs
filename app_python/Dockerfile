FROM python:3-alpine3.15

RUN adduser -D worker
USER worker

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY templates ./templates

CMD ["python", "app.py"]

