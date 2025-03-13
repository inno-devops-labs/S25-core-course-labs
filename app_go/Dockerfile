FROM golang:1.12-alpine AS builder
WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 go build -o go-app

FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/go-app .
RUN apk add --no-cache tzdata
RUN adduser -D nonroot
USER nonroot
EXPOSE 8080

CMD ["./go-app"]