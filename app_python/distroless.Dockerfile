# Use an official Python image as the base for building the app
FROM python:3.13.1-alpine3.21 AS builder

# Set environment variables to make the image more secure
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && cp "$(which gunicorn)" /app

# Copy the rest of the application code into the container
COPY app.py .

# Use Distroless as the runtime image
FROM gcr.io/distroless/python3-debian12:nonroot AS runtime

# Copy application files from builder
WORKDIR /app
COPY --from=builder /app /app
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.11/site-packages
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages

# Expose the port that the app will run on
EXPOSE 8080

# Command to run the app using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]
