# Stage 1: Build
FROM golang:1.23-alpine3.21@sha256:47d337594bd9e667d35514b241569f95fb6d95727c24b19468813d596d5ae596 AS builder

# Set working directory inside the container
WORKDIR /app_go

# Create a non-root user for security and assign permissions
RUN addgroup -g 1001 app && adduser -u 1001 -G app -D app && \
    chown -R app:app /app_go

# Switch to the non-root user
USER app

# Copy application files (Go source code and dependencies)
COPY --chown=app:app app.go go.mod ./
COPY --chown=app:app templates ./templates

# Download dependencies and compile the application
RUN go mod tidy && go mod download && go build -o app

# Stage 2: Final minimal image
FROM gcr.io/distroless/static-debian12:nonroot

# Set working directory inside the final container
WORKDIR /app_go

# Copy only the compiled binary and templates from the builder stage
COPY --from=builder /app_go/app /app_go/app
COPY --from=builder /app_go/templates /app_go/templates

# Expose the application port
EXPOSE 3500
ENTRYPOINT ["./app"]
