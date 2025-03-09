FROM python:3.10-slim

# Create a non-root user
RUN useradd --create-home builder
WORKDIR /home/builder

# Switch to the non-root user
USER builder

# Install dependencies
COPY requirements.txt .
RUN python -m venv venv
RUN . venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .
COPY prom.py .
COPY ./templates ./templates

# Expose port 8000
EXPOSE 8000

# Run the server
CMD ["/home/builder/venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]