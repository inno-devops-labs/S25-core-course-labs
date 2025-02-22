FROM python:3.10-alpine3.15

# set not root user for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# set working directory inside the container
WORKDIR /app

# copy files (only necessary ones to reduse image size)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the application
COPY app.py .

# expose the port Flask runs
EXPOSE 5000

# define the command to run app
CMD ["python", "app.py"]
