FROM golang:1.23-alpine AS builder

WORKDIR /app

COPY go.mod ./

COPY . .

RUN go build -o main .

FROM alpine:latest

RUN apk add --no-cache tzdata

RUN addgroup -S group && adduser -S user -G group

WORKDIR /app

COPY --from=builder /app/main .

USER user

EXPOSE 8080

CMD ["./main"]
