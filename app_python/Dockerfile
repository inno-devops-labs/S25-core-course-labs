# Use a lightweight and secure Python image
FROM python:3-alpine3.15

# Create a non-root user for better security
RUN addgroup -g 1007 app && adduser -u 1007 -G app -D app
# Swtich to the non-root user
USER app

WORKDIR /app_python

# Copy the application files with the correct permissions
COPY --chown=app:app requirements.txt .
COPY --chown=app:app main.py .
COPY --chown=app:app templates templates
COPY --chown=app:app visits .

# Install the application dependencies preventing unnecessary cache
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variables
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["python", "-m", "flask", "run"]