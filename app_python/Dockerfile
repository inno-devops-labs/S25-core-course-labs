FROM python:3.11-bullseye

# Set the working directory
WORKDIR /app

# Install the required dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY visits/ visits/

# Copy the application
COPY app.py .

RUN apt update && apt install -y dnsutils

# Create user
RUN addgroup --system user && \
    adduser --system --ingroup user user && \
    chown -R user:user /app
USER user

# Expose the port that Flask uses
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
