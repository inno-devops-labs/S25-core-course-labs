# Use the python:3.12.8-alpine3.21 image with the sha256 digest as the base image
FROM python:3.12.8-alpine3.21@sha256:ba13ef990f6e5d13014e9e8d04c02a8fdb0fe53d6dccf6e19147f316e6cc3a84

# Maintainer information
LABEL maintainer="a.bayramov@innopolis.university"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user
RUN addgroup -S app_group && adduser -S app_user -G app_group

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip==24.3.1 && pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the source code
COPY main.py ./
COPY index.html ./

# Change the ownership of the app directory to the non-root user
RUN chown -R app_user:app_group /app

# Change the user to the non-root user
USER app_user

# Expose the port the app runs on
EXPOSE 8001

# Set the command to run the app
CMD ["python", "main.py"]
