FROM python:3.9 as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM gcr.io/distroless/python3-debian11
WORKDIR /app
COPY --from=builder /app /app
COPY app.py .
CMD ["python", "app.py"]
