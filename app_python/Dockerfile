# Step 1: Use an official lightweight Python image as the base
FROM python:3.11-slim

# Step 2: Set environment variables to ensure output is logged immediately
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy requirements.txt into the container
COPY requirements.txt /app/requirements.txt

# Step 5: Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Step 6: Copy the rest of the application code
COPY . /app

# Step 7: Expose the port the app runs on
EXPOSE 8000

# Step 8: Command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
