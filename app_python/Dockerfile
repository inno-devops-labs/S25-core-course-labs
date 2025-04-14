# 1) Use a pinned version of Python on Alpine
FROM python:3.11-slim

# 2) Create a non-root user
RUN useradd -m python_user

# 3) Set a working directory
WORKDIR /app

# 4) Copy ONLY necessary files (best practice)
COPY requirements.txt /app/

# 5) Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6) Copy the application code
COPY main.py /app/

# 7) Switch to non-root user
USER python_user

# 8) Expose port 5000 (Flask default)
EXPOSE 5000

# 9) Define the command
CMD ["python", "main.py"]
