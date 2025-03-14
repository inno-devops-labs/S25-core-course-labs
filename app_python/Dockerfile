FROM python:3.11-alpine3.19

RUN adduser -D appuser

WORKDIR /app

# Create data directory and set permissions
RUN mkdir -p /data && chown -R appuser:appuser /data && chmod 755 /data

COPY --chown=appuser:appuser requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser app.py .

USER appuser

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["python", "app.py"]
