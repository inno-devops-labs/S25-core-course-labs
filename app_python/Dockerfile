FROM python:3.12.2-alpine3.19
WORKDIR /app
RUN addgroup -S appgroup && \
    adduser -S appuser -G appgroup && \
    mkdir -p /app/data && \
    chown -R appuser:appgroup /app && \
    chmod -R 755 /app/data && \
    chown -R appuser:appgroup /app/*
COPY requirements.txt .
RUN pip3.12 install -r requirements.txt
COPY app/ app/
USER appuser
CMD ["python", "-u", "app/app.py"]
EXPOSE 5000