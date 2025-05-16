# Stage 1: Build
FROM python:3.13.1-alpine3.21@sha256:f9d772b2b40910ee8de2ac2b15ff740b5f26b37fc811f6ada28fce71a2542b0e AS builder

# Set environment variables
ENV VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create a virtual environment
RUN python3 -m venv $VIRTUAL_ENV

# Install dependencies
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install --no-cache-dir -r requirements.txt

# Stage 2: Final
FROM python:3.13.1-alpine3.21@sha256:f9d772b2b40910ee8de2ac2b15ff740b5f26b37fc811f6ada28fce71a2542b0e

# Set environment variables
ENV VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Copy the virtual environment from the builder stage
COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV

# Create a non-root user
RUN addgroup -g 1001 app && \
    adduser -u 1001 -G app -D app

USER app

# Set the working directory
WORKDIR /app_python

# Copy the application code
COPY --chown=app:app app.py ./app.py
COPY --chown=app:app templates ./templates


# Expose application port
EXPOSE 5000

# Define the entry point for the application
ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=5000"]