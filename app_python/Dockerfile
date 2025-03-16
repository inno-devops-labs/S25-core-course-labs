FROM python:3.10-alpine3.15

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

# Create data directory with proper permissions
RUN mkdir /data && \
    chown -R appuser:appgroup /data && \
    chmod 755 /data

COPY requirements.txt .
COPY app.py .
COPY templates/ templates/

RUN pip install --no-cache-dir -r requirements.txt
RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 5000
EXPOSE 8000

CMD ["python", "app.py"]