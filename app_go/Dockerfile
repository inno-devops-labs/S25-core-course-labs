FROM golang:1.22.5-alpine AS builder

WORKDIR /app

ADD go.mod .
ADD go.sum .

RUN go mod download

COPY main.go .

RUN addgroup -S appuser && \
    adduser -S -G appuser appuser && \
    chown -R appuser:appuser /app
USER appuser

EXPOSE 8080

CMD ["go", "run", "main.go"]