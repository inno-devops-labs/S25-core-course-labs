FROM python:3.9-alpine3.15

ENV PYTHONUNBUFFERED=1

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

COPY requirements.txt requirements.txt
COPY app.py app.py
COPY templates templates

RUN pip install --no-cache-dir -r requirements.txt

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
