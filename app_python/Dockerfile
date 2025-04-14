
# use the official latest ubuntu base image
FROM python:3-alpine3.15

# set the working directory inside the container
WORKDIR /app

# copy the requirements temporarily to the working directory and install them
RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
    pip install --no-cache-dir --requirement /tmp/requirements.txt

# copy the projects content to the container working directory
COPY app.py /app/
COPY templates/index.html /app/templates/

# expose the app's port (8000 as the setup in the main app code)
EXPOSE 8000

# set the default command to run the Flask app
CMD ["python3", "app.py"]