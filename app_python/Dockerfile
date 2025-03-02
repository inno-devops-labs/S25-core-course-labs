FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Use a non-root user for security
RUN useradd -m appuser
USER appuser

EXPOSE 5000
CMD ["python", "app.py"]
