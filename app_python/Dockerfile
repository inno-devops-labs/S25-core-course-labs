# Use a specific version of Python Alpine
FROM python:3.9-alpine3.15

LABEL maintainer="Kirill Arkhipov <karhipov606@gmail.com>"
LABEL version="1.0"
LABEL description="Python Flask Time Application"

RUN adduser -D appuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates ./templates
COPY static ./static

RUN chown -R appuser:appuser /app

USER appuser

# Expose the correct port (8000 instead of 5000)
EXPOSE 8000

# Command to run the application
CMD ["python", "app.py"]