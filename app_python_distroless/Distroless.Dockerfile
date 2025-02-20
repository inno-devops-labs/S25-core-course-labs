# Use Python 3.11 slim image based on Debian bookworm for the build stage
FROM python:3.11-slim-bookworm as builder

# Set the working directory to /app in the container
WORKDIR /app

# Copy the requirements.txt file into the container's working directory
COPY requirements.txt .

# Update the package list, install necessary system dependencies (gcc and python3-dev for building C extensions), and install Python dependencies from requirements.txt
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    pip install --user --no-cache-dir -r requirements.txt

# Runtime Stage
# Use a distroless Python image based on Debian 11 with non-root user for the runtime environment
FROM gcr.io/distroless/python3-debian11:nonroot

# Set the working directory to /app in the container
WORKDIR /app

# Copy the installed Python packages from the builder stage to the runtime stage
COPY --from=builder /root/.local /home/nonroot/.local

# Copy the application file app.py and change ownership to the non-root user
COPY --chown=nonroot:nonroot app.py .

# Set the Python path and include the user-installed binaries in the system PATH
ENV PYTHONPATH=/home/nonroot/.local/lib/python3.11/site-packages \
    PATH=/home/nonroot/.local/bin:$PATH

# Expose port 5001 for the app to communicate
EXPOSE 5001

# Switch to the non-root user for running the application
USER nonroot

# Command to run the Python application
CMD ["app.py"]
