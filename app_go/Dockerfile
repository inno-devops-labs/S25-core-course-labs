# Use the golang:1.23.5-alpine3.21 image with the sha256 digest as the build stage base image
FROM golang:1.23.5-alpine3.21@sha256:47d337594bd9e667d35514b241569f95fb6d95727c24b19468813d596d5ae596 AS build

# Maintainer information
LABEL maintainer="a.bayramov@innopolis.university"

# Set the working directory
WORKDIR /build

# Copy the source code
COPY main.go ./

# Build the Go application
RUN go build -o app main.go

# Use the alpine:3.21.2 image with the sha256 digest as the final base image
FROM alpine:3.21.2@sha256:56fa17d2a7e7f168a043a2712e63aed1f8543aeafdcee47c58dcffe38ed51099

# Create a non-root user
RUN addgroup -S app_group && adduser -S app_user -G app_group

# Install the tzdata package for the timezone data
RUN apk add --no-cache tzdata=2024b-r1

# Set the working directory
WORKDIR /app

# Copy the app and index.html from the previous stage
COPY --from=build /build/app ./
COPY index.html ./

# Change the ownership of the app directory to the non-root user
RUN chown -R app_user:app_group /app

# Change the user to the non-root user
USER app_user

# Expose the port the app runs on
EXPOSE 8002

# Set the command to run the app
CMD ["./app"]
