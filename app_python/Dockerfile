# specific version of base image
FROM python:3.9-alpine

WORKDIR /app

# only specific files copying
COPY requirements.txt .
COPY app.py .
COPY templates/index.html templates/

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
