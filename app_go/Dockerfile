# Build Stage
FROM golang:1.23-alpine3.19 AS builder

WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY cmd ./cmd
COPY internal ./internal

RUN CGO_ENABLED=0 GOOS=linux go build -o=./bin/app_go ./cmd/api/main.go

# Runtime Stage
FROM alpine:3.19

RUN adduser -D user1 && \
    mkdir -p /app && \
    chown -R user1 /app

WORKDIR /app

COPY --from=builder --chown=user1 /app/bin/app_go .

ENV PORT=8080 \
    APP_ENV=local

USER user1

EXPOSE 8080
CMD ["./app_go"]