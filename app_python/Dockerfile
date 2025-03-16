FROM python:3.9-alpine3.15

# Set the working directory inside the container
WORKDIR /app

# Copy only files allowed in dockerignore
COPY . .

# install reqs and create user
RUN apt update && apt install -y dnsutils
RUN pip install --no-cache-dir -r requirements.txt && adduser -D webapp
RUN touch /app/app.log && chmod 777 /app/app.log
USER webapp

EXPOSE 5000

CMD ["python", "run.py"]