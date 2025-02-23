# Build Stage
FROM golang:1.23-alpine3.19 AS builder

WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download

COPY cmd ./cmd
COPY internal ./internal

RUN CGO_ENABLED=0 GOOS=linux go build -o=./bin/app_go ./cmd/api/main.go

# Distroless Runtime
FROM gcr.io/distroless/static-debian12:nonroot

WORKDIR /app
COPY --from=builder --chown=nonroot:nonroot /app/bin/app_go .

ENV PORT=8080 \
    APP_ENV=local

USER nonroot:nonroot
EXPOSE 8080
CMD ["/app/app_go"]