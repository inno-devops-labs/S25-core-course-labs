# If i use 3.11-alpine it does not work :(
FROM python:3.11-slim AS builder

WORKDIR /service

COPY service/ ./
COPY requirements.txt ./

# Install dependencies into a dedicated directory
RUN pip install --no-cache-dir -r requirements.txt \
    && cp $(which uvicorn) /service

FROM gcr.io/distroless/python3:nonroot

WORKDIR /service

COPY --from=builder /service /service
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
