# Stage 1: Builder
FROM golang:1.23 AS builder

# Set working directory
WORKDIR /app

# Copy go.mod and go.sum for dependency management
COPY go.mod go.sum ./

# Download dependencies
RUN go mod download

# Copy the rest of the application code
COPY . .

# Build the binary
RUN CGO_ENABLED=0 GOOS=linux go build -o moscow-time-app main.go

# Stage 2: Final Image
FROM gcr.io/distroless/static-debian11

# Set working directory
WORKDIR /app

# Copy the binary from the builder stage
COPY --from=builder /app/moscow-time-app .

# Expose the correct port
EXPOSE 8080

# Set the entrypoint
CMD ["/app/moscow-time-app"]


