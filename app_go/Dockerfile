# Use the golang:1.23.5-alpine3.21 image with the sha256 digest to pin the image version
FROM golang:1.23.5-alpine3.21@sha256:47d337594bd9e667d35514b241569f95fb6d95727c24b19468813d596d5ae596

LABEL maintainer="a.bayramov@innopolis.university"

# Create a non-root user
RUN addgroup -S app_group && adduser -S app_user -G app_group

# Set the working directory
WORKDIR /app

# Copy the source code
COPY main.go ./
COPY index.html ./

# Build the Go application
RUN go build -o app main.go

# Change the ownership of the app directory to the non-root user
RUN chown -R app_user:app_group /app

# Change the user to the non-root user
USER app_user

# Expose the port the app runs on
EXPOSE 8002

# Set the command to run the app
CMD ["./app"]
