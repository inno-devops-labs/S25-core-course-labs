# # Build Stage (Install dependencies and build the app)
# FROM python:3-alpine3.15 AS build-stage

# WORKDIR /app

# # Copy the requirements file and install dependencies
# COPY requirements.txt . 
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application code
# COPY . . 

# # Custom Distroless Stage with Python installed
# FROM gcr.io/distroless/python3:nonroot

# # Copy Python binary, installed packages, and application code from build stage
# COPY --from=build-stage /usr/local/bin/python3 /usr/local/bin/python3
# COPY --from=build-stage /usr/local/lib/python3.*/site-packages /usr/local/lib/python3.*/site-packages
# COPY --from=build-stage /app /app

# # Set the PYTHONPATH to the location where Python packages are installed
# ENV PYTHONPATH=/usr/local/lib/python3.*/site-packages

# # Expose the port the app will run on
# EXPOSE 5000

# # Run the application with the non-root user
# CMD ["/app/main.py"]


# Build Stage (Install dependencies and build the app)
FROM python:3-alpine3.15 AS build-stage

WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Custom Distroless Stage with Python installed
FROM gcr.io/distroless/python3:nonroot

# Copy Python binary and the installed site-packages (dependencies) from the build stage
COPY --from=build-stage /usr/local/bin/python3 /usr/local/bin/python3
COPY --from=build-stage /usr/local/lib/python3.*/site-packages /usr/local/lib/python3.*/site-packages

# Copy the application code from the build stage
COPY --from=build-stage /app /app

# Set the PYTHONPATH to the location where Python packages are installed
ENV PYTHONPATH=/usr/local/lib/python3.*/site-packages

# Expose the port the app will run on
EXPOSE 5000

# Set the entry point to the app
CMD ["/app/main.py"]

