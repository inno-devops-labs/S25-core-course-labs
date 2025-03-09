# Use the debian:12-slim image with the sha256 digest as the build stage base image
FROM debian:12-slim@sha256:f70dc8d6a8b6a06824c92471a1a258030836b26b043881358b967bf73de7c5ab AS build

# Maintainer information
LABEL maintainer="a.bayramov@innopolis.university"

# Install the required packages and create a virtual environment
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv=3.11.2-1+b1 libpython3-dev=3.11.2-1+b1 && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip==24.3.1

# Install dependencies
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --no-cache-dir --disable-pip-version-check -r /requirements.txt

# Use the gcr.io/distroless/python3-debian12:nonroot image with the sha256 digest as the final base image
FROM gcr.io/distroless/python3-debian12:nonroot@sha256:66f3e24fd4906156a7360d2861731d31d3457a02f34fd3c4491f0b710a259988

# Set the working directory
WORKDIR /app

# Copy the virtual environment with the installed dependencies from the previous stage
COPY --from=build /venv /venv

# Copy the source code
COPY main.py ./
COPY index.html ./

# Expose the port the app runs on
EXPOSE 8001

# Set the command to run the app
ENTRYPOINT ["/venv/bin/python3", "main.py"]
