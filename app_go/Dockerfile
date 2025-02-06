FROM golang:1.22-alpine3.18 AS builder

ENV GO111MODULE=on \
    CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64

RUN addgroup -S buildgroup && adduser -S builder -G buildgroup

WORKDIR /src

COPY go.mod go.sum ./

RUN go mod download

COPY . .

RUN go build -o app .

FROM alpine:3.18

ENV APP_ENV=production

RUN addgroup -S webgroup && adduser -S webuser -G webgroup && \
    mkdir /app && \
    apk add --no-cache curl && \
    chown webuser:webgroup /app

WORKDIR /app

COPY --from=builder /src/app .

RUN chown webuser:webgroup /app/app

USER webuser

EXPOSE 8080

HEALTHCHECK --interval=60s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8080/ || exit 1

CMD ["./app"]
