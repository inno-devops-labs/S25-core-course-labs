FROM python:3.9-alpine3.17

WORKDIR /app

COPY requirements.txt .

COPY app.py .

RUN apk add --no-cache tzdata \
    && pip install --no-cache-dir -r requirements.txt

RUN addgroup -S app && adduser -S app -G app

USER app

CMD ["python", "app.py"]
