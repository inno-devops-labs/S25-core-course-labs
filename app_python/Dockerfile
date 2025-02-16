FROM python:3.9-alpine3.15

RUN adduser -D appuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/main.py .

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]