FROM golang:1.23-alpine AS builder

WORKDIR /app

COPY go.mod ./

COPY . .

RUN go build -o main .

RUN apk add --no-cache tzdata

FROM gcr.io/distroless/base-debian10:nonroot

WORKDIR /app

COPY --from=builder /app/main .

EXPOSE 8080

CMD ["./main"]
