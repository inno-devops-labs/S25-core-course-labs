# using lightweight image
FROM python:3.10-slim-bullseye

# setting a non-root user
RUN useradd -m nonrootuser
USER nonrootuser

# setting working directory and environment variables
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# installing dependencies
COPY --chown=nonrootuser:nonrootuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy application code
COPY --chown=nonrootuser:nonrootuser app.py .

# exposing port and setting the entry point
EXPOSE 5000
CMD ["python", "app.py"]
