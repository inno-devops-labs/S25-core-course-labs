# Python slim base image with sha256 digest
FROM python:3.12.8-slim@sha256:69ce3aed05675d284bee807e7c45e560e98db21fb1e4c670252b4ee0f2496b6d

# Maintainer information
LABEL maintainer="Darya Koncheva d.koncheva@innopolis.university"

RUN groupadd -r appgroup && useradd --no-log-init -r -g appgroup appuser

# Set workdir
WORKDIR /code

# Copy and install all needed requirements
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# Copy source code
COPY templates/index.html templates/index.html
COPY main.py main.py

# Expose 5000 port
EXPOSE 5000

USER appuser

# Command to run application
ENTRYPOINT ["python", "main.py"]
