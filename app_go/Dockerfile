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

FROM alpine:3.21.2

WORKDIR /app

# Copy the compiled application from the builder stage
COPY --from=builder /app/main.out .

# Switch to non-root user
RUN addgroup --system user && \
    adduser --system --ingroup user user && \
    chown -R user:user /app
USER user

EXPOSE 8080

CMD ["./main.out"]
