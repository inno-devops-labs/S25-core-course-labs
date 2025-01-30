FROM python:3.10-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM gcr.io/distroless/python3:nonroot
WORKDIR /app
COPY --from=builder /app /app
COPY . .

# Expose the Flask application port
EXPOSE 5000

# Run the application
CMD ["app.py"]
