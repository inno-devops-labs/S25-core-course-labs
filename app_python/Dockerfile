FROM python:3.12-alpine3.18

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN adduser -D appuser && \
    mkdir -p /app/templates /app/data && \
    chown -R appuser:appuser /app
WORKDIR /app
COPY --chown=appuser:appuser requirements.txt app.py /app/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
COPY --chown=appuser:appuser templates/ /app/templates/
EXPOSE 8080
USER appuser
CMD ["python", "app.py"]