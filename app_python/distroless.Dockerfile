# Stage 1: Building stage
FROM python:3.10-slim AS build

WORKDIR /app

# install
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/app/packages -r requirements.txt

COPY app.py .
COPY templates/ ./templates/
COPY static/ ./static/


# Stage 2: Runtime stage (non-root user)
FROM gcr.io/distroless/python3:nonroot as final

WORKDIR /app
COPY --from=build /app /app

# ensure Python uses the custom packages path
ENV PYTHONPATH=/app/packages


EXPOSE 5000
CMD ["app.py"]
