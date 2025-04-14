# Build and install dependencies
FROM python:3.9-slim AS build

# set the working directory inside the container
WORKDIR /app

# copy the requirements temporarily to the working directory and install them
RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
    pip install --target=/install --no-cache-dir --requirement /tmp/requirements.txt

# copy application files
COPY app.py templates/ .

# import python distroless image
FROM gcr.io/distroless/python3-debian12:nonroot

# set the working directory inside the container
WORKDIR /app

# set PYTHONPATH to point to the installed dependencies
ENV PYTHONPATH=/app/packages

# copy only the installed Python packages (related to requirements.txt)
COPY --from=build /install /app/packages

# copy the application files
COPY app.py .
COPY templates/ ./templates

# expose the app's port (8000 as the setup in the main app code)
EXPOSE 8000

# set the default command to run the Flask app
CMD ["app.py"]
