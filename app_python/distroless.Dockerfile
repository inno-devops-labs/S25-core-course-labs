FROM python:3.9.18-alpine3.15 as build

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --target /app/deps

COPY main.py .

FROM gcr.io/distroless/python3.9:nonroot

WORKDIR /app

COPY --from=build /app /app

# Expose port 5000
EXPOSE 5000

ENTRYPOINT ["/usr/bin/python3","/app/main.py"]
