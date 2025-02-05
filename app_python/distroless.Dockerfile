FROM python:3.11-slim AS builder

# Set the working directory 
WORKDIR /app_python

# Copy the file with dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && cp $(which uvicorn) /app_python

# Copy the main file and other web site files 
COPY app.py .
COPY static/ static/
COPY templates/ templates/

# Use a distroless image without root privileges 
FROM gcr.io/distroless/python3:nonroot

# Change to the working directory 
WORKDIR /app_python

# Copy data from the intermediate image and other necessary components 
COPY --from=builder /app_python /app_python
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages

# Open a port to access the application
EXPOSE 8000

# Command to run web app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]