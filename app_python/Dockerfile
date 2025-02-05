# Use official Python image as a base
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the Flask default port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
