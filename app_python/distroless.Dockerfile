# Prepare production dependencies
FROM python:3.11-slim AS deps-env
WORKDIR /app

COPY /static ./static
COPY /templates ./templates
COPY main.py ./main.py
COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt -t /app

# Create final production stage
FROM gcr.io/distroless/python3-debian12:nonroot AS run-env
WORKDIR /app

COPY --from=deps-env /app ./

EXPOSE 8000
CMD ["main.py"]