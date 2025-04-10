# Build stage using Go
FROM golang:1.23-alpine AS builder

# Set working directory
WORKDIR /app

# Copy go.mod and go.sum to cache dependencies
COPY go.mod ./
RUN go mod download

# Copy application source code
COPY . .

# Build the application binary
RUN go build -o app .

# Final runtime stage using Distroless
FROM gcr.io/distroless/static:nonroot

# Set working directory
WORKDIR /app

# Copy only the necessary built binary and required files
COPY --from=builder /app/app .
COPY --from=builder /app/templates ./templates
COPY --from=builder /app/quotes.txt .

# Expose the application port
EXPOSE 8080

# Run the application
CMD ["/app/app"]
