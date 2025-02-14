# Setting base image
FROM golang:1.23.5-alpine AS builder

# Setting working directory
WORKDIR /app

# Copying files necessarry for build
COPY /cmd ./cmd
COPY go.mod go.sum ./
COPY /internal ./internal

# Downloading Go packages and building an app
RUN go mod download && \
    go build -o goapp ./cmd/numerologist/main.go

# Base image for the final Go app image
FROM alpine:3.21 AS final

# Setting working directory
WORKDIR /app

# Copying static content and binary
COPY --from=builder /app/cmd/numerologist/static /app/static
COPY --from=builder /app/goapp /app/.

# Creating user with limited permissions
RUN addgroup -S user && \
    adduser -S -G user user && \
    chown -R user:user /app
USER user

# Exposing a port
EXPOSE 8080

# Creating entrypoint
ENTRYPOINT [ "./goapp" ]