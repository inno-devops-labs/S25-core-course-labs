# Build Stage
FROM debian:12-slim AS build
### Update package list and install necessary dependencies
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv=3.11.2-1+b1 gcc=4:12.2.0-3 libpython3-dev=3.11.2-1+b1 && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Build virtualenv
FROM build AS build-venv
### Set the working directory for the application
WORKDIR /app
### Copy requirements file
COPY requirements.txt /requirements.txt
### Install requirements
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt
### Copy the app
COPY . .

# Running app
FROM gcr.io/distroless/python3-debian12:nonroot
### Use nonroot user
USER nonroot
### Set the working directory for the application
WORKDIR /app
# Copy virtualenv and app code
COPY --from=build-venv /venv /venv
COPY --from=build-venv /app /app
# Expose the port
EXPOSE 8000
# Set the entry point for running the application using uvicorn
ENTRYPOINT ["/venv/bin/python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]