FROM python:3.9-alpine3.15

RUN adduser -D appuser
USER appuser

WORKDIR /app

COPY requirements.txt .
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Run the application
CMD ["python3", "app.py"]
