FROM python:3.10-slim

# working directory is app
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# for health checking
RUN apt-get update && apt-get install -y curl

# creating non-root user and give him ownership of the /app dir
RUN addgroup --system appuser && \
    adduser --system --group appuser && \
    chown -R appuser:appuser /app
USER appuser

COPY app.py .
COPY templates/ ./templates/
COPY static/ ./static/

EXPOSE 5000
CMD ["python3", "app.py"]