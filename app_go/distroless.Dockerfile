FROM golang:1.12 AS builder
WORKDIR /app
COPY . .
RUN go build -o go-app

FROM gcr.io/distroless/base-debian12:nonroot
WORKDIR /app
COPY --from=builder /app/go-app .
EXPOSE 8080

CMD ["./go-app"]