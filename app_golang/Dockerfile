# Use the official Go image for building
FROM golang:1.23-alpine AS builder

# Set working directory
WORKDIR /app

# Copy only the necessary files
COPY go.mod ./
RUN go mod download

# Copy the rest of the application files
COPY . .

# Build the Go application
RUN go build -o app .

# Use a minimal runtime image
FROM alpine:3.18

# Create a non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# Set working directory
WORKDIR /app

# Copy the built application and necessary files
COPY --from=builder /app/app .
COPY --from=builder /app/templates ./templates
COPY --from=builder /app/quotes.txt .

# Expose the application port
EXPOSE 8080

CMD ["./app"]
