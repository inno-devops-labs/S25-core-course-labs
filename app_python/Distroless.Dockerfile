FROM python:3.12-slim as build
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir --target=/app -r /app/requirements.txt
COPY ./app.py ./app.py
# Create a Distroless image for the runtime environment
FROM gcr.io/distroless/python3:nonroot
WORKDIR /app
# Copy the app and its dependencies
COPY --from=build /app /app
EXPOSE 5000
CMD ["-m", "flask", "run", "--host=0.0.0.0"]
