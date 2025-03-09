FROM python:3.11-alpine3.18

RUN adduser -D appuser && \
    mkdir -p /app && \
    chown appuser:appuser /app

WORKDIR /app
USER appuser

COPY --chown=appuser:appuser requirements.txt requirements.txt

RUN pip install --user --no-warn-script-location -r requirements.txt

COPY --chown=appuser:appuser . .

ENV PATH="/home/appuser/.local/bin:${PATH}"
ENV PYTHONPATH=/app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
