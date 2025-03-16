# Official Python runtime, slim since the project do not need full Python image
FROM python:3.12-slim

# Working directory in the container
WORKDIR /app_python

RUN apt update && apt install -y dnsutils

# Non-root user
RUN useradd -m python_user && \
    mkdir -p /app_python/data && \
    chown python_user:python_user /app_python/data && \
    chmod 755 /app_python/data
USER python_user

# Copy only the necessary files
COPY --chown=python_user:python_user requirements.txt .
COPY --chown=python_user:python_user app.py .

# Install needed libraries with no cache
RUN pip install --no-cache-dir -r requirements.txt

# Set the port for the app
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run the app
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
