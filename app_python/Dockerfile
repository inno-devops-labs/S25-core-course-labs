FROM python:3.9-slim-bullseye

WORKDIR /app

# Install python dependencies (no caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# create system group and usr to launch app without root
RUN groupadd --system appgroup && \
    useradd --system --gid appgroup appuser

# Copy app code into workdir
COPY . .

# Change owner of files to created group and usr
RUN chown -R appuser:appgroup /app

# Select created usr
USER appuser

EXPOSE 5000

CMD ["python3", "app.py"]