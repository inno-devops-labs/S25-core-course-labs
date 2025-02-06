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

FROM gcr.io/distroless/base:nonroot

USER 65532:65532

WORKDIR /app

COPY --from=builder /src/app /app/app

EXPOSE 8080

HEALTHCHECK --interval=60s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

CMD ["/app/app"]
