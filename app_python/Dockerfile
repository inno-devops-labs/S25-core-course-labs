FROM python:3.10-slim

# working directory is app
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# visits check
RUN mkdir data
RUN echo "0" > data/visits

# for health checking
RUN apt-get update && apt-get install -y curl

# to access pods via DNS
RUN apt update && apt install -y dnsutils

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