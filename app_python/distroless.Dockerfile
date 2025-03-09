FROM python:3.10-alpine AS build-env

WORKDIR /app

COPY main.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt && \
    cp $(which uvicorn) /app

FROM gcr.io/distroless/python3-debian11 AS final

WORKDIR /app

COPY --from=build-env /app /app

COPY --from=build-env /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

ENV PYTHONPATH=/usr/local/lib/python3.10/site-packages

USER nonroot

EXPOSE 8000

CMD ["./uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]