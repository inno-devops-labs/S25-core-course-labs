FROM python:3.9.18-alpine3.15 as base

RUN adduser -D -u 1000 myuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 5000

USER myuser

CMD ["python", "main.py"]
