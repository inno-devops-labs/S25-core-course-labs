FROM golang:1.23-alpine3.20

RUN addgroup -g 1001 appgroup && \
    adduser -D -u 1001 -G appgroup appuser

WORKDIR /app

COPY . .

RUN go mod download && \
    go build -o /app/service

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 8080

CMD ["/app/service"]
