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

# Use the gcr.io/distroless/static-debian12:nonroot image with the sha256 digest as the final base image
FROM gcr.io/distroless/static-debian12:nonroot@sha256:6ec5aa99dc335666e79dc64e4a6c8b89c33a543a1967f20d360922a80dd21f02

# Set the working directory
WORKDIR /app

# Copy the built app from the previous stage
COPY --from=build /build/app ./

# Copy the index.html
COPY index.html ./

# Expose the port the app runs on
EXPOSE 8002

# Set the command to run the app
CMD ["./app"]
