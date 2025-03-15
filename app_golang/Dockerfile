FROM golang:alpine AS builder

LABEL stage=gobuilder

ENV CGO_ENABLED=0

RUN apk update --no-cache && apk add --no-cache tzdata

WORKDIR /build

COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN go build -ldflags="-s -w" -o /app/main main.go

FROM scratch

COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo

ENV DOCKER_ENV=true

WORKDIR /app
COPY --from=builder /app/main /app/main

EXPOSE 8080

CMD ["./main"]
