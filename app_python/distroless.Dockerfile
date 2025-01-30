FROM python:3.11-alpine3.18 AS builder

WORKDIR /app

RUN adduser -D appuser

USER appuser
ENV PATH="/home/appuser/.local/bin:${PATH}"
ENV PYTHONPATH=/app

COPY requirements.txt requirements.txt

RUN mkdir -p /home/appuser/.local && pip install --user --no-warn-script-location -r requirements.txt

COPY . .

FROM gcr.io/distroless/python3:nonroot

WORKDIR /app
COPY --from=builder /app /app

ENV PATH="/home/nonroot/.local/bin:${PATH}"
ENV PYTHONPATH=/app

USER nonroot
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

