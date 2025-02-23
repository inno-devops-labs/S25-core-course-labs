FROM python:3.13.1-alpine3.21

# Environment variables
ENV ADMIN_USER="admin"

# Install the application dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy static file directory
COPY templates ./templates
# Copy python app file
COPY moscow_app.py ./

# Setup an app user so the container doesn't run as the root user
RUN adduser --system $ADMIN_USER
USER $ADMIN_USER

# Explicitly specify port
EXPOSE 5005

CMD ["python", "moscow_app.py"]
