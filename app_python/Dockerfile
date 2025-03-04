# Setting base image
FROM python:3.10-alpine AS builder

# Setting working directory
WORKDIR /app

# Installing requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copying static and code files
COPY static/ static/
COPY templates/ templates/
COPY main.py .

# Creating user with limited permissions
RUN addgroup -S user && \
    adduser -S -G user user && \
    chown -R user:user /app
USER user

# Exposing a port and creating an entrypoint
EXPOSE 8000
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]