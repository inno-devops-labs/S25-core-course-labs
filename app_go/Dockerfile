FROM golang:1.12-alpine AS builder
WORKDIR /app
COPY . .
RUN go build -o go-app

FROM debian:bullseye-slim
WORKDIR /app
COPY --from=builder /app/go-app .
RUN adduser nonroot
USER nonroot
EXPOSE 8080

CMD ["./go-app"]