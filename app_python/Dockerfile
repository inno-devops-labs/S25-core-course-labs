FROM python:3.11-slim-bullseye

# Set the working directory
WORKDIR /app

# Install the required dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY app.py .

# Create user
RUN addgroup --system user && \
    adduser --system --ingroup user user && \
    chown -R user:user /app
USER user

# Expose the port that Flask uses
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
