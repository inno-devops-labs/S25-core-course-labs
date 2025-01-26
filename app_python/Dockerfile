FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
COPY ./app ./app
COPY app/.env* .
COPY run.py .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "run.py", ".env"]
