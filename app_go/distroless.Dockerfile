FROM golang:1.23.5-bullseye AS builder

# Set environment variables to prevent prompts during package installation
ENV CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64

# Create a non-root user
RUN useradd -ms /bin/bash appuser

WORKDIR /app

COPY main.go .

# Build the application
RUN go build -o main.out main.go

FROM gcr.io/distroless/static:nonroot

WORKDIR /

# Copy the compiled application from the builder stage
COPY --from=builder /app/main.out .

# Switch to non-root user
USER nonroot:nonroot

EXPOSE 8080

CMD ["./main.out"]
