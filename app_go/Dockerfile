FROM golang:1.21-alpine AS builder

WORKDIR /app

COPY main.go .
RUN go mod init app && go mod tidy
RUN go build -o myapp main.go

FROM alpine:latest

RUN adduser -D -g '' appuser
USER appuser

WORKDIR /app
COPY --from=builder /app/myapp .

CMD ["/app/myapp"]
