FROM python:3.12.8-alpine3.21@sha256:ba13ef990f6e5d13014e9e8d04c02a8fdb0fe53d6dccf6e19147f316e6cc3a84

LABEL description="This is a simple python app" maintainer="s.asekrea@innopolis.university"

# prevents Python from writing compiled Python files to the disk --> reduces image size
ENV PYTHONDONTWRITEBYTECODE=1

# logs and output are shown in real-time on terminal --> easier to debug
ENV PYTHONUNBUFFERED=1



# Create a non-root user
RUN addgroup -S app_group && adduser -S app_user -G app_group

WORKDIR /app

# Requiments is copied first to cache installation of dependencies
COPY requirements.txt /app/app_python/requirements.txt

RUN pip install --no-cache-dir --upgrade pip==25.0 \
    && pip install --no-cache-dir --upgrade -r app_python/requirements.txt

# Copy python files
# reduce the number of layers by copying all files at once
COPY __init__.py app.py time_template.html app_service.py /app/app_python/

# Change the owner of the app_python directory
RUN chown -R app_user:app_group /app/

# Switch to the non-root user
USER app_user

# Expose the port
EXPOSE 8000

# Run the app
# More workers can handle more concurrent requests (scale horizontally)
# but it depnds on the project complexity and the server resources .
CMD ["gunicorn", "app_python.app:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]